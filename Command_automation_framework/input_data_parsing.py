import pandas as pd
import csv
from Command_testing import command_testing
import logging


def input_parse(filename):
    logging.basicConfig(filename="newfile.log",
                        format='%(asctime)s %(levelname)s %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    final_list = []

    read_file = pd.read_excel(filename)
    logger.info("reading excel files")
    read_file.to_csv("Test_excel_1.csv", index=None, header=True)
    csv_data = pd.DataFrame(pd.read_csv("Test_excel_1.csv"))
    csv_data.to_csv("Test_excel_1.csv")
    logger.info("data converted to .csv file")

    with open('Test_excel_1.csv', mode='r') as fp:
        logger.info("opening .csv file in read mode")
        reader = csv.reader(fp)
        header = next(reader)
        for row in reader:
            temp_list = []
            temp_dict = {}
            temp_dict = {'test_case_Id': '', 'Test_title': '',
                        'Test_Description': '', 'stepdata': ''}
            test_case_Id = {}
            Test_title = {}
            Test_Description = {}
            test_case_Id['test_case_Id'] = row[1]
            Test_title['Test_title'] = row[2]
            Test_Description['Test_Description'] = row[3]
            temp_dict.update(test_case_Id)
            temp_dict.update(Test_title)
            temp_dict.update(Test_Description)
            stepdata = {}
            stepdata["stepId"] = row[4]
            stepdata['Step_Description'] = row[5]
            stepdata['commandString'] = row[6]
            stepdata['Expected_Output'] = row[7]
            stepdata['Actual_result'] = []
            temp_list.append(stepdata)
            temp_dict["stepdata"] = temp_list
            final_list.append(temp_dict)
    fp.close()

    for index, element in enumerate(final_list):
        if element["test_case_Id"] == '':
            final_list[index-1]['stepdata'] += element['stepdata']
            del final_list[index]
    return final_list


def iterate_test(test_data):
    step_list = test_data['stepdata']
    command_list = []
    for step in step_list:
        command_list.append(step['commandString'])
        command_string = '; '.join(command_list)
        final_command = command_testing.test_command(command_string)
    return final_command


def collect_data(final_data):
    for test in final_data:
        actual_result_data = iterate_test(test)
        for result in test['stepdata']:
            if result['Expected_Output'] == '':
                result['Actual_result'] = ''
            else:
                result['Actual_result'] = actual_result_data
            if result['Expected_Output'] == result['Actual_result']:
                result['test_result'] = "pass"
            else:
                result['test_result'] = "fail"
    return final_data