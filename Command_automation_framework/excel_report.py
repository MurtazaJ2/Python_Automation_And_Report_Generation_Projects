from input_data_parsing import collect_data, input_parse
import xlsxwriter
import os


def Process(xlsxfile, outfile):
    try:
        content = input_parse(xlsxfile)
        dict_list = collect_data(content)
    except NotImplementedError:
        exit()

    workbook = xlsxwriter.Workbook(os.path.join('/home/softnautics/Public/Murtaza/Command_automation_framework/output_folder', outfile))
    sheet = workbook.add_worksheet()
    cell_format = workbook.add_format({'bold': True})
    cf = workbook.add_format()
    cf2 = workbook.add_format()
    cf.set_font_color("red")
    cf2.set_font_color("green")

    sheet.write_row(0, 0, ['Testcase Id', 'Test title', 'Test Description', 'step Id',
                    'Step Description', 'Step input', 'Expected Output', 'Actual result', 'Test result'])
    row = 1

    for item in dict_list:
        test_data = item.copy()
        test_data['stepdata'] = {}
        step_data = item['stepdata'].copy()
        sheet.write(row, 0, test_data['test_case_Id'])
        sheet.write(row, 1, test_data['Test_title'])
        sheet.write(row, 2, test_data['Test_Description'])
        for step in step_data:
            sheet.write(row, 3, step['stepId'])
            sheet.write(row, 4, step['Step_Description'])
            sheet.write(row, 5, step['commandString'])
            sheet.write(row, 6, step['Expected_Output'])
            sheet.write(row, 7, step['Actual_result'])
            sheet.write(row, 8, step['test_result'])
            if step['test_result'] == 'fail':
                sheet.write(row, 8, step['test_result'], cf)
            else: 
                sheet.write(row, 8, step['test_result'], cf2)
            row += 1

    sheet.set_column('B:C', 40)
    sheet.set_column('E:H', 45)
    sheet.set_row(0, None, cell_format)
    workbook.close()
    return "Data exported successfully"


if __name__ == "__main__":
    files = os.listdir('/home/softnautics/Public/Murtaza/Command_automation_framework/Command_input')
    path = '/home/softnautics/Public/Murtaza/Command_automation_framework/Command_input'
    for file in files:
        if file.endswith('.xlsx'):
            path_of_file = os.path.join(path, file)
            output_filename = file.replace('.xlsx','_output.xlsx')
            data = Process(path_of_file, output_filename)
            print(data)
        else:
            print("didn't got the .xlsx file")