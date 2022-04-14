from datetime import datetime
from Reading.src.pages.utils import Create_dir
from Reading.src.pages.Browser import Browser
import os
import time
import re
import random


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def ScrShot(self, filename, location=''):
        """
        :param filename: String, name of image that your want to take screen
        :param location: String, the Folder of image file that you want to locate after screen shot
        :return: None
        """
        try:
            dir_img = os.getcwd()
            if location == '':
                path = dir_img + '\\Reading Test Results\\img'
            else:
                path = dir_img + '\\Reading Test Results\\' + location + '\\img'
            Create_dir(path)
            file = path + '\\' + filename + '.png'
            print(file)
            self.driver.get_screenshot_as_file(file)
        except Exception as e:
            print('Error: ', e)

    def get_size(self):
        try:
            return self.driver.get_window_size()
        except Exception as e:
            print('Error: ', e)

    def set_size(self, width, height):
        try:
            return self.driver.set_window_size(width, height)
        except Exception as e:
            print('Error: ', e)

    def get_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            print('Error: ', e)

    def set_url(self, link):
        try:
            return self.driver.get(link)
        except Exception as e:
            print('Error: ', e)

    def window_handle(self, link):
        try:
            return self.driver.get(link)
        except Exception as e:
            print('Error: ', e)


class HomePage(BasePage):
    pass


class GameLobbyPage(BasePage):
    pass


class GameCasinoPage(BasePage):
    pass


class ValidateData:
    # CHECKING SHOW/HIDE PASSWORD icon working or NOT
    def ShowHideButton(data, name, driver):
        caseNo = str(data[0])
        text_input = 'SHOW PASS'
        sts = ''
        actual = ''
        notes = ''
        data[3].set_text(text_input)
        if data[4][0].visible():
            data[4][0].click()
        else:
            data[4][1].click()
            data[4][0].click()
        time.sleep(2)
        actual = data[3].get_attribute('type')
        if actual == data[7]:
            sts = 'PASSED'
        else:
            driver.ScrShot(caseNo+'_ The show password display wrong', name)
            sts = 'FAILED'
        notes = 'INPUT: ' + text_input + '\nType: ' + actual
        print('Status: \t', sts)
        print('Expected: \t', data[7])
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], text_input, data[7], actual, sts, notes]

    # CHECKING HELPTEXT
    def HelpTextCheck(data, name, driver):
        caseNo = str(data[0])
        actual = ''
        sts = ''
        notes = ''
        actual = data[3].get_attribute('placeholder')
        if actual == data[7]:
            sts = 'PASSED'
        else:
            sts = 'FAILED'
            driver.ScrShot(caseNo+'_ The show password display wrong', name)
        print('Status: \t', sts)
        print('Expected: \t', data[7])
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], '-', data[7], actual, sts, notes]

    # CHECKING INVALID CASE
    def CheckINVALIDCase(data, name, driver):
        caseNo = str(data[0])
        actual = ''
        sts = ''
        notes = ''
        listdata_return = []
        data_input = ''
        if data[2] == 'INVALID-MULTI':
            for c in range(len(data[6])):
                Number = caseNo+'-'+str(c+1)
                data_input = 'validdata'+data[6][c]
                data[3].set_text(data_input)
                time.sleep(1)
                if data[4].visible():
                    actual = data[4].get_text()
                    if actual == data[7]:
                        sts = 'PASSED'
                    else:
                        sts = 'FAILED'
                        notes = 'Hiển thị lỗi không chính xác'
                        driver.ScrShot(Number+'_Error text is wrong', name)
                else:
                    sts = 'FAILED'
                    notes = 'Không hiển thị lỗi khi nhập ' + \
                        data[6][c]
                    driver.ScrShot(Number+'_Error text is not display', name)
                print('Status: \t', sts)
                print('Expected: \t', data[7])
                print('Actual: \t', actual, '\n')
                listdata_return.append([Number, data[5], data_input, data_input, actual, sts, notes])
            return listdata_return
        elif '-P' in data[2]:
            for set in range(len(data[3])-2):
                data[3][set].set_text(data[6][set])
                data_input = data_input + data[6][set]
            for item in data[3][len(data[3])-1]:
                item.click()
                time.sleep(1)
            if data[4][0].visible():
                actual = data[4][1].get_text()
                if actual == data[7]:
                    sts = 'PASSED'
                else:
                    sts = 'FAILED'
                    notes = 'Hiển thị lỗi không chính xác'
                    driver.ScrShot(str(data[0])+'_Error popup is wrong', name)
                notes = '\nCONTENT: '+actual
                data[4][2].click()
            else:
                actual = '-'
                sts = 'FAILED'
                notes = 'Popup error không hiện'
                driver.ScrShot(str(data[0])+'_Error popup not display', name)

        else:
            data_input = data[6]
            data[3].set_text(data_input)
            time.sleep(1)
            if data[4].visible():
                actual = data[4].get_text()
                if actual == data[7]:
                    sts = 'PASSED'
                else:
                    sts = 'FAILED'
                    notes = 'Hiển thị lỗi không chính xác'
                    driver.ScrShot(caseNo+'_Error text is wrong', name)
            else:
                sts = 'FAILED'
                notes = 'Không hiển thị lỗi'
                driver.ScrShot(caseNo+'_Error text is not display', name)
        print('Status: \t', sts)
        print('Expected: \t', data[7])
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], data_input, data[7], actual, sts, notes]

    # CHECKING INVALID CASE
    def CheckVALIDCase(data, name, driver):
        caseNo = str(data[0])
        actual = ''
        sts = ''
        notes = ''
        data_input = ''
        listdata_return = []
        if data[2] == 'VALID-MULTI':
            for c in range(len(data[6])):
                Number = caseNo+'-'+str(c+1)
                data_input = str(data[6][c])
                print('\n', '-'*15, ' Case: ', data_input, ': ', data[5], ' ', 15*'-')
                data[3].set_text(data_input)
                time.sleep(1)
                if data[4].visible():
                    actual = data[4].get_text()
                    sts = 'FAILED'
                    notes = 'Hiển thị lỗi khi nhập tên'
                    driver.ScrShot(Number+' Hiển thị lỗi khi nhập tên', name)
                else:
                    sts = 'PASSED'
                print('Status: \t', sts)
                print('Expected: \t', data[7])
                print('Actual: \t', actual, '\n')
                listdata_return.append([Number, data[5], data_input, data_input, actual, sts, notes])
        else:
            data[3].set_text(data[6])
            time.sleep(1)
            if data[4].visible():
                actual = data[4].get_text()
                sts = 'FAILED'
                notes = 'Hiển thị lỗi khi nhập đúng'
                driver.ScrShot(caseNo+'_Error text is display', name)
            else:
                sts = 'PASSED'
        print('Status: \t', sts)
        print('Expected: \t', data[7])
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], data_input, data[7], actual, sts, notes]

    # CHECK INPUT CALCULATED
    def CheckInputCase(data, name, driver):
        caseNo = str(data[0])
        actual = ''
        expected = ''
        sts = 'PASSED'
        notes = ''
        data_input = ''
        expected = ''
        list_data_return = []
        if data[2] == 'CHECK-1-1':
            data_input = str(random.randrange(data[6][0], data[6][1]))
            data[3].set_text(data_input)
            try:
                actual = re.sub('[=.VNĐD ]', '', str(data[4].get_text()))
            except Exception:
                actual = ''
            expected = data_input+'000'
            if expected == actual:
                sts = 'PASSED'
            else:
                sts = 'FAILED'
                notes = 'Text: ' + re.sub('[=]', '', str(data[4].get_text()))
                driver.ScrShot(caseNo+'_ Số tiền hiển thị không chính xác', name)
        elif 'CHECK-1-N' in data[2]:
            data_input = random.randrange(data[6][0], data[6][1])
            data[3][0].set_text(str(data_input))
            data[3][1].click()

            method_agrument = ['number of roll', '%km']
            if data[2] == 'CHECK-1-N-100':
                method_agrument = [20, 100]
            elif data[2] == 'CHECK-1-N-40':
                method_agrument = [14, 40]
            elif data[2] == 'CHECK-1-N-125':
                method_agrument = [0, 0]
            promo_amount = int(data_input*method_agrument[1]*1000/100)
            real_amount = int(data_input*(100+method_agrument[1])*1000/100)
            min_amount = int(real_amount*method_agrument[0])
            promo_amount = str(promo_amount)
            real_amount = str(real_amount)
            min_amount = str(min_amount)
            try:
                actual_promo = re.sub('[=.VNĐD ]', '', str(data[4][0].get_text()))
            except Exception:
                actual_promo = ''
            try:
                actual_real = re.sub('[=.VNĐD ]', '', str(data[4][1].get_text()))
            except Exception:
                actual_real = ''
            try:
                actual_min = re.sub('[=.VNĐD ]', '', str(data[4][2].get_text()))
            except Exception:
                actual_min = ''

            if promo_amount != actual_promo:
                sts = 'FAILED'
                notes = 'Promo FAILED: ' + re.sub('[=]', '', str(data[4][0].get_text()))
                driver.ScrShot(caseNo+'_ Số tiền khuyến mãi không chính xác', name)
            if real_amount != actual_real:
                sts = 'FAILED'
                notes = 'Promo FAILED: ' + re.sub('[=]', '', str(data[4][0].get_text()))
                driver.ScrShot(caseNo+'_ Số tiền thực nhận không chính xác', name)
            if min_amount != actual_min:
                sts = 'FAILED'
                notes = 'Promo FAILED: ' + re.sub('[=]', '', str(data[4][0].get_text()))
                driver.ScrShot(caseNo+'_ Tổng cực tối thiểu không chính xác', name)
            expected = promo_amount + ',\t'+real_amount+',\t'+min_amount
            actual = actual_promo + ',\t'+actual_real+',\t'+actual_min
        elif data[2] == 'CHECK-SELECTOR':
            list_data_return.append([caseNo, data[5], '', '', '', '', ''])
            for suplier in data[3][0]:
                data[3][0][suplier].click()
                list_data_return.append(['Case: ' + suplier, '', '', '', '', '', ''])
                for amount in data[3][1][suplier]:
                    if amount == '1000k' and (suplier == 'vinaphone' or suplier == 'mobifone'):
                        pass
                    else:
                        data[3][3].click()
                        data[3][1][suplier][amount][0].click()
                        _fee = int(data[3][1][suplier][amount][1]*data[3][2][suplier]/100)
                        _real = int(data[3][1][suplier][amount][1]-_fee)
                        _fee = str(_fee)
                        _real = str(_real)
                        time.sleep(1)
                        expected = 'Fee:\t'+_fee + '\tReal:\t' + _real
                        try:
                            actual_fee = re.sub('[=.VNĐD ]', '', str(data[4][0].get_text()))
                        except Exception:
                            actual_fee = ''
                        try:
                            actual_real = re.sub('[=.VNĐD ]', '', str(data[4][1].get_text()))
                        except Exception:
                            actual_real = ''
                        if _fee != actual_fee:
                            sts = 'FAILED'
                            notes = 'Fee amount FAILED: ' + re.sub('[=]', '', str(data[4][0].get_text()))
                            driver.ScrShot(caseNo+'-'+amount+'_ Số tiền phí không chính xác', name)
                        if _real != actual_real:
                            sts = 'FAILED'
                            notes = 'Promo FAILED: ' + re.sub('[=]', '', str(data[4][0].get_text()))
                            driver.ScrShot(caseNo+'-'+amount+'_ Số tiền thực nhận không chính xác', name)
                        actual = 'Fee:\t'+actual_fee + '\tReal:\t' + actual_real
                        print('Status: \t', sts)
                        print('Expected: \t', expected)
                        print('Actual: \t', actual, '\n')
                        list_data_return.append([caseNo+'-'+amount, 'Loại thẻ: '+amount, data_input, expected, actual, sts, notes])
            return list_data_return

        elif data[2] == 'CHECK-LINK-PAYWIN':
            window_before = driver.driver.window_handles[0]
            data[3][0].set_text('456')
            data[3][1].click()
            time.sleep(3)
            window_after = driver.driver.window_handles[1]
            driver.driver.switch_to_window(window_after)
            if data[4].visible():
                sts = 'PASSED'
            else:
                sts = 'FAILED'
                notes = 'Page not load'
                driver.ScrShot(caseNo+'_ '+notes, name)
            driver.driver.close()
            driver.driver.switch_to_window(window_before)
        print('Status: \t', sts)
        print('Expected: \t', expected)
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], data_input, expected, actual, sts, notes]

    # COPY ACTION
    def CheckCOPYbutton(data, name, driver):
        caseNo = str(data[0])
        actual = ''
        sts = 'PASSED'
        notes = ''
        data_input = ''
        for i in data[3]:
            if i.get_text().upper() == 'ĐÃ COPY':
                sts = 'FAILED'
                driver.ScrShot(caseNo+'_DEFAULT '+str(i), name)
        for i in range(len(data[3])):
            data[3][i].click()
            temp_text = [x for x in data[4]]
            temp_text.pop(i)
            if data[4][i].get_text().upper() != 'ĐÃ COPY':
                sts = 'FAILED'
                driver.ScrShot(caseNo+'_CLICKED'+str(i), name)
            for j in temp_text:
                actual = j.get_text().upper()

                if actual != 'COPY':
                    sts = 'FAILED'
                    driver.ScrShot(caseNo+'_ NOT CLICKED ITEM :\''+actual+'\'', name)
        print('Status: \t', sts)
        print('Expected: \t', data[7])
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], data_input, '', actual, sts, notes]

    # TIME CHECKING
    def CheckTimeFinished(data, name, driver):
        caseNo = str(data[0])
        actual = ''
        sts = ''
        notes = ''
        data_input = ''
        text = data[4].get_text()
        actual = re.sub('[/ .)()]', '', text.split(' ')[len(text.split(' '))-1])
        today = datetime.fromordinal(datetime.now().toordinal()+30)
        if today.day > 9:
            day = str(today.day)
        else:
            day = '0'+str(today.day)
        if today.month > 9:
            month = str(today.month)
        else:
            month = '0'+str(today.month)
        expected = day+month+str(today.year)
        if expected == actual:
            sts = 'PASSED'
        else:
            sts = 'FAILED'
            notes = 'Text: ' + text
            driver.ScrShot(caseNo+'_ Ngày hoàn thành hiển thị không chính xác', name)
        print('Status: \t', sts)
        print('Expected: \t', expected)
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], data_input, expected, actual, sts, notes]

    # CHECK BUTTON AVAILABLE TO CLICK OR NOT
    def CheckButtonClickAble(data, name, driver):
        caseNo = str(data[0])
        actual = ''
        expected = ''
        sts = ''
        notes = ''
        data_input = ''
        data[3].set_text('')

        if expected == actual:
            sts = 'PASSED'
        else:
            sts = 'FAILED'
            notes = 'Text: ' + text
            driver.ScrShot(caseNo+'_ Ngày hoàn thành hiển thị không chính xác', name)
        print('Status: \t', sts)
        print('Expected: \t', expected)
        print('Actual: \t', actual, '\n')
        return [caseNo, data[5], data_input, expected, actual, sts, notes]
