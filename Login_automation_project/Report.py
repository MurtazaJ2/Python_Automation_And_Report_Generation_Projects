import xlsxwriter
from login_test_data import Data_Extraction

file = '/home/softnautics/Public/Murtaza/Login_automation_project/login_page_testcases.xlsx'
credintials, final_list = Data_Extraction(file)
workbook = xlsxwriter.Workbook('login_report.xlsx')
sheet = workbook.add_worksheet()
cell_format = workbook.add_format({'bold': True})
cf = workbook.add_format()
cf2 = workbook.add_format()
cf.set_font_color("red")
cf2.set_font_color("green")

sheet.write_row(0, 0, ['Test case Id', 'Test Description', 'Step Id', 'Step input', 'Expected Output', 'Actual Output'])
row = 1

for item in final_list:
    test_data = item
    sheet.write(row, 0, test_data['Test case Id'])
    sheet.write(row, 1, test_data['Test Description'])
    sheet.write(row, 2, test_data['Step ID'])
    sheet.write(row, 3, test_data['Step input'])
    sheet.write(row, 4, test_data['Expected Output'])
    row += 1

row = 1
for data in credintials:
    sheet.write(row, 5, data['Actual Output'])
    if data['Actual Output'] != 'Login successfull':
        sheet.write(row, 5, data['Actual Output'], cf)
    else: 
        sheet.write(row, 5, data['Actual Output'], cf2)
    row += 1
sheet.set_column('A:A', 11)
sheet.set_column('B:B', 40)
sheet.set_column('D:D', 40)
sheet.set_column('E:F', 13)
sheet.set_row(0, None, cell_format)
workbook.close()
print('data exported sucessfully')