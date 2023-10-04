import openpyxl

file = "Agosto.xlsx"

wb = openpyxl.load_workbook(file)

sheet_obj = wb.active

cell_obj = sheet_obj.cell(row = 1, column = 1)
print(cell_obj.value)