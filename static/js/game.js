(function () {
    var fieldBlock = $('#field');
    var gameInfo = fieldBlock[0].dataset;
    var field = new TicTacField(gameInfo.size, gameInfo.min_length);

    fieldBlock.html(field.render());

    socket = new WebSocket("ws://" + window.location.host + window.location.pathname);
    socket.onmessage = function (e) {
        console.log(e.data);
    };
    socket.onopen = function () {
        socket.send("hello world");
    }
})();

