"""code to deal with Excel"""

import csv
import pandas as pd
import xlsxwriter


class excel_manipulation:
    def __init__(self, filename):
        self.filename = filename

    def xl_extract(self):
        """function to convert execl data to python list of dictionaries"""
        main_data = []
        list_of_addition = []
        list_of_subtraction = []
        list_of_multiplication = []
        list_of_division = []
        read_file = pd.read_excel(self.filename)
        read_file.to_csv("calc_excel.csv", index=None, header=True)

        with open('calc_excel.csv', mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                temp_dict = {'TestCaseID': row[0], 'TestFunction': row[1],
                             'TestInputs': row[2], 'ExpectedValue': row[3]}
                main_data.append(temp_dict)
                if 'Addition' in temp_dict['TestFunction']:
                    if 'None' in temp_dict['TestInputs']:
                        test_data = [temp_dict['TestInputs'], 0, temp_dict['ExpectedValue']]
                        list_of_addition.append(test_data)
                    else:
                        result = [x.strip() for x in temp_dict['TestInputs'].split(',')]
                        for i in range(len(result) - 1):
                            test_data = [int(result[0]), int(result[1]), int(temp_dict['ExpectedValue'])]
                            list_of_addition.append(test_data)
                if 'Subtraction' in temp_dict['TestFunction']:
                    if 'None' in temp_dict['TestInputs']:
                        test_data = [temp_dict['TestInputs'], 0, temp_dict['ExpectedValue']]
                        list_of_subtraction.append(test_data)
                    else:
                        result = [x.strip() for x in temp_dict['TestInputs'].split(',')]
                        for i in range(len(result) - 1):
                            test_data = [int(result[0]), int(result[1]), int(temp_dict['ExpectedValue'])]
                            list_of_subtraction.append(test_data)
                if 'Multiplication' in temp_dict['TestFunction']:
                    if 'None' in temp_dict['TestInputs']:
                        test_data = [temp_dict['TestInputs'], 0, temp_dict['ExpectedValue']]
                        list_of_multiplication.append(test_data)
                    else:
                        result = [x.strip() for x in temp_dict['TestInputs'].split(',')]
                        for i in range(len(result) - 1):
                            test_data = [int(result[0]), int(result[1]), int(temp_dict['ExpectedValue'])]
                            list_of_multiplication.append(test_data)
                if 'Division' in temp_dict['TestFunction']:
                    if 'None' in temp_dict['TestInputs']:
                        test_data = [temp_dict['TestInputs'], 0, temp_dict['ExpectedValue']]
                        list_of_division.append(test_data)
                    else:
                        result = [x.strip() for x in temp_dict['TestInputs'].split(',')]
                        for i in range(len(result) - 1):
                            test_data = [int(result[0]), int(result[1])]
                            if not temp_dict['ExpectedValue'].isalpha():
                                test_data.append(float(temp_dict['ExpectedValue']))
                            else:
                                test_data.append(temp_dict['ExpectedValue'])
                            list_of_division.append(test_data)
        return list_of_addition, list_of_subtraction, list_of_multiplication, list_of_division, main_data

    def write_excel(self, actual_and_result_dict, file_to_generate):
        """function to dump data in excel"""
        _, _, _, _, output_data = self.xl_extract()

        workbook = xlsxwriter.Workbook(file_to_generate)
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True})
        cf = workbook.add_format()
        cf2 = workbook.add_format()
        cf.set_font_color("red")
        cf2.set_font_color("green")

        sheet.write_row(0, 0, ['TestCaseID', 'TestFunction', 'TestInputs',
                               'ExpectedValue', 'ActualResult', 'TestResult'])

        row = 1
        for item in output_data:
            sheet.write(row, 0, item['TestCaseID'])
            sheet.write(row, 1, item['TestFunction'])
            sheet.write(row, 2, item['TestInputs'])
            sheet.write(row, 3, item['ExpectedValue'])
            row += 1

        row = 1
        for actual_result in actual_and_result_dict['ActualResult']:
            sheet.write(row, 4, actual_result)
            row += 1

        row = 1
        for test_result in actual_and_result_dict['TestResult']:
            sheet.write(row, 5, test_result)
            if test_result == 'Passed':
                sheet.write(row, 5, test_result, cf2)
            else:
                sheet.write(row, 5, test_result, cf)
            row += 1

        sheet.set_column('A:A', 10)
        sheet.set_column('B:F', 14)
        sheet.set_row(0, None, cell_format)
        workbook.close()

        print("Data exported successfully")
