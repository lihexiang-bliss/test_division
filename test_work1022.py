#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, shelve
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWork1022():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        # self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_work1022(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        cookies = [
            {'domain': '.qq.com', 'expiry': 1603549358, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'Iq9zg5-9rkNcNB9yu_0k4QlzjmjnyR7aJL36Q34gVSeSDztBXX_6lg9BDpnIS1_7TyTglbvZ_N117ys_0P0j3MJT0meYMNyIyHIf_G_vqSlOGIPrjbi3uLM7YmhIlOHv7J1qNcYZTWeGUAXT2nbG02qUIpYlgz3VUfe2qIS35tPAwpk3LEhEpXHVCDE7b_Tu4Ego5nD2ilsWtlYKuh6GH3jzKqB9LFwhJbbf5Tt4FBJz_c8fT4ywl5pOfUzekaZoFLHXgqkHCVt1VVm1UvC4PQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850723527137'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850723527137'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325105167322'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5790418'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634914951, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'LqhDKL6BdAtzuZgKGn_LCRZ-MSWPQZr4tBS5uGCxkAGtGqZ-lKhiZ8iBjWUP0Nbj'},
            {'domain': '.qq.com', 'expiry': 1666621298, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1159914280.1603378955'},
            {'domain': '.qq.com', 'expiry': 1603635698, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1020942740.1603378955'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603577127, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '7ci7l5o'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '3019481555119326'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606141299, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]
        db = shelve.open('cookies')  # 打开表
        db['cookies'] = cookies

        for cookie in db['cookies']:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            'C:\\Users\\Administrator\\Desktop\\shuju.xlsx')
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        '.ww_fileImporter_fileContainer_fileNames').text == 'shuju.xlsx'
