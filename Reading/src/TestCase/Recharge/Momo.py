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


class RechargeMomoFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    def test_RechargeMomoFlow(self):
        self.now = ''
        self.no = 1
        self.workingPage = 'http://dev-ta.mooo.com/account/deposit'
        self.range = [50, 20000]
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'Recharge using Momo'

        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = BasePage(self.driver)  # Khai báo base page handler
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # DATA TEST
        TEST_DATA = [
            [1, 'Data validation', 'INVALID', rl.in_amount, rl.in_amount_error, 'Không nhập số tiền', '', 'Vui lòng nhập số tiền'],
            [2, 'Data validation', 'INVALID', rl.in_amount, rl.in_amount_error, 'Nhập tiền ít hơn 50K', '49', 'Số tiền nạp tối thiểu là 50 K'],
            [3, 'Data validation', 'VALID', rl.in_amount, rl.in_amount_error, 'Nhập tiền ít bằng 50K', '50', ''],
            [4, 'Data validation', 'INVALID', rl.in_amount, rl.in_amount_error, 'Nhập tiền nhiều hơn 20.000K', '20001', 'Số tiền nạp tối đa là 20.000 K'],
            [5, 'Data validation', 'VALID', rl.in_amount, rl.in_amount_error, 'Nhập tiền bằng 20.000K', '20000', ''],
            [6, 'Data validation', 'VALID-RAN', rl.in_amount, rl.in_amount_error, 'Nhập tiền lớn hơn 50k nhỏ hơn 20.000k', [50,20000], ''],
            [7, 'Data validation', 'INVALID', rl.in_amount, rl.in_amount_error, 'Nhập chữ ở ô số tiền', 'Numberofmoney', 'Vui lòng nhập số tiền'],
            [8, 'Data validation', 'CHECK-1-1', rl.in_amount, rl.out_amount, 'Số tiền hiển thị phải tương đương với số tiền nhập', [50,20000], '1208000'],
            [9, 'Data validation', 'INVALID', rl.in_name, rl.in_name_error, 'Không nhập tên người gửi', '', 'Vui lòng nhập họ & tên người gửi'],
            [10, 'Data validation', 'VALID', rl.in_name, rl.in_name_error, 'Nhập tên người gửi', 'Tuấn Anh @ 123', ''],
            [11, 'Data validation', 'INVALID', rl.in_code, rl.in_code_error, 'Không nhập mã giao dịch', '', 'Vui lòng nhập mã giao dịch'],
            [12, 'Data validation', 'VALID', rl.in_code, rl.in_code_error, 'Nhập mã giao dịch', 'CODE123456789', ''],
            [13, 'Copy', 'UI', [rl.momo_phoneNo_btn, rl.momo_owner_btn], [rl.momo_phoneNo_text, rl.momo_owner_text], 'Các nút COPY chuyển sang COPIED khi click và chuyển về COPY khi click nút COPY khác', '', ''],
            [14, 'Copy', 'FUNC', [rl.momo_phoneNo_btn, rl.momo_owner_btn], [rl.momo_phoneNo_text, rl.momo_owner_text], 'Nội dung được copy vào clipboard khi click COPY', '', ''],
            [15, 'Helptext', 'TEXT', rl.in_amount, None, 'Nhập số tiền', '', 'Nhập số tiền'],
            [16, 'Helptext', 'TEXT', rl.in_name, None, 'Nhập tên người gửi', '', 'Nhập tên người gửi'],
            [17, 'Helptext', 'TEXT', rl.in_code, None, 'Nhập mã giao dịch', '', 'Nhập mã giao dịch'],
            [18, 'Data validation', 'CHECK-1-N-100', [rl.in_amount, rl.promo_100], [rl.amount_promo, rl.amount_real, rl.amount_minbet], 'Số tiền nhận được hiển thị phải được tính tương ứng với số tiền nhập và gói khuyến mãi', [50, 20000], ''],
            [19, 'Data validation', 'CHECK-1-N-40', [rl.in_amount, rl.promo_40], [rl.amount_promo, rl.amount_real, rl.amount_minbet], 'Số tiền nhận được hiển thị phải được tính tương ứng với số tiền nhập và gói khuyến mãi', [50, 20000], ''],
            [20, 'Data validation', 'CHECK-1-N-125', [rl.in_amount, rl.promo_125], [rl.amount_promo, rl.amount_real, rl.amount_minbet], 'Số tiền nhận được hiển thị phải được tính tương ứng với số tiền nhập và gói khuyến mãi', [50, 20000], ''],
            [21, 'Data validation', 'TIME', rl.finished_date, rl.finished_date, 'Thời gian hoàn thành khuyến mãi', '', ''],
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
            time.sleep(1)
            rl.first_100.click()
            rl.rc_momo.click()
            time.sleep(1)
            rl.momo_Selector.click()
            rl.momo_account3.click()
            rl.in_amount.set_text('999999999')
            rl.in_name.set_text('LE TUAN ANH')
            rl.in_code.set_text('CODE123456789')
            rl.momo_TAO_PHIEU_NAP.click()
            self.driver.implicitly_wait(30)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)

            for i in TEST_DATA:
                print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
                if rl.bank_Selector.visible() == False:
                    base.set_url(self.workingPage)
                    if rl.first_100.visible():
                        rl.first_100.click()
                    rl.rc_bank.click()
                    time.sleep(1)
                    rl.bank_Selector.click()
                    rl.bank_Vietcombank.click()
                    rl.in_amount.set_text('999999999')
                    rl.in_name.set_text('LE TUAN ANH')
                    rl.in_code.set_text('CODE123456789')
                    rl.momo_TAO_PHIEU_NAP.click()
                    time.sleep(3)
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
                        self.TEST_RESULT.append(ValidateData.CheckInputCase(i, self.name, base))
                    elif 'TIME' in i[2]:
                        self.TEST_RESULT.append(ValidateData.CheckTimeFinished(i, self.name, base))
                elif i[1] == 'Show/Hide pw':
                    self.TEST_RESULT.append(ValidateData.ShowHideButton(i, self.name, base))

                elif i[1] == 'Helptext':
                    self.TEST_RESULT.append(ValidateData.HelpTextCheck(i, self.name, base))
                elif i[1] == 'Copy':
                    if i[2] == 'UI':
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
