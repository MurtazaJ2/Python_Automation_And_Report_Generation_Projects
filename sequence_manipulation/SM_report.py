import xlsxwriter
from input_parsing_SM import Manipulate

file = 'input excel SM.xlsx'
output_data = Manipulate(file)

workbook = xlsxwriter.Workbook('SM_excel_output.xlsx')
sheet = workbook.add_worksheet()
cell_format = workbook.add_format({'bold': True})

sheet.write_row(0, 0, ['Step Id', 'Sequence', 'Step input'])
row = 1

for item in output_data:
    sheet.write(row, 0, item['Step ID'])
    sheet.write(row, 1, item['Sequence'])
    sheet.write(row, 2, item['Step input'])
    row += 1

sheet.set_column('B:C', 13)
sheet.set_row(0, None, cell_format)
workbook.close()

print("Data exported successfully")