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


class ListGameLoading(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_ListGameLoading(self):
        self.no = 1
        self.cur_position = 0
        DATA_LINK = [0, 0, 0, 0, 0]
        TEST_RESULT = [['#', 'Partner', 'Game Id', 'Game Name', 'API', 'Status', 'Notes']]
        TEST_DATA_HEADER = []
        self.name = 'ALL GAME LOADING IN CONG GAME'
        start = datetime.now()
        TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = page.GameCasinoPage(self.driver)  # Khai báo base page
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()

        # COMPARE LINK AND RETURN DATA LIST
        MainMenuLocators.MENU_CONG_GAME.click()
        while CongGameLocators.btn_Xem_them.visible():
            CongGameLocators.btn_Xem_them.click()
            time.sleep(0.5)
        try:
            listGameName = CongGameLocators.List_Game_Load_Name.get_elements()
        except Exception:
            listGameName = []
        # for i in listGameName:
        #     print(i.text)
        # time.sleep(30)
        actual_game_name = [i.text.replace(' ', '') for i in listGameName]
        dataAPI = API(ge.DOMAIN+'api/v1/game/search', [{'key': 'limit', 'value': '999'}]).GET()

        def sortPartner(e):
            return e["partner"]

        listdata = [i for i in dataAPI['data']['items']]
        listdata.sort(key=sortPartner)
        Number = 1
        for i in range(len(listdata)):
            # sts = 'PASSED'
            notes = ''
            partner = (str(listdata[i]['partner']))
            name = (str(listdata[i]['name']))
            id = (str(listdata[i]['partner_game_id']))
            apiurl = ('/gameUrl?partnerProvider='+partner+'&partnerGameId='+id)
            if i == 0 or partner != listdata[i-1]['partner']:
                list = [a for a in listdata if a['partner'] == listdata[i]['partner']]
                count = len(list)
                TEST_RESULT.append([str(count) + ' game của ' + partner, '', '', '', '', ''])
                Number = 1
            if name.upper().replace(' ', '') in actual_game_name:
                sts = 'PASSED'
            else:
                sts = 'FAILED'
            count_name = [i for i in actual_game_name if i == name.upper()]
            if len(count_name) > 1:
                sts = 'FAILED'
                notes = 'Game ' + name + ' is displayed ' + len(count_name) + 'times'
            TEST_RESULT.append([Number, partner, id, name.upper(), apiurl, sts, notes])

            print('\n', '-'*25, ' CASE: ', self.no, ' ', '-'*25)
            print('Status:\t', sts)
            print('Partner:\t', partner)
            print('Name:\t', name)
            print('Game Id:\t', id)
            self.no += 1
            Number += 1

        # CHECK ALL CASE FOLLOWING: SORT >> SUPPLIER >> GAME TYPE

        end = datetime.now()
        TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
        TEST_DATA_HEADER.append(['Time spend', str(end-start).split('.')[0]])
        TEST_DATA_HEADER.append(['Size', str(SIZE)])
        # REPORT data
        report = Report(self.name.upper(), TEST_RESULT, TEST_DATA_HEADER)
        report.export()
        report.close()

        # base.ScrShot('Test Checking url link: FAILED')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
