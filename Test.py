import threading
import unittest
from selenium import webdriver
import time
from datetime import datetime
from datetime import date
import xlsxwriter
import requests
import json

from Reading.src.pages.Browser import Browser
import time
import os
from random import randint
import re
from Reading.src.pages.locators import *
from Reading.src.pages.locators import RechargeLocators as rl
from Reading.src.pages.UIObject import UiObject
from Reading.src.pages.page import *


# a = ['!','@','#','$','%','^','&','*','(',')',' ',';',':',"'",'"','`','~','>','.','<','{','}','[',']','\\',',','/','-','=','+']

# date = re.sub('[ :-]','',str(datetime.now()).split('.')[0])

class CasinoLobbyHeadingTitle(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Heading_Title_Content(self):
        self.now = ''
        self.no = 1
        self.workingPage = 'http://dev-ta.mooo.com/account/deposit'
        self.TEST_RESULT = [['#', 'Case', 'Data Input', 'Expected Error/Page link', 'Actual Error/Page link', 'Status', 'Notes']]
        self.TEST_DATA_HEADER = []
        self.name = 'Recharge using Banks'

        start = datetime.now()
        # self.TEST_DATA_HEADER.append(['Start', str(start).split('.')[0]])
        base = BasePage(self.driver)  # Khai báo base page handler
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Mở full màn hình đang test
        SIZE = base.get_size()
        if MainMenuLocators.MENU_DANG_KY.click():
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
        if UserInfoLocator.drop_username.visible():
            base.set_url(self.workingPage)
            time.sleep(3)
            rl.first_100.click()
            rl.rc_bank.click()
            time.sleep(1)
            rl.bank_Selector.click()
            a = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li')
            b = a.get_elements()
            for x in b:
                print('\'', x.text, '\'')

    def tearDown(self):
        self.driver.close()
# a= {'iBanking':{'Vietcombank':'Vui lòng nhập số lệnh giao dịch','ACB':'Vui lòng nhập số tài khoản người gửi','DongA':'Vui lòng nhập số tài khoản người gửi','Vietinbank':'Vui lòng nhập thời gian chuyển tiền','BIDV':'Vui lòng nhập số tài khoản người gửi hoặc thời gian chuyển tiền','Sacombank':'Vui lòng nhập thời gian chuyển tiền','Techcombank':'Vui lòng nhập số bút toán hoặc số tài khoản người gửi'},	'ATM':{'Vietcombank':'Vui lòng nhập số tài khoản người gửi','ACB':'Vui lòng nhập số tài khoản người gửi','DongA':'Vui lòng nhập số tài khoản người gửi','Vietinbank':'Vui lòng nhập thời gian chuyển tiền','BIDV':'Vui lòng nhập số tài khoản người gửi','Sacombank':'Vui lòng nhập thời gian chuyển tiền','Techcombank':'Vui lòng nhập số tài khoản người gửi'},	'Cash':{'Vietcombank':'Vui lòng nhập họ và tên người gửi','ACB':'Vui lòng nhập họ và tên người gửi','DongA':'Vui lòng nhập họ và tên người gửi','Vietinbank':'Vui lòng nhập họ và tên người gửi','BIDV':'Vui lòng nhập họ và tên người gửi','Sacombank':'Vui lòng nhập họ và tên người gửi','Techcombank':'Vui lòng nhập họ và tên người gửi'}}

# print(a['iBanking']['Vietcombank'])

# print(DepositLocator)

# if __name__ == "__main__":
# #     unittest.main()
# a = re.sub('[= VNĐ. ]','','= 974.295.000                      VNĐ')
# # print('`',a,'`')
# print(datetime.now().toordinal())
# print(datetime.fromordinal(datetime.now().toordinal()+30))
# a= datetime.fromordinal(datetime.now().toordinal()+30)
# print(a.day,a.month,a.year)


a = requests.get('http://dev-ta.mooo.com/api/v1/game/search?limit=999')
print(type(a.text))
print(type(json.loads(a.text)))
for i in json.loads(a.text)['data']['items']:
    print('---'*25)
    print(str(i['partner']))
    print(str(i['name']))
    print(str(i['partner_game_id']))
    print('/gameUrl?partnerProvider='+str(i['partner'])+'&partnerGameId='+str(i['partner_game_id']))
    # print(i)
