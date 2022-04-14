# from Reading.src.pages.utils import Report_temp
import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter

from Reading.src.pages.Browser import Browser
import Reading.src.pages.page as page
from Reading.src.pages.locators import *
from Reading.src.pages.locators import CongGameLocators as cg
from Reading.src.pages.UIObject import UiObject
from Reading.src.pages.utils import *

class GameLobby(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_url_link(self):
        self.no = 1
        self.cur_position = 0
        self.lobby_domain = 'http://dev-ta.mooo.com/cong-game'
        DATA_LINK = [0, 0, 0]

        TEST_DATA_HEADER = []
        name = 'Test link formats - GAME LOBBY'
        TEST_RESULT = [['#', 'Slug 1', 'Slug 2', 'Slug 3', 'Expected link', 'Actual link', 'Status']]
        TEST_DATA_HEADER = []
        start = datetime.now()
        TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        lobby = page.GameLobbyPage(self.driver)  # Khai báo lobby page
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = lobby.get_size()

        # COMPARE LINK AND RETURN DATA LIST
        def check_link(data, number):
            expected = self.lobby_domain
            TYPE = []
            NCC = []
            SORT = []
            data_return = [self.no]
            self.no += 1
            for i in data:
                if i != 0:
                    if 'type' in i[2]:
                        TYPE.append(i)
                    if 'ncc' in i[2]:
                        NCC.append(i)
                    if 'sx' in i[2]:
                        SORT.append(i)
            if len(TYPE) > 1:
                for t in range(len(TYPE)):
                    if t == 0:
                        expected = expected + '?' + TYPE[t][2]
                    else:
                        expected = expected + ','+TYPE[t][2].split('=')[1]
            elif len(TYPE) == 1 and TYPE[0][2] != 'type=all':
                expected = expected + '?' + TYPE[0][2]
            for t in TYPE:
                data_return.append(t[1])
            if len(TYPE) > 0:
                if len(NCC) != 0:
                    if TYPE[0][2] != 'type=all':
                        expected = expected + '&' + NCC[0][2]
                    else:
                        expected = expected + '?' + NCC[0][2]
                    data_return.append(NCC[0][1])
                    if len(SORT) != 0:
                        expected = expected + '&' + SORT[0][2]
                        data_return.append(SORT[0][1])
                else:
                    if len(SORT) != 0:
                        if TYPE[0][2] != 'type=all':
                            expected = expected + '&' + SORT[0][2]
                        else:
                            expected = expected + '?' + SORT[0][2]
                        data_return.append(SORT[0][1])
            else:
                if len(NCC) != 0:
                    expected = expected + '?' + NCC[0][2]
                    data_return.append(NCC[0][1])
                    if len(SORT) != 0:
                        expected = expected + '&' + SORT[0][2]
                        data_return.append(SORT[0][1])
                else:
                    if len(SORT) != 0:
                        expected = expected + '?' + SORT[0][2]
                        data_return.append(SORT[0][1])

            while len(data_return) < 4:
                data_return.append('-')
            data_return.append(expected)
            actual = lobby.get_url()
            data_return.append(actual)
            if actual != expected:
                data_return.append('FAILED')
                # lobby.ScrShot(str(number) + '_' + data_return[1] + '_' + data_return[2] + '_' + data_return[3])
            else:
                data_return.append('PASSED')
            print('\n', '-'*15, ' Case: ', number,
                  ': ', data_return[6], ' ', 15*'-')
            print(data_return[1], ' - ', data_return[2], ' - ', data_return[3])
            print('Expected link: \t', data_return[4])
            print('Actual link: \t', data_return[5])
            return data_return

        # num : vị trí ở DATALINK, value:
        def click_and_check(obj, value=True, isAdded=True):
            obj[0].click()
            time.sleep(0.5)
            if value == False:
                DATA_LINK[self.cur_position-1] = 0
            else:
                DATA_LINK[self.cur_position] = obj
            check = check_link(DATA_LINK, self.no)
            if isAdded == True:
                self.cur_position += 1
            else:
                self.cur_position -= 1
                if self.cur_position < 0:
                    self.cur_position = 0
            TEST_RESULT.append(check)

        if MainMenuLocators.MENU_CONG_GAME.visible():
            MainMenuLocators.MENU_CONG_GAME.click()
            self.driver.implicitly_wait(30)
            time.sleep(3)
            Template_Report = Report_temp(name.upper(), TEST_RESULT, TEST_DATA_HEADER)
            # CHECK DEFAULT CASE
            df_link = 'http://dev-ta.mooo.com/cong-game'
            c_url = lobby.get_url()
            sts = 'PASSED'
            if df_link != c_url:
                lobby.ScrShot('Default link - FAILED')
                sts = 'FAILED'
            TEST_RESULT.append([self.no, 'default', 'default', 'default', df_link, c_url, sts])
            self.no += 1
            TEST_RESULT.append(['-', 'Case chỉ có Thể loại', '', '', '', '', '', '', ''])
            DATA_LINK = [0, 0, 0]
            for T in cg.List_type:
                click_and_check(T)
                self.cur_position -= 1
                time.sleep(0.5)
            Template_Report.export()
            Template_Report.close()

            # CHECK ALL CASE FOLLOWING: SORT >> TYPE >> SUPPLIER
            # TEST_RESULT.append(['', 'Sắp xếp theo', 'Thể loại', 'Nhà cung cấp', '', '', ''])
            DATA_LINK = [0, 0, 0]
            for T in cg.List_type:
                DATA_LINK = [0, 0, 0]
                print('0', self.cur_position)
                click_and_check(T)
                if T[1] == 'Game Nhanh' or T[1] == 'InGame' or T[1] == 'Table Games' or T[1] == 'Lô Đề':
                    if T[1] == 'Lô Đề':
                        pass
                    else:
                        print('abcdesadasd', self.cur_position)
                        for S in cg.List_Sort:
                            print('1', self.cur_position)
                            click_and_check(S)
                            self.cur_position -= 1
                else:
                    for S in cg.List_Sort:
                        print('1', self.cur_position)
                        click_and_check(S)
                        for N in cg.List_NCC:
                            cg.NCC_selector.click()
                            time.sleep(1)
                            print('2', self.cur_position)
                            click_and_check(N)
                            self.cur_position -= 1
                        self.cur_position -= 1
                self.cur_position -= 1
                Template_Report = Report_temp(name.upper(), TEST_RESULT, TEST_DATA_HEADER)
                Template_Report.export()
                Template_Report.close()

            end = datetime.now()
            TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            TEST_DATA_HEADER.append(['Time spend', str(end-start).split('.')[0]])
            TEST_DATA_HEADER.append(['Size', str(SIZE)])
            # REPORT data
            report = Report(name.upper(), TEST_RESULT, TEST_DATA_HEADER)
            report.export()
            report.close()
        else:
            lobby.ScrShot('Test Checking url link: FAILED')
            # print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()