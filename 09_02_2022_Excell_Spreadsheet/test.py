# import cell
# import spreadsheet
#
#
# class Test:
#     def test_set_cell_at(self):
#         test_spreadsheet = spreadsheet.Spreadsheet(2, 3)
#         if len(test_spreadsheet.cells) == 2 and len(test_spreadsheet.cells[0]) == 3:
#             print("Test set cell at successfully passed")
#         else:
#             print("Test set cell at failed")
#
#     def test_get_cell_at(self):
#         test_spreadsheet = spreadsheet.Spreadsheet(2, 3)
#         if isinstance(test_spreadsheet.get_cell_at(1, 2), cell.Cell):
#             print("Test set cell at successfully passed")
#         else:
#             print("Test set cell at failed")
#
#     def test_add_row(self):
#         test_spreadsheet = spreadsheet.Spreadsheet(2, 3)
#         initial_rows = len(test_spreadsheet.cells)
#         test_spreadsheet.add_row(1)
#         if initial_rows == len(test_spreadsheet.cells) - 1:
#             print("Test set cell at successfully passed")
#         else:
#             print("Test set cell at failed")
#
#     def test_add_column(self):
#         test_spreadsheet = spreadsheet.Spreadsheet(2, 3)
#         initial_columns = len(test_spreadsheet.cells[0])
#         test_spreadsheet.add_column(1)
#         if initial_columns == len(test_spreadsheet.cells[0]) - 1:
#             print("Test set cell at successfully passed")
#         else:
#             print("Test set cell at failed")
#
#
#
# test = Test()
# test.test_set_cell_at()
# test.test_get_cell_at()
# test.test_add_row()
# test.test_add_column()
