import pandas as pd


class excel_format:
    def __init__(self, file, sheetname):
        self.file = file
        self.sheetname = sheetname
        dataframe = pd.read_excel(self.file)
        writer = pd.ExcelWriter(self.file, engine='xlsxwriter')
        dataframe.to_excel(writer, sheet_name=sheetname, index=False)
        self.workbook = writer.book
        self.sheet = writer.sheets[sheetname]

    def close_book(self):
        self.workbook.close()

    def set_width(self, data_dict):
        for key in data_dict:
            self.sheet.set_column(f'{key}:{key}', data_dict[key])

    def set_height(self, data_dict):
        for key in data_dict:
            self.sheet.set_row(int(key), data_dict[key])

    def wordwrap(self, column_list):
        wordwrap_format = self.workbook.add_format({'text_wrap': True})
        for column in column_list:
            self.sheet.set_column(f'{column}:{column}', None, wordwrap_format)

    def set_url(self, prefix, jobname=None, postfix='', start_col=None, startrow=None):
        url_format = self.workbook.add_format({
            'font_color': 'blue',
            'underline': 1
        })
        row = startrow
        for name in jobname:
            self.sheet.write_url(row, start_col, prefix + name + '/' + postfix, url_format, string=name)
            row += 1
