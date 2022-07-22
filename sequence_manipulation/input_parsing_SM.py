import pandas as pd
import csv
import random
import re

def Random_num():
    R = str(random.randint(1, 20))
    return R

def Manipulate(filename):
    main_data = []
    head_data = []
    tail_data = []
    tail_index = []
    temp = ''
    final_output = []
    read_file = pd.read_excel(filename)
    read_file.to_csv("SM_excel.csv", index=None, header=True)
    csv_data = pd.DataFrame(pd.read_csv("SM_excel.csv"))
    csv_data.to_csv("SM_excel.csv")
    with open('SM_excel.csv', mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            temp_dict = {}
            temp_dict = {'Step ID': '', 'Sequence': '', 'Step input': ''}
            temp_dict["Step ID"] = row[1]
            temp_dict['Sequence'] = row[2]
            temp_dict['Step input'] = row[3]
            main_data.append(temp_dict)
            if 'R' in temp_dict['Step input']:
                if ',' in temp_dict['Sequence']:
                    tail_regex = re.compile(r'\d\,(\d(\,?\d?)+)')
                    tail_search = tail_regex.search(temp_dict['Sequence'])
                    tail_group = tail_search.group(1)
                    tail = tail_group.split(',')
                    tail_data.append(tail)
                    for i in range(1, 6):
                        temp_dict2 = {}
                        temp_dict['Sequence'].split(',')
                        var = temp_dict['Sequence'][0]
                        temp = var
                        temp_dict['Step ID'] = f'{var}.{i}'
                        replaced = re.sub('R', Random_num(), temp_dict['Step input'])
                        temp_dict['Step input'] = replaced
                        temp_dict2.update(temp_dict)
                        head_data.append(temp_dict2)
        file.close()

    for value in tail:
        tail_value = int(value)-1
        tail_index.append(tail_value)

    add_data = main_data[:int(temp)-1]

    for data in head_data:
        final_output.append(data)
        for index in tail_index:
            final_output.append(main_data[index])

    final_output = add_data + final_output + main_data[tail_index[-1]+1:]
    return final_output