from selenium.webdriver.common.by import By
from Reading.src.pages.UIObject import UiObject


class ge(object):
    # DOMAIN = 'http://v2.fabet.info/'
    DOMAIN = 'http://dev-ta.mooo.com/'
    ProjectName = 'Reading'


class MainMenuLocators(object):
    mm_btn_the_thao = (By.XPATH, "//*[@hkatt='mm-btn-the-thao']")
    mm_btn_ban_ca = (By.XPATH, "//*[@hkatt='mm-btn-ban-ca']")
    mm_btn_live_casino = (By.XPATH, "//*[@hkatt='mm-btn-live-casino']")
    mm_btn_game_nhanh = (By.XPATH, "//*[@hkatt='mm-btn-game-nhanh']")
    mm_btn_table_game = (By.XPATH, "//*[@hkatt='mm-btn-table-game']")
    mm_btn_cong_game = (By.XPATH, "//*[@hkatt='mm-btn-cong-game']")
    mm_btn_dang_nhap = (By.XPATH, "//*[@hkatt='mm-btn-dang-nhap']")
    mm_btn_dang_ky = (By.XPATH, "//*[@hkatt='mm-btn-dang-ky']")

    mm_btn_khuyen_mai = (By.XPATH, '//*[@hkatt="mm-btn-khuyen-mai"]')
    mm_btn_tin_tuc = (By.XPATH, '//*[@hkatt="mm-btn-tin-tuc"]')
    mm_btn_game_vua_choi = (By.XPATH, '//*[@hkatt="mm-btn-game-vua-choi"]')

    mm_btn_nap_tien = (By.XPATH, '//*[@hkatt="mm-btn-nap-tien"]')
    mm_btn_chuyen_vi = (By.XPATH, '//*[@hkatt="mm-btn-chuyen-vi"]')
    mm_txt_cvi_tong_vi = (By.XPATH, '//*[@hkatt="mm-txt-cvi-tong-vi"]')
    mm_txt_cvi_vi_chinh = (By.XPATH, '//*[@hkatt="mm-txt-cvi-vi-chinh"]')
    mm_txt_cvi_vi_phu = (By.XPATH, '//*[@hkatt="mm-txt-cvi-vi-phu"]')
    mm_txt_cvi_content = (By.XPATH, '//*[@hkatt="mm-txt-cvi-content"]')
    mm_btn_cvi_nap_tien = (By.XPATH, '//*[@hkatt="mm-btn-cvi-nap-tien"]')

    mm_btn_open_dropdown = (By.XPATH, '//*[@hkatt="mm-btn-open-dropdown"]')
    mm_btn_drop_userinfo = (By.XPATH, '//*[@hkatt="mm-btn-drop-userinfo"]')
    mm_btn_drop_recharge = (By.XPATH, '//*[@hkatt="mm-btn-drop-recharge"]')
    mm_btn_drop_withdraw = (By.XPATH, '//*[@hkatt="mm-btn-drop-withdraw"]')
    mm_btn_drop_history = (By.XPATH, '//*[@hkatt="mm-btn-drop-history"]')
    mm_btn_drop_promo = (By.XPATH, '//*[@hkatt="mm-btn-drop-promo"]')
    mm_btn_drop_news = (By.XPATH, '//*[@hkatt="mm-btn-drop-news"]')
    mm_btn_drop_logout = (By.XPATH, '//*[@hkatt="mm-btn-drop-logout"]')


class CongGameLocators(object):
    cg_btn_type_all = (By.XPATH, '//*[@hkatt="cg-btn-type-all"]')
    cg_btn_type_no_hu = (By.XPATH, '//*[@hkatt="cg-btn-type-no-hu"]')
    cg_btn_type_ban_ca = (By.XPATH, '//*[@hkatt="cg-btn-type-ban-ca"]')
    cg_btn_type_lo_de = (By.XPATH, '//*[@hkatt="cg-btn-type-lo-de"]')
    cg_btn_type_ingame = (By.XPATH, '//*[@hkatt="cg-btn-type-ingame"]')
    cg_btn_type_table_game = (By.XPATH, '//*[@hkatt="cg-btn-type-table-game"]')
    cg_btn_type_game_nhanh = (By.XPATH, '//*[@hkatt="cg-btn-type-game-nhanh"]')

    cg_btn_ncc_selector = (By.XPATH, '//*[@hkatt="cg-btn-ncc-selector"]')
    cg_btn_ncc_all = (By.XPATH, '//*[@hkatt="cg-btn-ncc-all"]')
    cg_btn_ncc_techplay = (By.XPATH, '//*[@hkatt="cg-btn-ncc-techplay"]')
    cg_btn_ncc_pragmatic_play = (By.XPATH, '//*[@hkatt="cg-btn-ncc-pragmatic-play"]')
    cg_btn_ncc_cq9 = (By.XPATH, '//*[@hkatt="cg-btn-ncc-cq9"]')
    cg_btn_ncc_tomhorn = (By.XPATH, '//*[@hkatt="cg-btn-ncc-tomhorn"]')
    cg_btn_ncc_playngo = (By.XPATH, '//*[@hkatt="cg-btn-ncc-playngo"]')

    cg_btn_sort_nhieu_nguoi_choi = (By.XPATH, '//*[@hkatt="cg-btn-sort-nhieu-nguoi-choi"]')
    cg_btn_sort_dang_hot = (By.XPATH, '//*[@hkatt="cg-btn-sort-dang-hot"]')
    cg_btn_sort_pho_bien = (By.XPATH, '//*[@hkatt="cg-btn-sort-pho-bien"]')
    cg_btn_sort_moi_nhat = (By.XPATH, '//*[@hkatt="cg-btn-sort-moi-nhat"]')
    cg_btn_sort_a_z = (By.XPATH, '//*[@hkatt="cg-btn-sort-a-z"]')

    cg_btn_xem_them = (By.XPATH, '//*[@hkatt="cg-btn-xem-them"]')
    cg_lst_danh_sach_game = (By.XPATH, '//*[@hkatt="cg-lst-danh-sach-game"]')
    cg_lst_danh_sach_ten_game = (By.XPATH, '//*[@hkatt="cg-lst-danh-sach-ten-game"]')
    cg_txt_heading_title = (By.XPATH, '//*[@hkatt="cg-txt-heading-title"]')
    # Ce NOT DONE

    data_list_type = [
        [cg_btn_type_all, 'Tất Cả', 'type=all'],
        [cg_btn_type_no_hu, 'Nổ Hũ', 'type=slots'],
        [cg_btn_type_ban_ca, 'Bắn Cá', 'type=fishing'],
        [cg_btn_type_game_nhanh, 'Game Nhanh', 'type=instant'],
        [cg_btn_type_ingame, 'InGame', 'type=ingame'],
        [cg_btn_type_table_game, 'Table Games', 'type=tables'],
        [cg_btn_type_lo_de, 'Lô Đề', 'type=lode']
    ]

    data_list_ncc = [
        # [NCC_btn_All, 'Tất Cả', 'ncc=all'],
        [cg_btn_ncc_pragmatic_play, 'Pragmatic Play', 'ncc=pragmatic'],
        [cg_btn_ncc_cq9, 'CQ9', 'ncc=cq9'],
        [cg_btn_ncc_techplay, 'Techplay', 'ncc=vingame'],
        [cg_btn_ncc_tomhorn, 'Tomhorn Gaming', 'ncc=tomhorn'],
        [cg_btn_ncc_playngo, 'Play’n GO', 'ncc=playngo']
    ]

    data_list_sort = [
        [cg_btn_sort_nhieu_nguoi_choi, 'Nhiều Người Chơi', 'sx=most-played'],
        [cg_btn_sort_dang_hot, 'Đang Hot', 'sx=hot'],
        [cg_btn_sort_pho_bien, 'Phổ Biến', 'sx=popular'],
        [cg_btn_sort_moi_nhat, 'Mới Nhất', 'sx=new'],
        [cg_btn_sort_a_z, 'A-Z', 'sx=name']
    ]


class CasinoLocators(object):
    lc_btn_ncc_all = (By.XPATH, '//*[@hkatt="lc-btn-ncc-all"]')
    lc_btn_ncc_evolution = (By.XPATH, '//*[@hkatt="lc-btn-ncc-evolution"]')
    lc_btn_ncc_ebet = (By.XPATH, '//*[@hkatt="lc-btn-ncc-ebet"]')
    lc_btn_ncc_vivogaming = (By.XPATH, '//*[@hkatt="lc-btn-ncc-vivogaming"]')
    lc_btn_ncc_allbet = (By.XPATH, '//*[@hkatt="lc-btn-ncc-allbet"]')
    lc_btn_ncc_hogaming = (By.XPATH, '//*[@hkatt="lc-btn-ncc-hogaming"]')

    lc_btn_game_type_selector = (By.XPATH, '//*[@hkatt="lc-btn-game-type-selector"]')
    lc_btn_game_type_baccarat = (By.XPATH, '//*[@hkatt="lc-btn-game-type-baccarat"]')
    lc_btn_game_type_sicbo = (By.XPATH, '//*[@hkatt="lc-btn-game-type-sicbo"]')
    lc_btn_game_type_roulette = (By.XPATH, '//*[@hkatt="lc-btn-game-type-roulette"]')

    lc_btn_sort_nhieu_nguoi_choi = (By.XPATH, '//*[@hkatt="lc-btn-sort-nhieu-nguoi-choi"]')
    lc_btn_sort_dang_hot = (By.XPATH, '//*[@hkatt="lc-btn-sort-dang-hot"]')
    lc_btn_sort_pho_bien = (By.XPATH, '//*[@hkatt="lc-btn-sort-pho-bien"]')
    lc_btn_sort_moi_nhat = (By.XPATH, '//*[@hkatt="lc-btn-sort-moi-nhat"]')
    lc_btn_sort_a_z = (By.XPATH, '//*[@hkatt="lc-btn-sort-a-z"]')

    lc_btn_xem_them = (By.XPATH, '//*[@hkatt="lc-btn-xem-them"]')
    lc_lst_danh_sach_game = (By.XPATH, '//*[@hkatt="lc-lst-danh-sach-game"]')
    lc_lst_danh_sach_ten_game = (By.XPATH, '//*[@hkatt="lc-lst-danh-sach-ten-game"]')
    lc_txt_heading_title = (By.XPATH, '//*[@hkatt="lc-txt-heading-title"]')

    # Data
    data_list_game_type = [
        [lc_btn_game_type_baccarat, 'Baccarat', 'type=baccarat'],
        # [lc_btn_game_type_sicbo, 'Sicbo', 'type=sicbo'],
        [lc_btn_game_type_roulette, 'Roulette', 'type=roulette']
    ]

    data_list_ncc = [
        [lc_btn_ncc_all, 'All', 'ncc=all'],
        [lc_btn_ncc_evolution, 'Evolution', 'ncc=evo'],
        [lc_btn_ncc_ebet, 'Ebet', 'ncc=ebet'],
        [lc_btn_ncc_vivogaming, 'VivoGaming', 'ncc=vivo'],
        [lc_btn_ncc_allbet, 'Allbet', 'ncc=allbet'],
        [lc_btn_ncc_hogaming, 'HGaming', 'ncc=hogaming']
    ]

    data_list_sort = [
        [lc_btn_sort_nhieu_nguoi_choi, 'Nhiều Người Chơi', 'sx=most-played'],
        [lc_btn_sort_dang_hot, 'Đang Hot', 'sx=hot'],
        [lc_btn_sort_pho_bien, 'Phổ Biến', 'sx=popular'],
        [lc_btn_sort_moi_nhat, 'Mới Nhất', 'sx=new'],
        # [lc_btn_sort_a_z, 'A-Z', 'sx=name']
    ]


class LoginLocators(object):
    lg_in_username = (By.XPATH, '//*[@hkatt="lg-in-username"]')
    lg_in_password = (By.XPATH, '//*[@hkatt="lg-in-password"]')

    lg_txt_password_error = (By.XPATH, '//*[@hkatt="lg-txt-password-error"]')
    lg_txt_usernam_error = (By.XPATH, '//*[@hkatt="lg-txt-usernam-error"]')

    lg_ico_show_password = (By.XPATH, '//*[@hkatt="lg-ico-show-password"]')
    lg_ico_hide_password = (By.XPATH, '//*[@hkatt="lg-ico-hide-password"]')
    lg_btn_login = (By.XPATH, '//*[@hkatt="lg-btn-login"]')


class PopupLocators(object):
    pop_btn_close = (By.XPATH, '//*[@hkatt="pop-btn-close"]')
    pop_el_is_display = (By.XPATH, '//*[@hkatt="pop-el-is-display"]')
    pop_txt_title = (By.XPATH, '//*[@hkatt="pop-txt-title"]')
    pop_txt_content = (By.XPATH, '//*[@hkatt="pop-txt-content"]')
    pop_btn_confirm = (By.XPATH, '//*[@hkatt="pop-btn-confirm"]')


class SignupLocators(object):
    su_in_username = (By.XPATH, '//*[@hkatt="su-in-username"]')
    su_in_password = (By.XPATH, '//*[@hkatt="su-in-password"]')
    su_in_repassword = (By.XPATH, '//*[@hkatt="su-in-repassword"]')
    su_in_phone_no = (By.XPATH, '//*[@hkatt="su-in-phone-no"]')
    su_in_invite_code = (By.XPATH, '//*[@hkatt="su-in-invite-code"]')

    su_txt_username_error = (By.XPATH, '//*[@hkatt="su-txt-username-error"]')
    su_txt_password_error = (By.XPATH, '//*[@hkatt="su-txt-password-error"]')
    su_txt_repassword_error = (By.XPATH, '//*[@hkatt="su-txt-repassword-error"]')
    su_txt_phone_no_error = (By.XPATH, '//*[@hkatt="su-txt-phone-no-error"]')

    su_ico_show_password = (By.XPATH, '//*[@hkatt="su-ico-show-password"]')
    su_ico_hide_password = (By.XPATH, '//*[@hkatt="su-ico-hide-password"]')
    su_ico_show_repassword = (By.XPATH, '//*[@hkatt="su-ico-show-repassword"]')
    su_ico_hide_repassword = (By.XPATH, '//*[@hkatt="su-ico-hide-repassword"]')

    su_btn_agree_tou = (By.XPATH, '//*[@hkatt="su-btn-agree-tou"]')
    su_btn_register = (By.XPATH, '//*[@hkatt="su-btn-register"]')
    su_btn_close = (By.XPATH, '//*[@hkatt="su-btn-close"]')


class LeftPanelLocator(object):
    lp_txt_left_panel_username = (By.XPATH, '//*[@hkatt="lp-txt-left-panel-username"]')
    lp_txt_left_panel_so_tien = (By.XPATH, '//*[@hkatt="lp-txt-left-panel-so-tien"]')
    lp_txt_left_panel_vi_chinh = (By.XPATH, '//*[@hkatt="lp-txt-left-panel-vi-chinh"]')
    lp_txt_left_panel_vi_phu = (By.XPATH, '//*[@hkatt="lp-txt-left-panel-vi-phu"]')

    lp_btn_left_panel_user_info = (By.XPATH, '//*[@hkatt="lp-btn-left-panel-user-info"]')
    lp_btn_left_panel_recharge = (By.XPATH, '//*[@hkatt="lp-btn-left-panel-recharge"]')
    lp_btn_left_panel_withdraw = (By.XPATH, '//*[@hkatt="lp-btn-left-panel-withdraw"]')
    lp_btn_left_panel_history = (By.XPATH, '//*[@hkatt="lp-btn-left-panel-history"]')
    lp_btn_left_panel_promo = (By.XPATH, '//*[@hkatt="lp-btn-left-panel-promo"]')
    lp_btn_left_panel_logout = (By.XPATH, '//*[@hkatt="lp-btn-left-panel-logout"]')


class UserInfoLocator(object):
    ui_btn_tab_user_info = (By.XPATH, '//*[@hkatt="ui-btn-tab-user-info"]')
    ui_btn_tab_change_pass = (By.XPATH, '//*[@hkatt="ui-btn-tab-change-pass"]')
    ui_btn_tab_bank_info = (By.XPATH, '//*[@hkatt="ui-btn-tab-bank-info"]')

    ui_in_account_name = (By.XPATH, '//*[@hkatt="ui-in-account-name"]')
    ui_in_account_email = (By.XPATH, '//*[@hkatt="ui-in-account-email"]')
    ui_in_phone_no = (By.XPATH, '//*[@hkatt="ui-in-phone-no"]')
    ui_txt_account_name_error = (By.XPATH, '//*[@hkatt="ui-txt-account-name-error"]')
    ui_txt_account_email_error = (By.XPATH, '//*[@hkatt="ui-txt-account-email-error"]')
    ui_txt_phone_no_error = (By.XPATH, '//*[@hkatt="ui-txt-phone-no-error"]')
    ui_btn_email_confirm = (By.XPATH, '//*[@hkatt="ui-btn-email-confirm"]')
    ui_btn_phone_no_confirm = (By.XPATH, '//*[@hkatt="ui-btn-phone-no-confirm"]')
    ui_btn_info_confirm = (By.XPATH, '//*[@hkatt="ui-btn-info-confirm"]')

    ui_in_current_password = (By.XPATH, '//*[@hkatt="ui-in-current-password"]')
    ui_in_new_password = (By.XPATH, '//*[@hkatt="ui-in-new-password"]')
    ui_in_re_new_password = (By.XPATH, '//*[@hkatt="ui-in-re-new-password"]')
    ui_ico_show_current_pass = (By.XPATH, '//*[@hkatt="ui-ico-show-current-pass"]')
    ui_ico_hide_current_pass = (By.XPATH, '//*[@hkatt="ui-ico-hide-current-pass"]')
    ui_ico_show_new_pass = (By.XPATH, '//*[@hkatt="ui-ico-show-new-pass"]')
    ui_ico_hide_new_pass = (By.XPATH, '//*[@hkatt="ui-ico-hide-new-pass"]')
    ui_ico_show_re_new_pass = (By.XPATH, '//*[@hkatt="ui-ico-show-re-new-pass"]')
    ui_ico_hide_re_new_pass = (By.XPATH, '//*[@hkatt="ui-ico-hide-re-new-pass"]')
    ui_btn_change_pass_confirm = (By.XPATH, '//*[@hkatt="ui-btn-change-pass-confirm"]')

    ui_btn_them_ngan_hang = (By.XPATH, '//*[@hkatt="ui-btn-them-ngan-hang"]')

    # CONFIRM POPUP
    ui_el_confirm_popup = (By.XPATH, '//*[@hkatt="ui-el-confirm-popup"]')
    ui_btn_confirm_confirm = (By.XPATH, '//*[@hkatt="ui-btn-confirm-confirm"]')
    ui_btn_confirm_close = (By.XPATH, '//*[@hkatt="ui-btn-confirm-close"]')
    ui_btn_confirm_resend = (By.XPATH, '//*[@hkatt="ui-btn-confirm-resend"]')
    ui_txt_title = (By.XPATH, '//*[@hkatt="ui-txt-title"]')
    ui_txt_content = (By.XPATH, '//*[@hkatt="ui-txt-content"]')


class RechargeLocators(object):
    # REUSE LOCATOR
    rc_btn_recharge_confirm = (By.XPATH,'//*[@hkatt="rc-btn-recharge-confirm"]')
    rc_btn_huong_dan_nap_tien = (By.XPATH,'//*[@hkatt="rc-btn-huong-dan-nap-tien"]')

    rc_btn_promo_100 = (By.XPATH,'//*[@hkatt="rc-btn-promo-100"]')
    rc_btn_promo_40 = (By.XPATH,'//*[@hkatt="rc-btn-promo-40"]')
    rc_btn_promo_1dot6 = (By.XPATH,'//*[@hkatt="rc-btn-promo-1dot6"]')

    rc_btn_first_recharge_100 = (By.XPATH, '//*[@hkatt="rc-btn-first-recharge-100"]')
    rc_btn_first_recharge_40 = (By.XPATH, '//*[@hkatt="rc-btn-first-recharge-40"]')
    rc_btn_first_recharge_1dot6 = (By.XPATH, '//*[@hkatt="rc-btn-first-recharge-1dot6"]')

    # USING BANK LOCATOR
    rc_btn_tab_bank = (By.XPATH, '//*[@hkatt="rc-btn-tab-bank"]')
    rc_btn_tab_card = (By.XPATH, '//*[@hkatt="rc-btn-tab-card"]')
    rc_btn_tab_momo = (By.XPATH, '//*[@hkatt="rc-btn-tab-momo"]')
    rc_btn_tab_paywin = (By.XPATH, '//*[@hkatt="rc-btn-tab-paywin"]')

    rc_btn_bank_selector = (By.XPATH,'//*[@hkatt="rc-btn-bank-selector"]')
    rc_btn_sacombank = (By.XPATH,'//*[@hkatt="rc-btn-sacombank"]')
    rc_btn_techcombank = (By.XPATH,'//*[@hkatt="rc-btn-techcombank"]')
    rc_btn_vietcombank = (By.XPATH,'//*[@hkatt="rc-btn-vietcombank"]')
    rc_btn_vietinbank = (By.XPATH,'//*[@hkatt="rc-btn-vietinbank"]')
    rc_btn_acb = (By.XPATH,'//*[@hkatt="rc-btn-acb"]')
    rc_btn_bidv = (By.XPATH,'//*[@hkatt="rc-btn-bidv"]')
    rc_btn_donga = (By.XPATH,'//*[@hkatt="rc-btn-donga"]')

    rc_btn_bank_type_ibanking = (By.XPATH, '//*[@hkatt="rc-btn-bank-type-ibanking"]')
    rc_btn_bank_type_atm = (By.XPATH, '//*[@hkatt="rc-btn-bank-type-atm"]')
    rc_btn_bank_type_banking = (By.XPATH, '//*[@hkatt="rc-btn-bank-type-banking"]')

    rc_in_bank_amount = (By.XPATH, '//*[@hkatt="rc-in-bank-amount"]')
    rc_in_bank_sender_name = (By.XPATH, '//*[@hkatt="rc-in-bank-sender-name"]')
    rc_in_bank_code = (By.XPATH, '//*[@hkatt="rc-in-bank-code"]')
    rc_txt_bank_amount_error = (By.XPATH, '//*[@hkatt="rc-txt-bank-amount-error"]')
    rc_txt_bank_sender_name_error = (By.XPATH, '//*[@hkatt="rc-txt-bank-sender-name-error"]')
    rc_txt_bank_code_error = (By.XPATH, '//*[@hkatt="rc-txt-bank-code-error"]')

    rc_btn_bank_promo_100 = (By.XPATH, '//*[@hkatt="rc-btn-bank-promo-100"]')
    rc_btn_bank_promo_40 = (By.XPATH, '//*[@hkatt="rc-btn-bank-promo-40"]')
    rc_btn_bank_promo_1dot6 = (By.XPATH, '//*[@hkatt="rc-btn-bank-promo-1dot6"]')

    rc_txt_bank_output_amount = (By.XPATH, '//*[@hkatt="rc-txt-bank-output-amount"]')

    rc_txt_bank_amount_promo = (By.XPATH, '//*[@hkatt="rc-txt-bank-amount-promo"]')
    rc_txt_bank_amount_real = (By.XPATH, '//*[@hkatt="rc-txt-bank-amount-real"]')
    rc_txt_bank_amount_min_of_bet = (By.XPATH, '//*[@hkatt="rc-txt-bank-amount-min-of-bet"]')
    rc_txt_bank_time_to_finish = (By.XPATH, '//*[@hkatt="rc-txt-bank-time-to-finish"]')

    rc_btn_bank_recharge_confirm = (By.XPATH, '//*[@hkatt="rc-btn-bank-recharge-confirm"]')
    rc_txt_bank_suggest_text = (By.XPATH, '//*[@hkatt="rc-txt-bank-suggest-text"]')

    rc_btn_bank_copy_owner = (By.XPATH, '//*[@hkatt="rc-btn-bank-copy-owner"]')
    rc_btn_bank_copy_account_no = (By.XPATH, '//*[@hkatt="rc-btn-bank-copy-account-no"]')
    rc_btn_bank_copy_brand = (By.XPATH, '//*[@hkatt="rc-btn-bank-copy-brand"]')
    rc_txt_bank_copy_owner = (By.XPATH, '//*[@hkatt="rc-txt-bank-copy-owner"]')
    rc_txt_bank_copy_account_no = (By.XPATH, '//*[@hkatt="rc-txt-bank-copy-account-no"]')
    rc_txt_bank_copy_brand = (By.XPATH, '//*[@hkatt="rc-txt-bank-copy-brand"]')

    # RECHARGE USING CARD SELECTOR
    rc_btn_ncc_viettel = (By.XPATH, '//*[@hkatt="rc-btn-ncc-viettel"]')
    rc_btn_ncc_vinaphone = (By.XPATH, '//*[@hkatt="rc-btn-ncc-vinaphone"]')
    rc_btn_ncc_mobifone = (By.XPATH, '//*[@hkatt="rc-btn-ncc-mobifone"]')

    data_percentage_card_fee = {
        'viettel': 32,
        'vinaphone': 32,
        'mobifone': 34
    }

    rc_btn_card_selector = (By.XPATH, '//*[@hkatt="rc-btn-card-selector"]')
    rc_btn_card_10k = (By.XPATH, '//*[@hkatt="rc-btn-card-10k"]')
    rc_btn_card_20k = (By.XPATH, '//*[@hkatt="rc-btn-card-20k"]')
    rc_btn_card_30k = (By.XPATH, '//*[@hkatt="rc-btn-card-30k"]')
    rc_btn_card_50k = (By.XPATH, '//*[@hkatt="rc-btn-card-50k"]')
    rc_btn_card_100k = (By.XPATH, '//*[@hkatt="rc-btn-card-100k"]')
    rc_btn_card_200k = (By.XPATH, '//*[@hkatt="rc-btn-card-200k"]')
    rc_btn_card_300k = (By.XPATH, '//*[@hkatt="rc-btn-card-300k"]')
    rc_btn_card_500k = (By.XPATH, '//*[@hkatt="rc-btn-card-500k"]')
    rc_btn_card_1000k = (By.XPATH, '//*[@hkatt="rc-btn-card-1000k"]')

    rc_in_card_pin = (By.XPATH, '//*[@hkatt="rc-in-card-pin"]')
    rc_in_card_series = (By.XPATH, '//*[@hkatt="rc-in-card-series"]')
    rc_txt_card_pin_error = (By.XPATH, '//*[@hkatt="rc-txt-card-pin-error"]')
    rc_txt_card_series_error = (By.XPATH, '//*[@hkatt="rc-txt-card-series-error"]')



    rc_txt_card_fee = (By.XPATH, '//*[@hkatt="rc-txt-card-fee"]')
    rc_txt_card_real_received = (By.XPATH, '//*[@hkatt="rc-txt-card-real-received"]')

    # RECHARGE USING MOMO LOCATOR
    rc_btn_momo_selector = (By.XPATH, '//*[@hkatt="rc-btn-momo-selector"]')
    rc_btn_momo_account = (By.XPATH, '//*[@hkatt="rc-btn-momo-account"]')

    rc_in_momo_amount = (By.XPATH, '//*[@hkatt="rc-in-momo-amount"]')
    rc_in_momo_sender_name = (By.XPATH, '//*[@hkatt="rc-in-momo-sender-name"]')
    rc_in_momo_code = (By.XPATH, '//*[@hkatt="rc-in-momo-code"]')

    rc_txt_momo_amount_error = (By.XPATH, '//*[@hkatt="rc-txt-momo-amount-error"]')
    rc_txt_momo_sender_name_error = (By.XPATH, '//*[@hkatt="rc-txt-momo-sender-name-error"]')
    rc_txt_momo_code_error = (By.XPATH, '//*[@hkatt="rc-txt-momo-code-error"]')

    rc_btn_momo_copy_phone_no = (By.XPATH, '//*[@hkatt="rc-btn-momo-copy-phone-no"]')
    rc_btn_momo_copy_owner = (By.XPATH, '//*[@hkatt="rc-btn-momo-copy-owner"]')
    rc_txt_momo_copy_phone_no = (By.XPATH, '//*[@hkatt="rc-txt-momo-copy-phone-no"]')
    rc_txt_momo_copy_owner = (By.XPATH, '//*[@hkatt="rc-txt-momo-copy-owner"]')

    # RECHARGE USING PAYWIN
    rc_el_paywin_page_is_load = (By.XPATH,'//*[@hkatt="rc-el-paywin-page-is-load"]')

    rc_in_paywin_amount = (By.XPATH,'//*[@hkatt="rc-in-paywin-amount"]')
    rc_txt_paywin_amount_error = (By.XPATH,'//*[@hkatt="rc-txt-paywin-amount-error"]')
    rc_txt_paywin_output_amount = (By.XPATH,'//*[@hkatt="rc-txt-paywin-output-amount"]')

    rc_txt_paywin_amount_promo = (By.XPATH,'//*[@hkatt="rc-txt-paywin-amount-promo"]')
    rc_txt_paywin_amount_real = (By.XPATH,'//*[@hkatt="rc-txt-paywin-amount-real"]')
    rc_txt_paywin_amount_min_of_bet = (By.XPATH,'//*[@hkatt="rc-txt-paywin-amount-min-of-bet"]')
    rc_txt_paywin_time_to_finish = (By.XPATH,'//*[@hkatt="rc-txt-paywin-time-to-finish"]')

    # DATA HELPTEXT:
    data_helptext = {
        'iBanking': {
            'Vietcombank': 'Vui lòng nhập số lệnh giao dịch',
            'ACB': 'Vui lòng nhập số tài khoản người gửi',
            'DongA': 'Vui lòng nhập số tài khoản người gửi',
            'Vietinbank': 'Vui lòng nhập thời gian chuyển tiền',
            'BIDV': 'Vui lòng nhập số tài khoản người gửi hoặc thời gian chuyển tiền',
            'Sacombank': 'Vui lòng nhập thời gian chuyển tiền',
            'Techcombank': 'Vui lòng nhập số bút toán hoặc số tài khoản người gửi'},
        'ATM': {
            'Vietcombank': 'Vui lòng nhập số tài khoản người gửi',
            'ACB': 'Vui lòng nhập số tài khoản người gửi',
            'DongA': 'Vui lòng nhập số tài khoản người gửi',
            'Vietinbank': 'Vui lòng nhập thời gian chuyển tiền',
            'BIDV': 'Vui lòng nhập số tài khoản người gửi',
            'Sacombank': 'Vui lòng nhập thời gian chuyển tiền',
            'Techcombank': 'Vui lòng nhập số tài khoản người gửi'},
        'Cash': {
            'Vietcombank': 'Vui lòng nhập họ và tên người gửi',
            'ACB': 'Vui lòng nhập họ và tên người gửi',
            'DongA': 'Vui lòng nhập họ và tên người gửi',
            'Vietinbank': 'Vui lòng nhập họ và tên người gửi',
            'BIDV': 'Vui lòng nhập họ và tên người gửi',
            'Sacombank': 'Vui lòng nhập họ và tên người gửi',
            'Techcombank': 'Vui lòng nhập họ và tên người gửi'}
    }

    data_list_banks_bank = {
        'Vietcombank': rc_btn_vietcombank,
        'ACB': rc_btn_acb,
        'DongA': rc_btn_donga,
        'Vietinbank': rc_btn_vietinbank,
        # 'BIDV': rc_btn_bidv,
        'Sacombank': rc_btn_sacombank,
        'Techcombank': rc_btn_techcombank
    }

    data_list_banks_paywin = {
        'Vietcombank': rc_btn_vietcombank,
        'ACB': rc_btn_acb,
        # 'DongA': rc_btn_donga,
        'Vietinbank': rc_btn_vietinbank,
        # 'BIDV': rc_btn_bidv,
        'Sacombank': rc_btn_sacombank,
        'Techcombank': rc_btn_techcombank
    }

    data_list_bank_method = {
        'iBanking': rc_btn_bank_type_ibanking,
        'ATM': rc_btn_bank_type_atm,
        'Cash': rc_btn_bank_type_banking
    }

    data_list_card_amount = {
        'viettel': {
            '10k': [rc_btn_card_10k, 10000],
            '20k': [rc_btn_card_20k, 20000],
            '30k': [rc_btn_card_30k, 30000],
            '50k': [rc_btn_card_50k, 50000],
            '100k': [rc_btn_card_100k, 100000],
            '200k': [rc_btn_card_200k, 200000],
            '300k': [rc_btn_card_300k, 300000],
            '500k': [rc_btn_card_500k, 500000],
            '1000k': [rc_btn_card_1000k, 1000000]},
        'vinaphone': {
            '10k': [rc_btn_card_10k, 10000],
            '20k': [rc_btn_card_20k, 20000],
            '30k': [rc_btn_card_30k, 30000],
            '50k': [rc_btn_card_50k, 50000],
            '100k': [rc_btn_card_100k, 100000],
            '200k': [rc_btn_card_200k, 200000],
            '300k': [rc_btn_card_300k, 300000],
            '500k': [rc_btn_card_500k, 500000]},
        'mobifone': {
            '10k': [rc_btn_card_10k, 10000],
            '20k': [rc_btn_card_20k, 20000],
            '30k': [rc_btn_card_30k, 30000],
            '50k': [rc_btn_card_50k, 50000],
            '100k': [rc_btn_card_100k, 100000],
            '200k': [rc_btn_card_200k, 200000],
            '300k': [rc_btn_card_300k, 300000],
            '500k': [rc_btn_card_500k, 500000]}
    }

    data_list_card_supplier = {
        'viettel': rc_btn_ncc_viettel,
        'vinaphone': rc_btn_ncc_vinaphone,
        'mobifone': rc_btn_ncc_mobifone
    }


class WithdrawLocators:
    wd_btn_card_selector = (By.XPATH,'//*[@hkatt="wd-btn-card-selector"]')
    wd_btn_card_10k = (By.XPATH,'//*[@hkatt="wd-btn-card-10k"]')
    wd_btn_card_20k = (By.XPATH,'//*[@hkatt="wd-btn-card-20k"]')
    wd_btn_card_30k = (By.XPATH,'//*[@hkatt="wd-btn-card-30k"]')
    wd_btn_card_50k = (By.XPATH,'//*[@hkatt="wd-btn-card-50k"]')
    wd_btn_card_100k = (By.XPATH,'//*[@hkatt="wd-btn-card-100k"]')
    wd_btn_card_200k = (By.XPATH,'//*[@hkatt="wd-btn-card-200k"]')
    wd_btn_card_300k = (By.XPATH,'//*[@hkatt="wd-btn-card-300k"]')
    wd_btn_card_500k = (By.XPATH,'//*[@hkatt="wd-btn-card-500k"]')
    wd_btn_card_1000k = (By.XPATH,'//*[@hkatt="wd-btn-card-1000k"]')

    wd_btn_withdraw_confirm = (By.XPATH,'//*[@hkatt="wd-btn-withdraw-confirm"]')
    wd_btn_tab_bank = (By.XPATH,'//*[@hkatt="wd-btn-tab-bank"]')
    wd_btn_tab_card = (By.XPATH,'//*[@hkatt="wd-btn-tab-card"]')

    wd_btn_bank_select_account = (By.XPATH,'//*[@hkatt="wd-btn-bank-select-account"]')
    wd_lst_bank_account_list = (By.XPATH,'//*[@hkatt="wd-lst-bank-account-list"]')
    wd_in_bank_amount = (By.XPATH,'//*[@hkatt="wd-in-bank-amount"]')
    wd_in_bank_password = (By.XPATH,'//*[@hkatt="wd-in-bank-password"]')
    wd_txt_bank_output_amount = (By.XPATH,'//*[@hkatt="wd-txt-bank-output-amount"]')
    wd_ico_bank_show_password = (By.XPATH,'//*[@hkatt="wd-ico-bank-show-password"]')
    wd_ico_bank_hide_password = (By.XPATH,'//*[@hkatt="wd-ico-bank-hide-password"]')

    wd_btn_viettel = (By.XPATH,'//*[@hkatt="wd-btn-viettel"]')
    wd_btn_vinaphone = (By.XPATH,'//*[@hkatt="wd-btn-vinaphone"]')
    wd_btn_mobifone = (By.XPATH,'//*[@hkatt="wd-btn-mobifone"]')
    wd_in_card_password = (By.XPATH,'//*[@hkatt="wd-in-card-password"]')
    wd_ico_card_show_password = (By.XPATH,'//*[@hkatt="wd-ico-card-show-password"]')
    wd_ico_card_hide_password = (By.XPATH,'//*[@hkatt="wd-ico-card-hide-password"]')

    card_Selector = UiObject(By.CLASS_NAME, 'base-select__inner')
    viettel_card_amount_10k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[10]')
    viettel_card_amount_20k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[9]')
    viettel_card_amount_30k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[8]')
    viettel_card_amount_50k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[7]')
    viettel_card_amount_100k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[6]')
    viettel_card_amount_200k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[5]')
    viettel_card_amount_300k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[4]')
    viettel_card_amount_500k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[3]')
    viettel_card_amount_1000k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[2]')

    mobi_vina_card_amount_10k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[9]')
    mobi_vina_card_amount_20k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[8]')
    mobi_vina_card_amount_30k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[7]')
    mobi_vina_card_amount_50k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[6]')
    mobi_vina_card_amount_100k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[5]')
    mobi_vina_card_amount_200k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[4]')
    mobi_vina_card_amount_300k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[3]')
    mobi_vina_card_amount_500k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[2]')

    data_listCardAmount = {
        'viettel': {
            '10k': [viettel_card_amount_10k, 10000],
            '20k': [viettel_card_amount_20k, 20000],
            '30k': [viettel_card_amount_30k, 30000],
            '50k': [viettel_card_amount_50k, 50000],
            '100k': [viettel_card_amount_100k, 100000],
            '200k': [viettel_card_amount_200k, 200000],
            '300k': [viettel_card_amount_300k, 300000],
            '500k': [viettel_card_amount_500k, 500000],
            '1000k': [viettel_card_amount_1000k, 1000000]},
        'vinaphone': {
            '10k': [mobi_vina_card_amount_10k, 10000],
            '20k': [mobi_vina_card_amount_20k, 20000],
            '30k': [mobi_vina_card_amount_30k, 30000],
            '50k': [mobi_vina_card_amount_50k, 50000],
            '100k': [mobi_vina_card_amount_100k, 100000],
            '200k': [mobi_vina_card_amount_200k, 200000],
            '300k': [mobi_vina_card_amount_300k, 300000],
            '500k': [mobi_vina_card_amount_500k, 500000]},
        'mobifone': {
            '10k': [mobi_vina_card_amount_10k, 10000],
            '20k': [mobi_vina_card_amount_20k, 20000],
            '30k': [mobi_vina_card_amount_30k, 30000],
            '50k': [mobi_vina_card_amount_50k, 50000],
            '100k': [mobi_vina_card_amount_100k, 100000],
            '200k': [mobi_vina_card_amount_200k, 200000],
            '300k': [mobi_vina_card_amount_300k, 300000],
            '500k': [mobi_vina_card_amount_500k, 500000]}
    }

    spp_viettel = UiObject(By.XPATH, '//div[@class="withdraw-select-card__list"]/div[1]')
    spp_vinaphone = UiObject(By.XPATH, '//div[@class="withdraw-select-card__list"]/div[2]')
    spp_mobifone = UiObject(By.XPATH, '//div[@class="withdraw-select-card__list"]/div[3]')

    data_listCardSupplier = {
        'viettel': spp_viettel,
        'vinaphone': spp_vinaphone,
        'mobifone': spp_mobifone
    }
