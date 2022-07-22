"""testing the functions of xl_format"""

from excel_formatting import xl_format

# set_width function
a = xl_format.excel_format('try_width.xlsx', 'Sheet1')
data_dict = {'A': 20, 'B': 30, 'C': 40, 'D': 10, 'E': 30}
a.set_width(data_dict)

# set_height function
data_dict = {'0': 20, '1': 30, '2': 50, '3': 100, '4': 150}
a.set_height(data_dict)

# wordwrap function
data_list = ['A', 'B', 'C', 'D']
a.wordwrap(data_list)

# set_url function
url_string = ['ranveer', 'rohan', 'rohit']
url_prefix = 'https://localhost:8080/job/'
a.set_url(url_prefix, jobname=url_string, postfix='justfortesting', startrow=1, start_col=0)

# close_book function
a.close_book()
