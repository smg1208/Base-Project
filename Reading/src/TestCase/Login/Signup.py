# from Reading.src.pages.locators import SignupLocators, MainMenuLocators
import re
import time
import unittest
from datetime import datetime

import Reading.src.pages.page as page
import xlsxwriter
from Reading.src.pages.Browser import Browser
from Reading.src.pages.locators import *
from Reading.src.pages.locators import SignupLocators as sl
from Reading.src.pages.UIObject import UiObject
from Reading.src.pages.utils import *
from selenium import webdriver


class SignupFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Signup(self):
        self.no = 1
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'SIGN UP FLOW FROM HOME PAGE'
        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = page.BasePage(self.driver)  # Khai báo base page handler
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        TEST_DATA = [
            [1, 'Data validation', 'INVALID', sl.username, sl.username_error, 'Không nhập tên đăng nhập', '', 'Vui lòng nhập tên đăng nhập'],
            [2, 'Data validation', 'INVALID', sl.username, sl.username_error, 'Tên đăng nhập ít hơn 6 ký tự', 'abcde', 'Tên đăng nhập tối thiểu 6 ký tự'],
            [3, 'Data validation', 'VALID', sl.username, sl.username_error, 'Tên đăng nhập = 6 ký tự', 'abcdef', ''],
            [4, 'Data validation', 'INVALID', sl.username, sl.username_error, 'Tên đăng nhập nhiều hơn 29 ký tự ', 'abcdefghijklnmopqrstuvwxyz1234', 'Tên đăng nhập tối đa 29 ký tự'],
            [5, 'Data validation', 'VALID', sl.username, sl.username_error, 'Tên đăng nhập = 29 ký tự', 'abcdefghijklnmopqrstuvwxyz123', ''],
            [6, 'Data validation', 'INVALID-MULTI', sl.username, sl.username_error, 'Tên đăng nhập với ký tự đặc biệt', '!@#$%^&*() ;:\'"`~>.<,{}[]\/-=+', 'Tên đăng nhập không chứa các ký tự đặc biệt'],
            [7, 'Data validation', 'INVALID', sl.password, sl.password_error, 'Không nhập mật khẩu', '', 'Vui lòng nhập mật khẩu'],
            [8, 'Data validation', 'INVALID', sl.password, sl.password_error, 'Mật khẩu ít hơn 6 ký tự', 'mnbvc', 'Mật khẩu tối thiểu 6 ký tự'],
            [9, 'Data validation', 'VALID', sl.password, sl.password_error, 'Mật khẩu = 6 ký tự', 'mnbvcx', ''],
            [10, 'Data validation', 'INVALID', sl.password, sl.password_error, 'Mật khẩu nhiều hơn 12 ký tự ', 'sadfghjklqwer', 'Mật khẩu tối đa 12 ký tự'],
            [11, 'Data validation', 'VALID', sl.password, sl.password_error, 'Mật khẩu = 12 ký tự', 'sadfghjklqwe', ''],
            [12, 'Data validation', 'INVALID-P', [sl.username, sl.password, sl.re_password, sl.phoneno, [sl.btn_agree, sl.btn_register]], [sl.popup_error, sl.popup_error_content, sl.popup_error_btn_confirm], 'Tài khoản đã tồn tại', ['tuananhle2203','123456','123456','0909090909'], 'Tài khoản đã tồn tại'],
            [13, 'Data validation', 'INVALID', sl.re_password, sl.re_password_error, 'Mật khẩu nhập lại không trùng khớp', 'khongtrung', 'Mật khẩu nhập lại không trùng khớp'],
            [14, 'Data validation', 'VALID', sl.re_password, sl.re_password, 'Mật khẩu nhập lại trùng khớp', '123456', ''],
            [15, 'Data validation', 'INVALID', sl.phoneno, sl.phoneno_error, 'Không nhập số điện thoại', '', 'Vui lòng nhập số điện thoại'],
            [16, 'Data validation', 'INVALID', sl.phoneno, sl.phoneno_error, 'Số điện thoại ít hơn 10 ký tự', '123456789', 'Số điện thoại yêu cầu tối thiểu 10 ký tự'],
            [17, 'Data validation', 'VALID', sl.phoneno, sl.phoneno_error, 'Số điện thoại nhiều hơn 11 ký tự', '123456789145', ''],
            [18, 'Data validation', 'VALID', sl.phoneno, sl.phoneno_error, 'Số điện thoại có 10 ký tự', '1234567890', ''],
            [19, 'Data validation', 'VALID', sl.phoneno, sl.phoneno_error, 'Số điện thoại có 11 ký tự', '12345678901', ''],
            [20, 'Data validation', 'INVALID', sl.phoneno, sl.phoneno_error, 'Nhập chữ ở trường số điện thoại', '12345abcdef', 'Số điện thoại yêu cầu tối thiểu 10 ký tự'],
            [21, 'Data validation', 'VALID', sl.phoneno, sl.phoneno_error, 'Nhập chữ ở trường số điện thoại', '0935770998haha', ''],
            [22, 'Navigation', '0', sl.username, sl.password, 'Đăng ký khi uncheck Tôi đồng ý...', ['tuananhle_', '123456'], 'http://dev-ta.mooo.com'],
            [23, 'Navigation', '1', sl.username, sl.password, 'Đăng ký khi check Tôi đồng ý... Chuyển đến trang nạp tiền nếu đăng nhập thành công', ['tuananhle_', '123456'], 'http://dev-ta.mooo.com/account/deposit'],
            [24, 'Show/Hide pw', 'SHOW', sl.password, [sl.show_pass, sl.hide_pass], 'Click show/hide sl.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '-', 'text'],
            [25, 'Show/Hide pw', 'HIDE', sl.password, [sl.hide_pass, sl.show_pass], 'Click show/hide sl.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '-', 'password'],
            [26, 'Show/Hide pw', 'SHOW', sl.re_password, [sl.show_repass, sl.hide_repass], 'Click show/hide nhập lại sl.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '-', 'text'],
            [27, 'Show/Hide pw', 'HIDE', sl.re_password, [sl.hide_repass, sl.show_repass], 'Click show/hide nhập lại sl.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '-', 'password'],
            # [28, 'Helptext', 'TEXT', sl.username, None, 'Tên đăng nhập', '', 'Tên đăng nhập'],
            # [29, 'Helptext', 'TEXT', sl.password, None, 'Mật khẩu', '', 'Mật khẩu'],
            # [30, 'Helptext', 'TEXT', sl.re_password, None, 'Nhập lại mật khẩu', '', 'Nhập lại mật khẩu'],
            # [31, 'Helptext', 'TEXT', sl.phoneno, None, 'Số điện thoại', '', 'Số điện thoại'],
            # [32, 'Helptext', 'TEXT', sl.invite_code, None, 'Mã giới thiệu (Nếu có)', '', 'Mã giới thiệu (Nếu có)'],
        ]

        # COMPARE LINK AND RETURN DATA LIST
        if MainMenuLocators.MENU_DANG_KY.visible():
            MainMenuLocators.MENU_DANG_KY.click()
            self.driver.implicitly_wait(30)
            sl.btn_register.click()
            time.sleep(3)
            self.driver.implicitly_wait(30)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            # CHECK DEFAULT CASE
            for i in TEST_DATA:
                print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
                if sl.btn_register.visible() == False:
                    MainMenuLocators.MENU_DANG_KY.click()
                actual = ''
                sts = ''
                notes = ''
                if i[1] == 'Data validation':
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], i[6], '-', '-', '-', '-'])
                            self.TEST_RESULT = self.TEST_RESULT + page.ValidateData.CheckINVALIDCase(i, self.name, base)
                        else:
                            self.TEST_RESULT.append(page.ValidateData.CheckINVALIDCase(i, self.name, base))
                    elif i[2] == 'VALID':
                        self.TEST_RESULT.append(page.ValidateData.CheckVALIDCase(i, self.name, base))

                elif i[1] == 'Show/Hide pw':
                    self.TEST_RESULT.append(page.ValidateData.ShowHideButton(i, self.name, base))
                elif i[1] == 'Navigation':
                    if sl.username.visible() == False:
                        MainMenuLocators.MENU_DANG_KY.click()
                        time.sleep(3)
                    else:
                        sl.btn_close.click()
                        MainMenuLocators.MENU_DANG_KY.click()
                        time.sleep(3)
                    now = re.sub('[ :-]', '', str(datetime.now()).split('.')[0])
                    sl.username.set_text(i[6][0] + now)
                    sl.password.set_text(i[6][1])
                    sl.re_password.set_text(i[6][1])
                    sl.phoneno.set_text('0935770998')
                    if i[2] == '0':
                        sl.btn_register.click()
                        if sl.btn_register.visible():
                            actual = base.get_url()
                            if actual == i[7]:
                                sts = 'PASSED'
                            else:
                                sts = 'FAILED'
                                notes = 'Link is wrong'
                                base.ScrShot(str(i[0])+'_Link is wrong', self.name)
                        else:
                            sts = 'FAILED'
                            notes = 'Do not stand on register when register without tick "Tôi đồng ý ..."'
                            base.ScrShot(str(i[0])+'_Do not stand on register', self.name)
                    else:
                        sl.btn_agree.click()
                        sl.btn_register.click()
                        if MainMenuLocators.MENU_USER_INFO_DROP.visible():
                            actual = base.get_url()
                            if actual == i[7]:
                                sts = 'PASSED'
                            else:
                                sts = 'FAILED'
                                notes = 'Login successful but link wrong'
                                base.ScrShot(str(i[0])+'_Login successful but link wrong', self.name)
                            MainMenuLocators.MENU_USER_INFO_DROP.click()
                            UserInfoLocator.drop_logout.click()
                        else:
                            sts = 'FAILED'
                            notes = 'Login un-successful'
                            base.ScrShot(
                                str(i[0])+'_Login un-successful', self.name)
                    self.TEST_RESULT.append([i[0], i[5], i[6][0]+now+', '+i[6][1], i[7], actual, sts, notes])

                elif i[1] == 'Helptext':
                    self.TEST_RESULT.append(page.ValidateData.HelpTextCheck(i, self.name, base))
                Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
                Template_Report.export()
                Template_Report.close()
                time.sleep(2)

            end = datetime.now()
            self.TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Time spend', str(end-start).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Size', str(SIZE)])
            # REPORT data
            report = Report(self.name.upper(), self.TEST_RESULT,self.TEST_DATA_HEADER)
            report.export()
            report.close()

        else:
            base.ScrShot('Test Checking url link: FAILED')
            # print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()