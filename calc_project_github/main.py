"""read write excel"""

from test_calc.test_calculator import TestCalcMethods
from read_write_excel import xlsx_read_write

actual_and_result_dict = {'TestResult': [], 'ActualResult': []}
excel_read = xlsx_read_write.excel_manipulation("/home/murtaza/training_github/Training_Murtaza_jambughoda/"
                                                "Calculator_unittesting/unit_testing_exercise.xls")
Addition_list, Subtraction_list, Multiplication_list, Division_list, _ = excel_read.xl_extract()

for item in Addition_list:
    bool_value, result = TestCalcMethods.test_addition_two_integers(_, item[0], item[1], item[2])
    actual_and_result_dict['ActualResult'].append(result)
    if bool_value is True:
        actual_and_result_dict['TestResult'].append("Passed")
    else:
        actual_and_result_dict['TestResult'].append("Failed")

for item in Subtraction_list:
    bool_value, result = TestCalcMethods.test_subtraction_two_integers(_, item[0], item[1], item[2])
    actual_and_result_dict['ActualResult'].append(result)
    if bool_value is True:
        actual_and_result_dict['TestResult'].append("Passed")
    else:
        actual_and_result_dict['TestResult'].append("Failed")

for item in Multiplication_list:
    bool_value, result = TestCalcMethods.test_multiplication_two_integers(_, item[0], item[1], item[2])
    actual_and_result_dict['ActualResult'].append(result)
    if bool_value is True:
        actual_and_result_dict['TestResult'].append("Passed")
    else:
        actual_and_result_dict['TestResult'].append("Failed")

for item in Division_list:
    bool_value, result = TestCalcMethods.test_division_two_integers(_, item[0], item[1], item[2])
    actual_and_result_dict['ActualResult'].append(result)
    if bool_value is True:
        actual_and_result_dict['TestResult'].append("Passed")
    else:
        actual_and_result_dict['TestResult'].append("Failed")

excel_read.write_excel(actual_and_result_dict, "excel_output1.xlsx")
