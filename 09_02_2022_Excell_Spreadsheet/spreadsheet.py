import cell


class Spreadsheet:
    def __init__(self, rows=0, column=0):
        if isinstance(rows, int) and isinstance(column, int) and rows >= 0 and column >= 0:
            self.cells = [[cell.Cell() for column in range(column)] for rows in range(rows)]
        else:
            raise Exception("Wrong input")

    def set_cell_at(self, row, column, value):
        if row >= 0 and column >= 0 and isinstance(row, int) and isinstance(column, int):
            self.cells[row][column].value = value
        else:
            raise Exception("No rows or columns found in the matrix.")

    def get_cell_at(self, row, column):
        return self.cells[row][column]

    def add_row(self, position):
        if 0 <= position <= len(self.cells):
            self.cells = self.cells[:position] + [[cell.Cell()] * len(self.cells[0])] + self.cells[position:]
        else:
            raise Exception("No rows found in the matrix.")

    def add_column(self, position):
        if 0 <= position <= len(self.cells[0]):
            for i in range(len(self.cells)):
                self.cells[i].insert(position, cell.Cell())
        else:
            raise Exception("No columns found in the matrix.")

    def swap_rows(self, row1, row2):
        self.cells[row1], self.cells[row2] = self.cells[row2], self.cells[row2]

    def swap_columns(self, column1, column2):
        for row in self.cells:
            row[column1], row[column2] = row[column2], row[column1]

    def remove_row(self, row):
        if 0 <= row < len(self.cells):
            del self.cells[row]
        else:
            raise Exception("No rows found in the matrix.")

    def remove_column(self, column):
        if 0 <= column < len(self.cells[0]):
            self.cells = [row[:column] + row[column + 1:] for row in self.cells]
        else:
            raise Exception("No columns found in the matrix.")

    def print(self):
        for row in self.cells:
            for value in row:
                print(value, value.value, end=" ")
            print()


spreadsheet1 = Spreadsheet(2,2)
spreadsheet1.set_cell_at(0, 0, 3)
spreadsheet1.set_cell_at(0, 1, 2)

print(spreadsheet1.get_cell_at(0,1).to_double())
spreadsheet1.add_column(1)
print(spreadsheet1.get_cell_at(1, 1).value)
spreadsheet1.print()
