import openpyxl as xl
from openpyxl.chart import BarChart, Reference

# Load a workbook and return a workbook object
wb = xl.load_workbook('transactions.xlsx')
# Access particular sheet in a workbook
sheet = wb['Sheet1']

print(f'\nProcessing {sheet} from \'{wb}\'... \n')

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)       # sheet['a1'] is another way to access a cell
    print(cell.value)
    correct_price = cell.value * 0.9
    correct_price_cell = sheet.cell(row, 4)
    correct_price_cell.value = correct_price



wb.save('transactions2.xlsx')
print('\nDone.\n')
