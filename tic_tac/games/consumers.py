from channels import Group
from channels.sessions import channel_session, enforce_ordering
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http


# Connected to websocket.connect
@enforce_ordering(slight=True)
@channel_session
@channel_session_user_from_http
def ws_connect(message):
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip("/")
    print(room)
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    g = Group("chat-%s" % room)
    g.history = []
    Group("chat-%s" % room).add(message.reply_channel)


# Connected to websocket.receive
@enforce_ordering(slight=True)
@channel_session
@channel_session_user_from_http
def ws_message(message):
    Group("chat-%s" % message.channel_session['room']).send({
        "text": message['text'],
    })


# Connected to websocket.disconnect
@enforce_ordering(slight=True)
@channel_session
@channel_session_user_from_http
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)
