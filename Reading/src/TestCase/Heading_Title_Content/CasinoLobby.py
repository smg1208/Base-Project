import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter

from Reading.src.pages.Browser import Browser
import Reading.src.pages.page as page
from Reading.src.pages.locators import *
from Reading.src.pages.locators import CasinoLocators as cs
from Reading.src.pages.UIObject import UiObject
from Reading.src.pages.utils import *


class CasinoLobbyHeadingTitle(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Heading_Title_Content(self):
        self.no = 1
        self.cur_position = 0
        DATA_LINK = [0, 0, 0, 0, 0]
        TEST_RESULT = [['#', 'Slug 1', 'Slug 2', 'Slug 3', 'Slug 4', 'Slug 5', 'Expected link', 'Actual link', 'Status']]
        TEST_DATA_HEADER = []
        name = 'HEADING H1 CONTENT - CASINO LOBBY'
        start = datetime.now()
        TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        lobby = page.GameCasinoPage(self.driver)  # Khai báo lobby page
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = lobby.get_size()

        # COMPARE LINK AND RETURN DATA LIST
        def check_link(data, number):
            print('\n', '-'*15, ' Case: ', self.no,  ' ', 15*'-')
            expected = ''
            TYPE = []
            NCC = []
            SORT = []
            data_return = [self.no]
            for i in data:
                if i != 0:
                    if 'type' in i[2]:
                        TYPE.append(i)
                    if 'ncc' in i[2]:
                        NCC.append(i)
                    if 'sx' in i[2]:
                        SORT.append(i)
            # RULE 1
            if len(NCC) > 0 or len(SORT) > 0:
                expected = expected + 'Top'
            # RULE 2, 3
            if len(NCC) > 0 or len(SORT) > 0:
                if cs.List_Game_Load.visible():
                    number_of_game = len(cs.List_Game_Load.get_elements())
                else:
                    number_of_game = 0
                if number_of_game > 1:
                    expected = expected + ' ' + str(number_of_game) + ' Trò Chơi'
                else:
                    expected = expected + ' Trò Chơi'
            # RULE 4
            if len(TYPE) > 0:
                if len(TYPE) > 1:
                    for t in range(len(TYPE)):
                        if t == 0:
                            expected = expected + ' ' + TYPE[t][1]
                        else:
                            expected = expected + ', ' + TYPE[t][1]
                else:
                    if TYPE[0][2] == 'type=all':
                        expected = expected + ' Cổng Game'
                    else:
                        expected = expected + ' ' + TYPE[0][1]
                if len(NCC) == 0 and len(SORT) == 0:
                    expected = expected + ' Online'
                # RULE 5
                if len(SORT) > 0:
                    expected = expected + ' ' + SORT[0][1]
                # RULE 6 & 7
                if len(NCC) > 0:
                    if NCC[0][2] == 'ncc=all':
                        expected = expected + ' Của Live Casino'
                    else:
                        expected = expected + ' Của ' + NCC[0][1]
            else:
                if len(NCC) == 0 and len(SORT) == 0:
                    expected = 'Live Casino Online'
                # RULE 5
                if len(SORT) > 0:
                    expected = expected + ' ' + SORT[0][1]
                # RULE 6 & 7
                if len(NCC) > 0:
                    if NCC[0][2] == 'ncc=all':
                        if len(SORT) > 0:
                            expected = expected + ' Của Live Casino'
                        else:
                            expected = 'Live Casino Online'
                    else:
                        if len(SORT) > 0:
                            expected = expected + ' Của ' + NCC[0][1]
                        else:
                            expected = expected + ' Của ' + NCC[0][1] + ' Online'
            for t in TYPE:
                data_return.append(t[1])
            if len(TYPE) > 0:
                if len(NCC) != 0:
                    data_return.append(NCC[0][1])
                if len(SORT) != 0:
                    data_return.append(SORT[0][1])
            else:
                if len(NCC) != 0:
                    data_return.append(NCC[0][1])
                    if len(SORT) != 0:
                        data_return.append(SORT[0][1])
                else:
                    if len(SORT) != 0:
                        data_return.append(SORT[0][1])

            while len(data_return) < 6:
                data_return.append('-')
            data_return.append(expected)
            actual = cs.List_Game_Heading.get_text()
            data_return.append(actual)
            if actual != expected:
                data_return.append('FAILED')
                lobby.ScrShot(str(number) + '_' + data_return[1] + '_' + data_return[2] + '_' + data_return[3] + '_' + data_return[4] + '_' + data_return[5])
            else:
                data_return.append('PASSED')
            print('- Case: ', self.no, ': ', data_return[6], ' ')
            print(data_return[1], ' - ', data_return[2], ' - ', data_return[3], ' - ', data_return[4], ' - ', data_return[5], ' - ')
            print('- Expected title: \t', data_return[6])
            print('- Actual title: \t', data_return[7])
            self.no += 1
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

        if MainMenuLocators.MENU_LIVE_CASINO.visible():
            MainMenuLocators.MENU_LIVE_CASINO.click()
            self.driver.implicitly_wait(30)
            time.sleep(3)
            Template_Report = Report_temp(name.upper(), TEST_RESULT, TEST_DATA_HEADER)

            # CHECK DEFAULT CASE
            check = check_link(DATA_LINK, self.no)
            TEST_RESULT.append(check)

            # CHECK ONLY SORT CASE
            TEST_RESULT.append(
                ['-', 'Case chỉ có nhà cung cấp', '', '', '', '', '', '', ''])
            DATA_LINK = [0, 0, 0, 0, 0]
            for S in cs.List_NCC:
                click_and_check(S)
                self.cur_position -= 1
                time.sleep(0.5)
            Template_Report.export()
            Template_Report.close()

            # CHECK ALL CASE FOLLOWING: SORT >> SUPPLIER >> GAME TYPE
            DATA_LINK = [0, 0, 0, 0, 0]
            for N in cs.List_NCC:
                DATA_LINK = [0, 0, 0, 0, 0]
                click_and_check(N)
                for S in cs.List_Sort:
                    click_and_check(S)
                    for G in range(len(cs.List_Game)):
                        List_Game_B = [x for x in cs.List_Game]
                        List_Game_B.pop(G)
                        cs.Game_selector.click()
                        click_and_check(cs.List_Game[G])
                        for SG in List_Game_B:
                            click_and_check(SG)
                            time.sleep(1)
                        # UNCHECK GAME 3
                        # cs.Game_selector.click()
                        for SG in List_Game_B:
                            click_and_check(SG, False, False)
                            time.sleep(1)
                        click_and_check(cs.List_Game[G], False, False)
                        cs.Game_selector.click()
                        Template_Report = Report_temp(name.upper(), TEST_RESULT, TEST_DATA_HEADER)
                        Template_Report.export()
                        Template_Report.close()
                    self.cur_position -= 1
                self.cur_position -= 1
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
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
