from datetime import datetime
import xlsxwriter
import os
import re
import json
import requests


class Report:
    def __init__(self, name, data, header):
        self.header = header
        self.name = name
        self.data = data
        now = str(datetime.now()).split('.')[0].replace(':', '_', -1)
        dir_folder = os.getcwd() + '\\Reading Test Results' + '\\' + name
        Create_dir(dir_folder)
        self.workbook = xlsxwriter.Workbook(dir_folder+'\\'+name+' ['+now+'].xlsx')
        self.worksheet = self.workbook.add_worksheet()

    def add_new_format(self, font_color, bg_color, bold=True, ilatic=False, Heading=False, border_color='black'):
        new_format = self.workbook.add_format()
        new_format.set_font_name('Cambria')
        new_format.set_font_color(font_color)
        new_format.set_bg_color(bg_color)
        new_format.set_border_color(border_color)
        if bold == True:
            new_format.set_bold()
        if ilatic == True:
            new_format.set_italic()
        if Heading == True:
            new_format.set_font_size(16)
        else:
            new_format.set_font_size(12)
        return new_format

    def close(self):
        self.workbook.close()

    def export(self, startrow=1):
        header_format = self.add_new_format('black', '#46bdc6')
        sub_header_format = self.add_new_format('black', '#78ecf5')
        failed_format = self.add_new_format('white', 'red')
        passed_format = self.add_new_format('white', 'green')
        na_format = self.add_new_format('white', 'gray')
        title_format = self.add_new_format('red', 'white', True, False, True)
        self.worksheet.write(0, 0, 'Result of '+self.name, title_format)

        for row_num in range(len(self.header)):
            for col_num in range(len(self.header[row_num])):
                cell_data = self.header[row_num][col_num]
                if col_num == 0:
                    self.worksheet.write(row_num+startrow, col_num, cell_data, header_format)
                else:
                    self.worksheet.write(row_num+startrow, col_num, cell_data)
        startrow = startrow + len(self.header) + 1

        f_row = False
        for row_num in range(len(self.data)):
            if 'PASSED' not in self.data[row_num] and 'FAILED' not in self.data[row_num]:
                if '' in self.data[row_num]:
                    f_row = True
            for col_num in range(len(self.data[row_num])):
                cell_data = self.data[row_num][col_num]
                if row_num == 0:
                    self.worksheet.write(row_num+startrow, col_num, cell_data, header_format)
                elif f_row == True:
                    self.worksheet.write(row_num+startrow, col_num, cell_data, sub_header_format)
                elif cell_data == 'PASSED':
                    self.worksheet.write(row_num+startrow, col_num, cell_data, passed_format)
                elif cell_data == 'N/A':
                    self.worksheet.write(row_num+startrow, col_num, cell_data, na_format)
                elif cell_data == 'FAILED':
                    self.worksheet.write(row_num+startrow, col_num, cell_data, failed_format)
                else:
                    self.worksheet.write(row_num+startrow, col_num, cell_data)
            f_row = False


class Report_temp(Report):
    def __init__(self, name, data, header):
        self.header = header
        self.name = name
        self.data = data
        dir_folder = os.getcwd() + '\\Reading Test Results' + '\\' + name
        Create_dir(dir_folder)
        self.workbook = xlsxwriter.Workbook(dir_folder+'\\'+name+' [TEMP].xlsx')
        self.worksheet = self.workbook.add_worksheet()


class Create_dir:
    def __init__(self, fpath):
        self.fpath = fpath
        list_Folder = fpath.split('\\')
        Folder = ''
        for i in range(len(list_Folder)):
            if i == 0:
                Folder = list_Folder[i]
            else:
                Folder = Folder + '\\'+list_Folder[i]
            try:
                os.stat(Folder)
            except Exception as e:
                os.mkdir(Folder)


class API:
    def __init__(self, domain, value=[]):
        self.domain = domain
        self.value = value
        apilink = domain
        if len(value) > 0:
            for i in range(len(value)):
                if i == 0:
                    apilink = apilink + '?'+value[i]['key'] + '='+value[i]['value']
                else:
                    apilink = apilink + '&'+value[i]['key'] + '='+value[i]['value']
        self.link = apilink

    def GET(self):
        text = requests.get(self.link).text
        return json.loads(text)
