# ! -*- coding: utf-8 -*-


class TicTacField(object):
    horizontal_walker = lambda self, x, y: (x + 1, y)
    vertical_walker = lambda self, x, y: (x, y + 1)
    right_diagonal_walker = lambda self, x, y: (x + 1, y + 1)
    left_diagonal_walker = lambda self, x, y: (x + 1, y - 1)

    def __init__(self, size, min_length, allow_horizontal, allow_vertical, allow_diagonal):
        self._size = size
        self._min_length = min_length
        self._allow_horizontal = allow_horizontal
        self._allow_vertical = allow_vertical
        self._allow_diagonal = allow_diagonal
        self._field = [[None] * self._size for x in range(self._size)]

    def get_cell(self, x, y):
        return self._field[x][y]

    def set_cell(self, x, y, val):
        self._field[x][y] = val

    def check_lines(self, x, y):
        return False

    def get_line(self, x, y, walker):
        line = []
        for i in range(self._min_length):
            print(x, y)
            line.append(self.get_cell(x, y))
            x, y = walker(x, y)
        return line

    def line_generator(self, x, y):
        length = self._min_length - 1
        x_left = max(x - length, 0)
        y_bottom = max(y - length, 0)
        y_top = min(y + length, self._size - 1)

        if self._allow_horizontal:
            x_start = x_left
            while x_start + length < self._size:
                yield self.get_line(x_start, y, self.horizontal_walker)
                x_start += 1
        if self._allow_vertical:
            y_start = y_bottom
            while y_start + length < self._size:
                yield self.get_line(x, y_start, self.vertical_walker)
                y_start += 1
        if self._allow_diagonal:
            y_start = y_bottom
            x_start = x_left
            while y_start + length < self._size and x_start + length < self._size:
                yield self.get_line(x_start, y_start, self.right_diagonal_walker)
                x_start += 1
                y_start += 1
            y_start = y_top
            x_start = x_left
            while y_start - length >= 0 and x_start + length < self._size:
                yield self.get_line(x_start, y_start, self.left_diagonal_walker)
                x_start += 1
                y_start -= 1


f = TicTacField(3, 3, True, True, True)
f._field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(f.line_generator(0, 1)))
