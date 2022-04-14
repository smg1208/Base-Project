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


class WithdrawCardsFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    def test_WithdrawCardsFlow(self):
        self.now = ''
        self.no = 1
        self.workingPage = 'http://dev-ta.mooo.com/account/withdraw'
        self.range = [50, 1000000]
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'Recharge using Card'

        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = BasePage(self.driver)  # Khai báo base page handler
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # DATA TEST
        TEST_DATA = [
            [1, 'Helptext', 'TEXT', wl.card_password, None, 'Nhập mật khẩu', '', 'Nhập mật khẩu'],
            [2, 'Show/Hide pw', 'SHOW', wl.card_password, [wl.card_show_pass, wl.card_hide_pass], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'text'],
            [3, 'Show/Hide pw', 'HIDE', wl.card_password, [wl.card_hide_pass, wl.card_show_pass], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'password'],
            [4, 'Data validation', 'INVALID-P', [wl.No_ofCard, wl.card_password, [wl.DOI_THE_CAO]], [wl.popup_error, wl.popup_error_content, wl.popup_error_btn_confirm], 'Số tiền trong tài khoản không đủ', ['1234', '123456'], 'Số tiền trong tài khoản không đủ'],
            [5, 'Data validation', 'INVALID-P', [wl.No_ofCard, wl.card_password, [wl.DOI_THE_CAO]], [wl.popup_error, wl.popup_error_content, wl.popup_error_btn_confirm], 'Mật khẩu không chính xác', ['0', 'Saimatkhau'], 'Mật khẩu không chính xác'],
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
            wl.tab_card.click()
            time.sleep(1)
            wl.card_Selector.click()
            wl.viettel_card_amount_50k.click()
            self.driver.implicitly_wait(30)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            for i in TEST_DATA:
                print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
                if i[1] == 'Data validation':
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                            self.TEST_RESULT = self.TEST_RESULT+ValidateData.CheckINVALIDCase(i, self.name, base)
                        elif '-P' in i[2]:
                            MainNo = i[0]
                            for suplier in wl.data_listCardSupplier:
                                wl.data_listCardSupplier[suplier].click()
                                self.TEST_RESULT.append([suplier, '', '', '', '', '', ''])
                                for amount in wl.data_listCardAmount[suplier]:
                                    wl.card_Selector.click()
                                    time.sleep(1)
                                    wl.data_listCardAmount[suplier][amount][0].click()
                                    i[0] = str(MainNo) + ' - ' + amount
                                    self.TEST_RESULT.append(ValidateData.CheckINVALIDCase(i, self.name, base))
                        else:
                            self.TEST_RESULT.append(ValidateData.CheckINVALIDCase(i, self.name, base))
                    elif 'VALID' in i[2]:
                        if i[2] == 'VALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                            self.TEST_RESULT = self.TEST_RESULT+ValidateData.CheckVALIDCase(i, self.name, base)
                        else:
                            if i[2] == 'VALID-RAN':
                                i[6] = str(random.randrange(self.range[0], self.range[1]))
                            self.TEST_RESULT.append(ValidateData.CheckVALIDCase(i, self.name, base))
                elif i[1] == 'Helptext':
                    self.TEST_RESULT.append(ValidateData.HelpTextCheck(i, self.name, base))
                elif i[1] == 'Show/Hide pw':
                    self.TEST_RESULT.append(ValidateData.ShowHideButton(i, self.name, base))

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
