(function () {
    var fieldBlock = $('#field');
    var gameInfo = fieldBlock[0].dataset;
    var field = new TicTacField(gameInfo.size, gameInfo.min_length);
    var logBlock = $('#log');

    fieldBlock.html(field.render());

    socket = new WebSocket("ws://" + window.location.host + window.location.pathname);
    socket.onmessage = function (e) {
        console.log(e.data);
        var data = JSON.parse(e.data);
        if(data.action == 'game-action'){
            logBlock.prepend('<p>' + data.details.message + '</p>');
            if (data.details.type == 'move'){
                field.setCell(data.details.x, data.details.y, data.details.val);
            }
            if (data.details.type == 'move') {
                field.setCell(data.details.x, data.details.y, data.details.val);
            }
        }

    };
    socket.onopen = function () {
        // socket.send("hello world");
    };

    fieldBlock.on('click', '[data-content="cell"]', function(e){
        if(socket.readyState != socket.OPEN){
            return;
        }
        var data = {
            x: this.dataset.x,
            y: this.dataset.y
        };
        socket.send(JSON.stringify({'details': data}));
    });

})();

