from selenium import webdriver
import time
import unittest
import xlsxwriter
import re
import random
from datetime import datetime

from Reading.src.pages.Browser import Browser
from Reading.src.pages.page import *
from Reading.src.pages.locators import *
from Reading.src.pages.locators import WithdrawLocators as wl
from Reading.src.pages.UIObject import UiObject
from Reading.src.pages.utils import *


class WithdrawBanksFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    def test_WithdrawBankFlow(self):
        self.now = ''
        self.no = 1
        self.workingPage = 'http://dev-ta.mooo.com/account/withdraw'
        self.range = [50, 1000000]
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'Recharge using Banks'

        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = BasePage(self.driver)  # Khai báo base page handler
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # DATA TEST
        TEST_DATA = [
            [1, 'Data validation', 'INVALID', wl.in_amount, wl.in_amount_error, 'Không nhập số tiền', '', 'Vui lòng nhập số tiền'],
            [2, 'Data validation', 'INVALID', wl.in_amount, wl.in_amount_error, 'Nhập tiền ít hơn 50K', '49', 'Số tiền nạp tối thiểu là 50 K'],
            [3, 'Data validation', 'VALID', wl.in_amount, wl.in_amount_error, 'Nhập tiền ít bằng 50K', '50', ''],
            [4, 'Data validation', 'INVALID', wl.in_amount, wl.in_amount_error, 'Nhập tiền nhiều hơn 1.000.000K', '1000001', 'Số tiền nạp tối đa là 1.000.000 K'],
            [5, 'Data validation', 'VALID', wl.in_amount, wl.in_amount_error, 'Nhập tiền bằng 1.000.000K', '1000000', ''],
            [6, 'Data validation', 'VALID-RAN', wl.in_amount, wl.in_amount_error, 'Nhập tiền lớn hơn 50k nhỏ hơn 1.000.000k', '[50,1000000]', ''],
            [7, 'Data validation', 'INVALID', wl.password, wl.password_error, 'Không nhập mật khẩu', '', 'Vui lòng nhập mật khẩu'],
            [8, 'Data validation', 'INVALID', wl.password, wl.password_error, 'Mật khẩu ít hơn 6 ký tự', 'abcde', 'Mật khẩu không hợp lệ, yêu cầu ít nhất 6 ký tự'],
            [9, 'Data validation', 'VALID', wl.password, wl.password_error, 'Mật khẩu = 6 ký tự', 'abcdef', ''],
            [10, 'Data validation', 'VALID', wl.password, wl.password_error, 'Mật khẩu nhiều hơn 12 ký tự ', 'abcdefghiyz1234', ''],
            [11, 'Data validation', 'VALID', wl.password, wl.password_error, 'Mật khẩu = 12 ký tự', 'abcdefghi123', ''],
            [12, 'Data validation', 'VALID-MULTI', wl.password, wl.password_error, 'Mật khẩu với ký tự đặc biệt', ['!@#$%^&*', '() ;:\'"', '`~>.<,{}', '[]\/-=+'], ''],
            [13, 'Show/Hide pw', 'SHOW', wl.password, [wl.show_pass, wl.hide_pass], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'text'],
            [14, 'Show/Hide pw', 'HIDE', wl.password, [wl.hide_pass, wl.show_pass], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'password'],
            [15, 'Helptext', 'TEXT', wl.in_amount, None, 'Nhập số tiền', '', 'Nhập số tiền'],
            [16, 'Helptext', 'TEXT', wl.password, None, 'Nhập mật khẩu', '', 'Nhập mật khẩu'],
            [17, 'Data validation', 'INVALID-P', [wl.in_amount, wl.password, [wl.TAO_PHIEU_RUT]], [wl.popup_error, wl.popup_error_content, wl.popup_error_btn_confirm], 'Mật khẩu không chính xác', ['1234', 'saimatkhau'], 'Mật khẩu không chính xác'],
        ]

        # RUNNING TEST
        isNewAccount = False
        if isNewAccount:
            if MainMenuLocators.MENU_DANG_KY.visible():
                MainMenuLocators.MENU_DANG_KY.click()
                self.driver.implicitly_wait(30)
                time.sleep(5)
                self.now = re.sub('[ :-]', '', str(datetime.now()).split('.')[0])
                account_test = 'tuananhle' + self.now
                SignupLocators.username.set_text('tuananhle' + self.now)
                SignupLocators.password.set_text('123456')
                SignupLocators.re_password.set_text('123456')
                SignupLocators.phoneno.set_text('0935770998')
                SignupLocators.btn_agree.click()
                SignupLocators.btn_register.click()
                time.sleep(2)
                if SignupLocators.popup_error.visible():
                    SignupLocators.popup_error_btn_confirm.click()
                    SignupLocators.btn_close.click()
                    if MainMenuLocators.MENU_DANG_NHAP.visible():
                        MainMenuLocators.MENU_DANG_NHAP.click()
                        account_test = 'tuananhle20210405110106'
                        LoginLocators.input_username.set_text(account_test)
                        LoginLocators.input_password.set_text('123456')
                        LoginLocators.btn_login.click()
                        time.sleep(2)
                self.TEST_DATA_HEADER.append(['Account Test', 'Username: ' + account_test + ', pass: 123456'])
        else:
            if MainMenuLocators.MENU_DANG_NHAP.visible():
                MainMenuLocators.MENU_DANG_NHAP.click()
                account_test = 'tuananhle20210405110106'
                LoginLocators.input_username.set_text(account_test)
                LoginLocators.input_password.set_text('123456')
                LoginLocators.btn_login.click()
                time.sleep(2)
            self.TEST_DATA_HEADER.append(['Account Test', 'Username: ' + account_test + ', pass: 123456'])
        if UserInfoLocator.drop_username.visible():
            base.set_url(self.workingPage)
            time.sleep(3)
            wl.tab_bank.click()
            wl.acc_selector.click()
            wl.acc_1.click()
            wl.in_amount.set_text('999999999')
            wl.password.set_text('999999999')
            wl.TAO_PHIEU_RUT.click()
            self.driver.implicitly_wait(30)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)

            for i in TEST_DATA:
                print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
                if wl.acc_selector.visible() == False:
                    base.set_url(self.workingPage)
                    time.sleep(3)
                    wl.tab_bank.click()
                    wl.acc_selector.click()
                    wl.acc_1.click()
                    wl.in_amount.set_text('999999999')
                    wl.password.set_text('999999999')
                    wl.TAO_PHIEU_RUT.click()
                    time.sleep(3)
                if i[1] == 'Data validation':
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                            self.TEST_RESULT = self.TEST_RESULT + ValidateData.CheckINVALIDCase(i, self.name, base)
                        else:
                            self.TEST_RESULT.append(ValidateData.CheckINVALIDCase(i, self.name, base))
                    elif 'VALID' in i[2]:
                        if i[2] == 'VALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                            self.TEST_RESULT = self.TEST_RESULT + ValidateData.CheckVALIDCase(i, self.name, base)
                        else:
                            if i[2] == 'VALID-RAN':
                                i[6] = str(random.randrange(self.range[0], self.range[1]))
                            self.TEST_RESULT.append(ValidateData.CheckVALIDCase(i, self.name, base))
                elif i[1] == 'Show/Hide pw':
                    self.TEST_RESULT.append(ValidateData.ShowHideButton(i, self.name, base))

                elif i[1] == 'Helptext':
                    self.TEST_RESULT.append(ValidateData.HelpTextCheck(i, self.name, base))

                elif i[1] == 'FUNC':
                    self.TEST_RESULT.append(ValidateData.CheckCOPYbutton(i, self.name, base))

                Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
                Template_Report.export()
                Template_Report.close()
                time.sleep(1)

            end = datetime.now()
            self.TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Time spend', str(end-start).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Size', str(SIZE)])
            # REPORT data
            report = Report(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            report.export()
            report.close()
        else:
            base.ScrShot('Test Checking url link: FAILED')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
