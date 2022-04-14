from unittest.case import TestCase
import HtmlTestRunner
import unittest
import os

# HEADING TITLE CONTENT Testcase
from Reading.src.TestCase.Heading_Title_Content.GameLobby import *
from Reading.src.TestCase.Heading_Title_Content.CasinoLobby import *
# URL FORMAT Testcase
from Reading.src.TestCase.Url_Format.GameLobby import *
from Reading.src.TestCase.Url_Format.CasinoLobby import *
# LOGIN SIGNUP Testcase
from Reading.src.TestCase.Login.Login import *
from Reading.src.TestCase.Login.Signup import *
# UPDATE USER INFO Testcase
from Reading.src.TestCase.UserInformation.UpdateInformation import *
from Reading.src.TestCase.UserInformation.ChangePassword import *
# RECHARGE FLOW
from Reading.src.TestCase.Recharge.Bank import *
from Reading.src.TestCase.Withdraw.Bank import *
from Reading.src.TestCase.Recharge.Momo import *
from Reading.src.TestCase.Recharge.Card import *
from Reading.src.TestCase.Withdraw.Card import *
from Reading.src.TestCase.Recharge.Paywin import *
from Reading.src.TestCase.APILoading.GameLoading import *



game_url_test = unittest.TestLoader().loadTestsFromTestCase(GameLobby)
casino_url_test = unittest.TestLoader().loadTestsFromTestCase(CasinoLobby)
game_heading_test = unittest.TestLoader().loadTestsFromTestCase(GameLobbyHeadingTitle)
casino_heading_test = unittest.TestLoader().loadTestsFromTestCase(CasinoLobbyHeadingTitle)
loginflow = unittest.TestLoader().loadTestsFromTestCase(LoginFlow)
signupflow = unittest.TestLoader().loadTestsFromTestCase(SignupFlow)
updateinfo = unittest.TestLoader().loadTestsFromTestCase(UpdateUserInformation)
changepass = unittest.TestLoader().loadTestsFromTestCase(ChangePasswordFlow)
rechargebank = unittest.TestLoader().loadTestsFromTestCase(RechargeBanksFlow)
rechargemomo = unittest.TestLoader().loadTestsFromTestCase(RechargeMomoFlow)
rechargecard = unittest.TestLoader().loadTestsFromTestCase(RechargeCardsFlow)
rechargepaywin = unittest.TestLoader().loadTestsFromTestCase(RechargePaywinFlow)

withdrawbank = unittest.TestLoader().loadTestsFromTestCase(WithdrawBanksFlow)
withdrawcard = unittest.TestLoader().loadTestsFromTestCase(WithdrawCardsFlow)
listgame = unittest.TestLoader().loadTestsFromTestCase(ListGameLoading)

# unittest.TextTestRunner().run(main)

# # Create test_suite
# test_suite = unittest.TestSuite([casino_heading_test, game_heading_test, casino_url_test, game_url_test])
# test_suite = unittest.TestSuite([casino_heading_test, game_heading_test])
test_suite = unittest.TestSuite([listgame])
unittest.TextTestRunner().run(test_suite)