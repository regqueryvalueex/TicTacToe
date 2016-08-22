import json

from django.core.cache import cache

from channels import Group
from channels.sessions import channel_session, enforce_ordering
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from django.utils import timezone

from .tic_tac_field import TicTacField, TicTacFieldSerializer
from . import models


CELL_VALUES = ['X', 'O']

def populate_message(action, message='', **kwargs):
    msg = {
        'action': action,
        'details': {
            'message': message,
        }
    }
    msg['details'].update(kwargs)
    return {'text': json.dumps(msg)}

# Connected to websocket.connect
@enforce_ordering(slight=True)
@channel_session
@channel_session_user_from_http
def ws_connect(message):
    # Work out room name from path (ignore slashes)

    room = message.content['path'].strip("/")

    g = Group("game-%s" % room)
    g.history = []
    Group("game-%s" % room).add(message.reply_channel)

    message.channel_session['room'] = room

    game_info = cache.get("game-%s" % message.channel_session['room'], {})

    game = models.Game.objects.get(pk=room.split('-')[-1])
    if game.finished or game.aborted:
        return

    if not 'game-id' in game_info:
        game_info['game-id'] = game.id
        game_info['game-field'] = TicTacFieldSerializer.serialize(TicTacField.from_game(game))

    open_games = cache.get('open_games', set())

    game_info.setdefault('players-queue', [])
    game_info.setdefault('players', {})
    if len(game_info['players-queue']) < 2:
        number = 0
        if game_info['players-queue'] and game_info['players'][game_info['players-queue'][0]]['name'] == 'Player-2':
            number = 1
        game_info['players-queue'].append(message.reply_channel.name)
        number = number or len(game_info['players-queue'])
        game_info['players'][message.reply_channel.name] = {
            'name': 'Player-%s' % number,
            'symbol': CELL_VALUES[number-1]
        }
        Group("game-%s" % message.channel_session['room']). \
            send(populate_message('game-action',
                                  'Player-%s join the game' % number,
                                  type='join')
                 )
        open_games.add(game_info['game-id'])
        if len(game_info['players-queue']) == 2:
            try:
                open_games.remove(game_info['game-id'])
            except KeyError:
                pass
    else:
        message.reply_channel. \
            send(populate_message('warning',
                                  'You connected as a spectator',
                                  type='spectator-connected',
                                  history=list(
                                      game.move_set.values(
                                          'id',
                                          'x',
                                          'y',
                                      )),
                                  )
                 )


    cache.set('open_games', open_games)

    cache.set("game-%s" % message.channel_session['room'], game_info, 3600)


# Connected to websocket.receive
@enforce_ordering(slight=True)
@channel_session
@channel_session_user_from_http
def ws_message(message):

    game_info = cache.get("game-%s" % message.channel_session['room'], {})

    game_id = game_info['game-id']
    game = models.Game.objects.get(id=game_id)
    if game.finished or game.aborted:
        return

    if len(game_info['players-queue']) < 2:
        Group("game-%s" % message.channel_session['room']). \
            send(populate_message('warning', 'Waiting for other player...'))
        return
    if game_info['players-queue'][0] != message.reply_channel.name:
        Group("game-%s" % message.channel_session['room']). \
            send(populate_message('warning', 'Wrong player'))
        return

    msg = json.loads(message['text'])
    field = TicTacFieldSerializer.restore(game_info['game-field'])
    players_queue = game_info['players-queue']
    players = game_info['players']

    x, y = int(msg['details']['x']), int(msg['details']['y'])
    if not field.get_cell(x, y):
        field.set_cell(x, y, players[message.reply_channel.name]['symbol'])
        models.Move.objects.create(
            game_id=game_id,
            x=x,
            y=y,
        )
        Group("game-%s" % message.channel_session['room']). \
            send(populate_message('game-action',
                                  '%s makes a move' % players[players_queue[0]]['name'],
                                  type='move',
                                  x=x,
                                  y=y,
                                  val=players[message.reply_channel.name]['symbol'],
                                  player=players[players_queue[0]]['name'])
                 )

        win_line = field.check_lines(x, y)
        if win_line:
            game.finished = True
            game.finished_time = timezone.now()
            game.finish_line = win_line
            game.save()
            Group("game-%s" % message.channel_session['room']).\
                send(populate_message('game-action',
                                      '%s win the game' % players[players_queue[0]]['name'],
                                      type='game-finish',
                                      winner=players[players_queue[0]]['name'],
                                      win_line=win_line,)
                     )

        players_queue.append(players_queue.pop(0))

    cache.set("game-%s" % message.channel_session['room'], game_info, 3600)


# Connected to websocket.disconnect
@enforce_ordering(slight=True)
@channel_session
@channel_session_user_from_http
def ws_disconnect(message):

    game_info = cache.get("game-%s" % message.channel_session['room'], {})

    players_queue = game_info['players-queue']
    players = game_info['players']
    if message.reply_channel.name in players:
        disconnected = players.pop(message.reply_channel.name)
        players_queue.remove(message.reply_channel.name)
        Group("game-%s" % message.channel_session['room']). \
            send(populate_message('game-action', '%s disconnected' % disconnected['name'], type='disconnect'))

        game_id = game_info['game-id']

        open_games = cache.get('open_games', set())
        try:
            open_games.remove(game_info['game-id'])
            open_games = cache.set('open_games', open_games)
        except KeyError:
            pass

        game = models.Game.objects.get(id=game_id)
        game.aborted = True
        game.save()
        Group("game-%s" % message.channel_session['room']). \
            send(populate_message('game-action',
                                  '%s win the game' % players[players_queue[0]]['name'],
                                  type='game-aborted',
                                  winner=players[players_queue[0]]['name']
                                  )
                 )

    cache.set("game-%s" % message.channel_session['room'], game_info, 3600)
