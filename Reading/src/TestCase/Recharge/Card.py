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
from Reading.src.pages.locators import RechargeLocators as rl
from Reading.src.pages.UIObject import UiObject
from Reading.src.pages.utils import *


class RechargeCardsFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    def test_RechargeCardsFlow(self):
        self.now = ''
        self.no = 1
        self.workingPage = 'http://dev-ta.mooo.com/account/deposit'
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
            [1, 'Data validation', 'CLICKABLE', rl.in_series, rl.in_series_error, 'Không nhập số series', '', ''],
            [2, 'Data validation', 'VALID', rl.in_series, rl.in_series_error, 'Nhập số series', '123456789012345', ''],
            [3, 'Data validation', 'VALID', rl.in_series, rl.in_series_error, 'Nhập số series chỉ có số', '951357852645741', ''],
            [4, 'Data validation', 'VALID', rl.in_series, rl.in_series_error, 'Nhập số series toàn chữ', 'UYISDFKLJWTRMFD', ''],
            [5, 'Data validation', 'VALID', rl.in_series, rl.in_series_error, 'Nhập số series cả số và chữ', 'SLKFWP239505320', ''],
            [6, 'Data validation', 'CLICKABLE', rl.in_pin, rl.in_pin_error, 'Không nhập mã thẻ (PIN)', '', ''],
            [7, 'Data validation', 'VALID', rl.in_pin, rl.in_pin_error, 'Nhập mã thẻ (PIN)', '123456789012345', ''],
            [8, 'Data validation', 'VALID', rl.in_pin, rl.in_pin_error, 'Nhập mã thẻ (PIN) chỉ có số', '951357852645741', ''],
            [9, 'Data validation', 'VALID', rl.in_pin, rl.in_pin_error, 'Nhập mã thẻ (PIN) toàn chữ', 'UYISDFKLJWTRMFD', ''],
            [10, 'Data validation', 'VALID', rl.in_pin, rl.in_pin_error, 'Nhập mã thẻ (PIN) cả số và chữ', 'SLKFWP239505320', ''],
            [11, 'Data validation', 'CHECK-SELECTOR', [rl.data_listCardSupplier, rl.data_listCardAmount, rl.card_fee_percent, rl.card_Selector], [rl.amount_card_fee, rl.amount_card_real], 'Số tiền nhận được hiển thị phải được tính tương ứng với số tiền nhập và gói khuyến mãi', '', ''],
            [12, 'Helptext', 'TEXT', rl.in_pin, None, 'Nhập mã thẻ (PIN)', '', 'Nhập mã thẻ (PIN)'],
            [13, 'Helptext', 'TEXT', rl.in_series, None, 'Nhập số series', '', 'Nhập số series'],
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
            rl.first_100.click()
            rl.rc_card.click()
            time.sleep(1)
            rl.card_Selector.click()
            rl.viettel_card_amount_500k.click()
            rl.in_pin.set_text('123456789')
            rl.in_series.set_text('9781236465')
            # rl.in_code.set_text('CODE123456789')
            # rl.bank_TAO_PHIEU_NAP.click()
            self.driver.implicitly_wait(30)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            for i in TEST_DATA:
                print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
                if i[1] == 'Data validation':
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                        self.TEST_RESULT.append(ValidateData.CheckINVALIDCase(i, self.name, base))
                    elif 'VALID' in i[2]:
                        if i[2] == 'VALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                        if i[2] == 'VALID-RAN':
                            i[6] = str(random.randrange(self.range[0], self.range[1]))
                        self.TEST_RESULT.append(ValidateData.CheckVALIDCase(i, self.name, base))
                    elif 'CHECK' in i[2]:
                        if i[2] == 'CHECK-SELECTOR':
                            self.TEST_RESULT = self.TEST_RESULT + ValidateData.CheckInputCase(i, self.name, base)
                        else:
                            self.TEST_RESULT.append(ValidateData.CheckInputCase(i, self.name, base))
                    elif 'TIME' in i[2]:
                        self.TEST_RESULT.append(ValidateData.CheckTimeFinished(i, self.name, base))
                elif i[1] == 'Helptext':
                    self.TEST_RESULT.append(ValidateData.HelpTextCheck(i, self.name, base))

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
