(function () {
    var fieldBlock = $('#field');
    var gameInfo = fieldBlock[0].dataset;
    var field = new TicTacField(gameInfo.size, gameInfo.min_length);
    var logBlock = $('#log');

    fieldBlock.html(field.render());

    socket = new WebSocket("ws://" + window.location.hostname + ':8000' + window.location.pathname);
    socket.onmessage = function (e) {
        console.log(e.data);
        var data = JSON.parse(e.data);

        switch (data.action) {
            case 'game-action':
                logBlock.prepend('<p>' + data.details.message + '</p>');
                switch (data.details.type) {
                    case 'move':
                        field.setCellValue(data.details.x, data.details.y, data.details.val);
                        break;
                    case 'game-finish':
                        field.highlightLine(data.details.win_line, "#18c155");
                        logBlock.prepend('<p>Game over!</p>');
                        break;
                }
                break;
            case 'warning':
                switch (data.details.type) {
                    case 'spectator-connected':
                        alert(data.details.message);
                        break;
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

