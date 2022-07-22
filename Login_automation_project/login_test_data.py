import pandas as pd
import csv
from login_automation import login

def Data_Extraction(filename):
    final_list = []
    credentials = []

    read_file = pd.read_excel(filename)
    read_file.to_csv("Testcases_excel.csv", index=None, header=True)
    csv_data = pd.DataFrame(pd.read_csv("Testcases_excel.csv"))
    csv_data.to_csv("Testcases_excel.csv")
    with open('Testcases_excel.csv', mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            temp_dict = {}
            temp_dict = {'Test case Id': '', 'Test Description': '',
                        'Step ID': '', 'Step input': '', 'Expected Output': ''}
            temp_dict['Test case Id'] = row[1]
            temp_dict['Test Description'] = row[2]
            temp_dict["Step ID"] = row[3]
            temp_dict['Step input'] = row[4]
            temp_dict['Expected Output'] = row[5]
            final_list.append(temp_dict)
        file.close()

    for dict in final_list:
        stepdata ={}
        stepdata = {'username': '', 'password': '', 'Actual Output': ''}
        input_data = dict['Step input']
        username_data = input_data.split(',')
        username = username_data[0]
        password = username_data[-1]
        username = username.split('-')
        stepdata['username'] = username[-1]
        password = password.split('-')
        stepdata['password'] = password[-1]
        stepdata['Actual Output'] = login(stepdata['username'], stepdata['password'])
        credentials.append(stepdata)

    return credentials, final_list

#if __name__ == "__main__":
#    file = "/home/softnautics/Desktop/Login_automation_project/login_page_testcases.xlsx"
#    data = Data_Extraction(file)