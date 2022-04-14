import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter

from Reading.src.pages.Browser import Browser
import Reading.src.pages.page as page
from Reading.src.pages.page import *
from Reading.src.pages.locators import *
from Reading.src.pages.locators import LoginLocators as li
from Reading.src.pages.UIObject import UiObject
from Reading.src.pages.utils import *


class LoginFlow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Login(self):
        self.no = 1
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'LOGIN FLOW FROM HOME PAGE'
        start = datetime.now()
        self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = page.BasePage(self.driver)  # Khai báo base page handler
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        TEST_DATA = [
            [1, 'Data validation', 'INVALID', li.input_username, li.text_error_username, 'Không nhập tên đăng nhập', '', 'Vui lòng nhập tên đăng nhập'],
            [2, 'Data validation', 'INVALID', li.input_username, li.text_error_username, 'Tên đăng nhập ít hơn 6 ký tự', 'abcde', 'Tên đăng nhập tối thiểu 6 ký tự'],
            [3, 'Data validation', 'VALID', li.input_username, li.text_error_username, 'Tên đăng nhập = 6 ký tự', 'abcdef', ''],
            [4, 'Data validation', 'INVALID', li.input_username, li.text_error_username, 'Tên đăng nhập nhiều hơn 30 ký tự ', 'abcdefghijklnmopqrstuvwxyz', 'Tên đăng nhập tối đa 30 ký tự'],
            [5, 'Data validation', 'VALID', li.input_username, li.text_error_username, 'Tên đăng nhập = 30 ký tự', 'abcdefghijklnmopqrstuvwxyz1234', ''],
            [6, 'Data validation', 'INVALID-MULTI', li.input_username, li.text_error_username, 'Tên đăng nhập với ký tự đặc biệt', '!@#$%^&*() ;:\'"`~>.<,{}[]\/-=+', 'Vui lòng nhập tên đăng nhập không chứa ký tự đặc biệt'],
            [7, 'Data validation', 'INVALID', li.input_password, li.text_error_password, 'Không nhập mật khẩu', '', 'Vui lòng nhập mật khẩu'],
            [8, 'Data validation', 'INVALID', li.input_password, li.text_error_password, 'Mật khẩu ít hơn 6 ký tự', 'mnbvc', 'Mật khẩu tối thiểu 6 ký tự'],
            [9, 'Data validation', 'VALID', li.input_password, li.text_error_password, 'Mật khẩu = 6 ký tự', 'mnbvcx', ''],
            [10, 'Data validation', 'INVALID', li.input_password, li.text_error_password, 'Mật khẩu nhiều hơn 12 ký tự ', 'sadfghjklqwer', 'Mật khẩu tối đa 12 ký tự'],
            [11, 'Data validation', 'VALID', li.input_password, li.text_error_password, 'Mật khẩu = 12 ký tự', 'sadfghjklqwe', ''],
            [12, 'Data validation', 'INVALID-P', [li.input_username, li.input_password, [li.btn_login]], [li.popup_error, li.popup_error_content, li.popup_error_btn_confirm], 'Nhập sai tên đăng nhập', ['khongtontai','123456'], 'Sai tên đăng nhập hoặc mật khẩu'],
            [13, 'Data validation', 'INVALID-P', [li.input_username, li.input_password, [li.btn_login]], [li.popup_error, li.popup_error_content, li.popup_error_btn_confirm], 'Nhập sai mật khẩu', ['tuananhle2203','khongdung'], 'Sai tên đăng nhập hoặc mật khẩu'],
            [14, 'Show/Hide pw', 'SHOW', li.input_password, [li.btn_show_password, li.btn_hide_password], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'text'],
            [15, 'Show/Hide pw', 'HIDE', li.input_password, [li.btn_hide_password, li.btn_show_password], 'Click show/hide password icon sẽ hiển thị những ký tự đã nhập hoặc ẩn đi', '', 'password'],
            [15, 'Navigation', '0', li.input_username, li.input_password, 'Nếu ví chính = 0, chuyển đến trang nạp tiền', ['tuananhle2603', '123456'], 'http://dev-ta.mooo.com/account/deposit'],
            [16, 'Navigation', '1', li.input_username, li.input_password, 'Nếu ví chính > 0, trở lại trang trước khi đăng nhập', ['tuananhle2603', '123456'], 'http://dev-ta.mooo.com/cong-game'],
            # [17,'Session','SESSION','Đăng nhập ở 1 trình duyệt khác sẽ log out ở trình duyệt cũ','','',]
        ]

        if MainMenuLocators.MENU_DANG_NHAP.visible():
            MainMenuLocators.MENU_DANG_NHAP.click()
            self.driver.implicitly_wait(30)
            time.sleep(10)
            li.btn_login.click()
            time.sleep(3)
            Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
            # CHECK DEFAULT CASE
            for i in TEST_DATA:
                actual = ''
                sts = ''
                notes = ''
                if i[1] == 'Data validation':
                    if 'INVALID' in i[2]:
                        if i[2] == 'INVALID-MULTI':
                            self.TEST_RESULT.append([i[0], i[5], '-', '-', '-', '-', '-'])
                            self.TEST_RESULT = self.TEST_RESULT+ValidateData.CheckINVALIDCase(i, self.name, base)
                        else:
                            self.TEST_RESULT.append(ValidateData.CheckINVALIDCase(i, self.name, base))
                    elif i[2] == 'VALID':
                        self.TEST_RESULT.append(ValidateData.CheckVALIDCase(i, self.name, base))
                elif i[1] == 'Show/Hide pw':
                    self.TEST_RESULT.append(ValidateData.ShowHideButton(i, self.name, base))

                elif i[1] == 'Navigation':
                    if i[2] == '0':
                        if li.input_username.visible() == False:
                            MainMenuLocators.MENU_DANG_NHAP.click()
                            time.sleep(3)

                    if i[2] == "1":
                        if li.input_username.visible() == False:
                            MainMenuLocators.MENU_CONG_GAME.click()
                            time.sleep(3)
                            MainMenuLocators.MENU_DANG_NHAP.click()
                            time.sleep(3)
                        else:
                            li.btn_close.click()
                            MainMenuLocators.MENU_CONG_GAME.click()
                            time.sleep(3)
                            MainMenuLocators.MENU_DANG_NHAP.click()
                            time.sleep(3)
                    i[3].set_text(i[6][0])
                    i[4].set_text(i[6][1])
                    time.sleep(3)
                    li.btn_login.click()
                    if MainMenuLocators.MENU_USER_INFO_DROP.visible():
                        actual = base.get_url()
                        if actual == i[7]:
                            sts = 'PASSED'
                        else:
                            sts = 'FAILED'
                            notes = 'Login successful but link wrong'
                            base.ScrShot(
                                str(i[0])+'_Login successful but link wrong', self.name)
                        MainMenuLocators.MENU_USER_INFO_DROP.click()
                        UserInfoLocator.drop_logout.click()
                    else:
                        sts = 'FAILED'
                        notes = 'Login un-successful'
                        base.ScrShot(str(i[0])+'_Login un-successful', self.name)
                    self.TEST_RESULT.append([i[0], i[5], i[6][0]+', '+i[6][1], i[7], actual, sts, notes])

                    print('\n', '-'*15, ' Case: ', str(i[0]), ': ', i[5], ' ', 15*'-')
                    print('Status: \t', sts)
                    print('Expected: \t', i[7])
                    print('Actual: \t', actual, '\n')
                Template_Report = Report_temp(self.name.upper(), self.TEST_RESULT, self.TEST_DATA_HEADER)
                Template_Report.export()
                Template_Report.close()
                time.sleep(2)

            end = datetime.now()
            self.TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            self.TEST_DATA_HEADER.append(
                ['Time spend', str(end-start).split('.')[0]])
            self.TEST_DATA_HEADER.append(['Size', str(SIZE)])
            # REPORT data

            report = Report(self.name.upper(), self.TEST_RESULT,
                            self.TEST_DATA_HEADER)
            report.export()
            report.close()

        else:
            base.ScrShot('[FAILED] '+self.name, self.name)
            # print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
