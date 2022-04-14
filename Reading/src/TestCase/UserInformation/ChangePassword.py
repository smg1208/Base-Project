from selenium import webdriver
import time
import unittest
import xlsxwriter
import re
from datetime import datetime

from Reading.src.pages.Browser import Browser
from Reading.src.pages.page import *
from Reading.src.pages.locators import *
from Reading.src.pages.locators import UserInfoLocator as ul
from Reading.src.pages.UIObject import UiObject
from Reading.src.pages.utils import *


class ChangePasswordFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    def test_ChangePasswordFlow(self):
        self.now = ''
        self.no = 1
        self.infopage = 'http://dev-ta.mooo.com/account/infomation'
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'CHANGE USER PASSWORD'

        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = BasePage(self.driver)  # Khai báo base page handler
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # DATA TEST
        TEST_DATA = [
            [1, 'Data validation', 'INVALID', ul.chg_cur_pass, ul.chg_cur_pass_error, 'Không nhập mật khẩu hiện tại', '', 'Vui lòng nhập mật khẩu hiện tại'],
            [2, 'Data validation', 'INVALID', ul.chg_cur_pass, ul.chg_cur_pass_error, 'Mật khẩu hiện tại ít hơn 6 ký tự', 'abcde', 'Mật khẩu hiện tại không hợp lệ, yêu cầu ít nhất 6 ký tự.'],
            [3, 'Data validation', 'VALID', ul.chg_cur_pass, ul.chg_cur_pass_error, 'Mật khẩu hiện tại = 6 ký tự', 'abcdef', ''],
            [4, 'Data validation', 'VALID', ul.chg_cur_pass, ul.chg_cur_pass_error, 'Mật khẩu hiện tại nhiều hơn 12 ký tự ', 'abcdefghiyz1234', ''],
            [5, 'Data validation', 'VALID', ul.chg_cur_pass, ul.chg_cur_pass_error, 'Mật khẩu hiện tại = 12 ký tự', 'abcdefghi123', ''],
            [6, 'Data validation', 'VALID-MULTI', ul.chg_cur_pass, ul.chg_cur_pass_error, 'Mật khẩu hiện tại với ký tự đặc biệt', ['!@#$%^&*', '() ;:\'"', '`~>.<,{}', '[]\/-=+'], ''],
            [7, 'Data validation', 'INVALID', ul.chg_new_pass, ul.chg_new_pass_error, 'Không nhập mật khẩu mới', '', 'Vui lòng nhập mật khẩu mới'],
            [8, 'Data validation', 'INVALID', ul.chg_new_pass, ul.chg_new_pass_error, 'Mật khẩu mới ít hơn 6 ký tự', 'abcde', 'Mật khẩu mới không hợp lệ, yêu cầu ít nhất 6 ký tự.'],
            [9, 'Data validation', 'VALID', ul.chg_new_pass, ul.chg_new_pass_error, 'Mật khẩu mới = 6 ký tự', 'abcdef', ''],
            [10, 'Data validation', 'VALID', ul.chg_new_pass, ul.chg_new_pass_error, 'Mật khẩu mới nhiều hơn 12 ký tự ', 'abcdefhhiyz1234', ''],
            [11, 'Data validation', 'VALID', ul.chg_new_pass, ul.chg_new_pass_error, 'Mật khẩu mới = 12 ký tự', 'abcdefhhi123', ''],
            [12, 'Data validation', 'VALID-MULTI', ul.chg_new_pass, ul.chg_new_pass_error, 'Mật khẩu mới với ký tự đặc biệt', ['!@#$%^&*', '() ;:\'"', '`~>.<,{}', '[]\/-=+'], ''],
            [13, 'Data validation', 'INVALID-DUP', ul.chg_new_pass, ul.chg_new_pass_error, 'Mật khẩu mới trùng với mật khẩu cũ', '123456', 'Vui lòng nhập mật khẩu không trùng với mật khẩu cũ'],
            [14, 'Data validation', 'VALID', ul.chg_re_new_pass, ul.chg_re_new_pass_error, 'Mật khẩu nhập lại trùng khớp', '123456', ''],
            [15, 'Data validation', 'INVALID-P', [ul.chg_cur_pass, ul.chg_new_pass, ul.chg_re_new_pass, [ul.chg_confirm]], [ul.popup_error, ul.popup_error_content, ul.popup_error_btn_confirm], 'Mật khẩu hiện tại không đúng', ['tuananhle2203','123456','123456'], 'Mật khẩu hiện tại không đúng. Vui lòng thử lại'],
            [16, 'Show/Hide pw', 'SHOW', ul.chg_cur_pass, [ul.show_cur_pass, ul.hide_cur_pass], 'Click show/hide ul.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'text'],
            [17, 'Show/Hide pw', 'HIDE', ul.chg_cur_pass, [ul.hide_cur_pass, ul.show_cur_pass], 'Click show/hide ul.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'ul.password'],
            [18, 'Show/Hide pw', 'SHOW', ul.chg_new_pass, [ul.show_new_pass, ul.hide_new_pass], 'Click show/hide nhập lại ul.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'text'],
            [19, 'Show/Hide pw', 'HIDE', ul.chg_new_pass, [ul.hide_new_pass, ul.show_new_pass], 'Click show/hide nhập lại ul.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'ul.password'],
            [20, 'Show/Hide pw', 'SHOW', ul.chg_re_new_pass, [ul.show_re_new_pass, ul.hide_re_new_pass], 'Click show/hide nhập lại ul.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'text'],
            [21, 'Show/Hide pw', 'HIDE', ul.chg_re_new_pass, [ul.hide_re_new_pass, ul.show_re_new_pass], 'Click show/hide nhập lại ul.password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'ul.password'],
            [22, 'Helptext', 'TEXT', ul.chg_cur_pass, None, 'Nhập mật khẩu hiện tại', '', 'Nhập mật khẩu hiện tại'],
            [23, 'Helptext', 'TEXT', ul.chg_new_pass, None, 'Nhập mật khẩu mới', '', 'Nhập mật khẩu mới'],
            [24, 'Helptext', 'TEXT', ul.chg_re_new_pass, None, 'Nhập lại mật khẩu mới', '', 'Nhập lại mật khẩu mới'],
        ]

        # RUNNING TEST
        if MainMenuLocators.MENU_DANG_KY.visible():
            MainMenuLocators.MENU_DANG_KY.click()
            self.driver.implicitly_wait(30)
            time.sleep(5)
            self.now = re.sub('[ :-]', '', str(datetime.now()).split('.')[0])
            SignupLocators.username.set_text('tuananhle' + self.now)
            SignupLocators.password.set_text('123456')
            SignupLocators.re_password.set_text('123456')
            SignupLocators.phoneno.set_text('0935770998')
            SignupLocators.btn_agree.click()
            SignupLocators.btn_register.click()
            time.sleep(2)
            self.TEST_DATA_HEADER.append(['Account Test', 'Username: ' + 'tuananhle' + self.now+', pass: 123456'])
        if ul.drop_username.visible():
            base.set_url(self.infopage)
            time.sleep(3)
            ul.tab_changepass.click()
            time.sleep(3)
            ul.chg_confirm.click()
            self.driver.implicitly_wait(30)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            for i in TEST_DATA:
                print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
                if ul.chg_new_pass.visible() == False:
                    base.set_url(self.infopage)
                    ul.tab_changepass.click
                    time.sleep(3)
                if i[1] == 'Data validation':
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                            self.TEST_RESULT = self.TEST_RESULT + ValidateData.CheckINVALIDCase(i, self.name, base)
                        else:
                            if i[2] == 'INVALID-DUP':
                                ul.chg_cur_pass.set_text(i[6])
                            self.TEST_RESULT.append(ValidateData.CheckINVALIDCase(i, self.name, base))
                    elif i[2] == 'VALID':
                        if i[2] == 'VALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                        self.TEST_RESULT.append(ValidateData.CheckVALIDCase(i, self.name, base))

                elif i[1] == 'Show/Hide pw':
                    self.TEST_RESULT.append(ValidateData.ShowHideButton(i, self.name, base))

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
