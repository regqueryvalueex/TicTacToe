(function () {

    function Field(size, min_length) {
        this.size = size || 3;
        this.min_length = min_length || 3;
        this.field = new Array(self.size);

        for (var i=0; i<this.size; i++){
            this.field[i] = new Array(this.size);
        }

        this.getCell = function(x, y){
            return this.field[x][y];
        };

        this.setCell = function (x, y, val) {
            if (this.getCell(x, y)){
                return false;
            }
            this.field[x][y] = val;
            $('[data-x=' + x + '][data-y=' + y + ']').text(val);
            return true;
        };

        this.render = function(){
            var html = '';
            for (var y = 0; y < this.size; y++) {
                html += "<div data-content='row'>";
                for (var x = 0; x < this.size; x++) {
                    html += "<div data-content='cell' data-x='" + x + "' data-y='" + y + "'>&nbsp;</div>";
                }
                html += "</div>";
            }
            return html;
        }
    }


window.TicTacField = Field;
})();

