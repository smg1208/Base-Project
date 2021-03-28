# from Template.src.pages.utils import Report_temp
import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter

from pages.Browser import Browser
import pages.page as page
from pages.locators import *
from pages.UIObject import UiObject
from pages.utils import *


class GameLobby(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_url_link(self):
        self.no = 1
        self.lobby_domain = 'http://dev-ta.mooo.com/cong-game?'
        DATA_LINK = [0, 0, 0]

        TEST_DATA_HEADER = []
        name = 'Test link formats - GAME LOBBY'
        TEST_RESULT = [['#', 'Slug 1', 'Slug 2', 'Slug 3',
                        'Expected link', 'Actual link', 'Status']]
        TEST_DATA_HEADER = []
        start = datetime.now()
        TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        lobby = page.GameLobbyPage(self.driver)  # Khai báo lobby page
        # Chờ để tất cả element ở trang load xong
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = lobby.get_size()

        # Variable Define
        MENU_CONG_GAME = UiObject(*MainMenuLocators.MENU_CONG_GAME)
        type_all = UiObject(*CongGameLocators.Type_All)
        type_No_hu = UiObject(*CongGameLocators.Type_No_hu)
        type_Ban_ca = UiObject(*CongGameLocators.Type_Ban_ca)
        type_Lo_de = UiObject(*CongGameLocators.Type_Lo_de)
        type_Ingame = UiObject(*CongGameLocators.Type_Ingame)
        type_Table_gane = UiObject(*CongGameLocators.Type_Table_game)
        type_Game_nhanh = UiObject(*CongGameLocators.Type_Game_nhanh)

        NCC_Selector = UiObject(*CongGameLocators.NCC_selector)
        NCC_Techplay = UiObject(*CongGameLocators.NCC_btn_Techplay)
        NCC_Pragmatic = UiObject(*CongGameLocators.NCC_btn_PragmaticPlay)
        NCC_CQ9 = UiObject(*CongGameLocators.NCC_btn_CQ9)

        Sort_multi = UiObject(*CongGameLocators.Sort_Nhieu_nguoi_choi)
        Sort_hot = UiObject(*CongGameLocators.Sort_Dang_hot)
        Sort_Pho_bien = UiObject(*CongGameLocators.Sort_Pho_bien)
        Sort_new = UiObject(*CongGameLocators.Sort_Moi_nhat)
        Sort_a_z = UiObject(*CongGameLocators.Sort_a_z)

        List_type = [
            [type_all, 'Tất cả', 'type=all'],
            [type_No_hu, 'Nổ hũ', 'type=no-hu'],
            [type_Ban_ca, 'Bắn Cá', 'type=ban-ca'],
            [type_Game_nhanh, 'Game nhanh', 'type=quick-game'],
            [type_Ingame, 'Ingame', 'type=ingame'],
            [type_Table_gane, 'Table game', 'type=table-games'],
            [type_Lo_de, 'Lô đề', 'type=lo-de']
        ]

        List_NCC = [
            [NCC_Pragmatic, 'Pragmatic Play', 'ncc=pragmatic-play'],
            [NCC_CQ9, 'CQ9', 'ncc=cq9'],
            [NCC_Techplay, 'Techplay', 'ncc=techplay']
        ]

        List_Sort = [
            [Sort_multi, 'Nhiều người chơi', 'sx=nhieu-nguoi-choi'],
            [Sort_hot, 'Đang hot', 'sx=dang-hot'],
            [Sort_Pho_bien, 'Phổ biến', 'sx=pho-bien'],
            [Sort_new, 'Mới nhất', 'sx=moi-nhat'],
            [Sort_a_z, 'A-Z', 'sx=a-z']
        ]

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
                        expected = expected + TYPE[t][2]
                    else:
                        expected = expected + ','+TYPE[t][2].split('=')[1]
            elif len(TYPE) == 1:
                expected = expected + TYPE[0][2]
            for t in TYPE:
                data_return.append(t[1])
            if len(TYPE) > 0:
                if len(NCC) != 0:
                    expected = expected + '&' + NCC[0][2]
                    data_return.append(NCC[0][1])
                if len(SORT) != 0:
                    expected = expected + '&' + SORT[0][2]
                    data_return.append(SORT[0][1])
            else:
                if len(NCC) != 0:
                    expected = expected + NCC[0][2]
                    data_return.append(NCC[0][1])
                    if len(SORT) != 0:
                        expected = expected + '&' + SORT[0][2]
                        data_return.append(SORT[0][1])
                else:
                    if len(SORT) != 0:
                        expected = expected + '&' + SORT[0][2]
                        data_return.append(SORT[0][1])

            while len(data_return) < 4:
                data_return.append('-')
            data_return.append(expected)
            actual = lobby.get_url()
            data_return.append(actual)
            if actual != expected:
                data_return.append('FAILED')
                # lobby.screenshot_window(str(number) + '_' + data_return[1] + '_' + data_return[2] + '_' + data_return[3])
            else:
                data_return.append('PASSED')
            print('\n', '-'*15, ' Case: ', number,
                  ': ', data_return[6], ' ', 15*'-')
            print(data_return[1], ' - ', data_return[2], ' - ', data_return[3])
            print('Expected link: \t', data_return[4])
            print('Actual link: \t', data_return[5])
            return data_return

        # num : vị trí ở DATALINK, value:
        def click_and_check(obj, num, value=0):
            obj[0].click()
            time.sleep(0.5)
            if value == 0:
                DATA_LINK[num] = 0
            else:
                DATA_LINK[num] = obj
            check = check_link(DATA_LINK, self.no)
            TEST_RESULT.append(check)

        if MENU_CONG_GAME.visible():
            MENU_CONG_GAME.click()
            self.driver.implicitly_wait(30)
            time.sleep(3)
            temp_rp = Report_temp(name.upper(), TEST_RESULT, TEST_DATA_HEADER)
            # CHECK DEFAULT CASE
            df_link = 'http://dev-ta.mooo.com/cong-game'
            c_url = lobby.get_url()
            sts = 'PASSED'
            if df_link != c_url:
                lobby.screenshot_window('Default link - FAILED')
                sts = 'FAILED'
            TEST_RESULT.append(
                [self.no, 'default', 'default', 'default', df_link, c_url, sts])
            self.no += 1

            # CHECK ALL CASE FOLLOWING: SORT >> TYPE >> SUPPLIER
            # TEST_RESULT.append(['', 'Sắp xếp theo', 'Thể loại', 'Nhà cung cấp', '', '', ''])
            DATA_LINK = [0, 0, 0]
            for S in List_Sort:
                DATA_LINK[1] = List_type[0]
                click_and_check(S, 0, 1)
                for T in List_type:
                    if T[1] == 'Game nhanh' or T[1] == 'Ingame' or T[1] == 'Table game' or T[1] == 'Lô đề':
                        if T[1] == 'Lô đề':
                            T[0].click()
                            time.sleep(0.5)
                            DATA_LINK[0] = T
                            DATA_LINK[1] = 0
                            DATA_LINK[2] = 0
                            check = check_link(DATA_LINK, self.no)                     
                            TEST_RESULT.append(check)
                            DATA_LINK[0] = S
                            type_all.click()
                        else:
                            click_and_check(T, 1, 1)
                    else:
                        click_and_check(T, 1, 1)
                        for N in List_NCC:
                            NCC_Selector.click()
                            time.sleep(2)
                            click_and_check(N, 2, 1)
                            # UNCHECK NHÀ CUNG CẤP
                            NCC_Selector.click()
                            time.sleep(2)
                            click_and_check(N, 2, 0)
                    List_type[0][0].click()
                    temp_rp = Report_temp(
                        name.upper(), TEST_RESULT, TEST_DATA_HEADER)
                    temp_rp.export()
                    temp_rp.close()

            # CHECK ALL CASE FOLLOWING: SORT >> SUPPLIER >> TYPE
            # TEST_RESULT.append(
            #     ['', 'Sắp xếp theo', 'Nhà cung cấp', 'Thể loại', '', '', ''])
            # DATA_LINK = [0, 0, 0]
            # for S in List_Sort:
            #     S[0].click()
            #     time.sleep(0.5)
            #     DATA_LINK[0] = S
            #     check = check_link(DATA_LINK, no)
            #     no += 1
            #     TEST_RESULT.append(check)
            #     for N in List_NCC:
            #         NCC_Selector.click()
            #         time.sleep(2)
            #         N[0].click(True)
            #         time.sleep(0.5)
            #         DATA_LINK[1] = N
            #         check = check_link(DATA_LINK, no)
            #         no += 1
            #         TEST_RESULT.append(check)
            #         for T in List_type:
            #             if T[1] == 'Game nhanh' or T[1] == 'Ingame' or T[1] == 'Table game' or T[1] == 'Lô đề':
            #                 if T[1] == 'Lô đề':
            #                     T[0].click()
            #                     time.sleep(0.5)
            #                     DATA_LINK[0] = T
            #                     DATA_LINK[1] = 0
            #                     DATA_LINK[2] = 0
            #                     check = check_link(DATA_LINK, no)
            #                     no += 1
            #                     TEST_RESULT.append(check)
            #                     DATA_LINK[0] = S
            #                     DATA_LINK[1] = N
            #                     type_all.click()
            #                 else:
            #                     T[0].click()
            #                     time.sleep(0.5)
            #                     DATA_LINK[1] = T
            #                     check = check_link(DATA_LINK, no)
            #                     no += 1
            #                     TEST_RESULT.append(check)
            #             else:
            #                 T[0].click()
            #                 time.sleep(0.5)
            #                 DATA_LINK[2] = T
            #                 check = check_link(DATA_LINK, no)
            #                 no += 1
            #                 TEST_RESULT.append(check)
            #         temp_rp = Report_temp(
            #             name.upper(), TEST_RESULT, TEST_DATA_HEADER)
            #         temp_rp.export()
            #         temp_rp.close()
            #         # UNCHECK NHÀ CUNG CẤP
            #         lobby.set_url(df_link)
            #         S[0].click()

            end = datetime.now()
            TEST_DATA_HEADER.append(['End', str(end).split('.')[0]])
            TEST_DATA_HEADER.append(
                ['Time spend', str(end-start).split('.')[0]])
            TEST_DATA_HEADER.append(['Size', str(SIZE)])
            # REPORT data

            report = Report(name.upper(), TEST_RESULT, TEST_DATA_HEADER)
            report.export()
            report.close()

        else:
            lobby.screenshot_window('Test Checking url link: FAILED')
            # print('Login or Register button is not appear')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()