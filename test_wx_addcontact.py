#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestWXWeb():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_WX_addcontact(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        cooikes=[{'domain': '.qq.com', 'expiry': 1667614043, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.847649449.1604541901'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850723527137'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850723527137'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325105167322'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8836711'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2989291740193382'},
             {'domain': '.qq.com', 'expiry': 1604628443, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1339630902.1604541901'},
             {'domain': 'work.weixin.qq.com', 'expiry': 1604573329, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8i860p2'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'LqhDKL6BdAtzuZgKGn_LCaAlo9C4K6Ap5i64ZmAxv8EgiTZNAMXQ1hl3LK2RD8oy'},
             {'domain': '.work.weixin.qq.com', 'expiry': 1636077793, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '7xnOc0RHMv_f-pIMgIz4AdbSfK9Zhbg5nLO-p6WE6cEqM0DR7UIPnbkB1ySlGjtaKTe1-xGw0cIg7wY1kUXVO0zHvG7FJwxSI95PfIlPQqFlktV14FMTot2dJk_uoQh_E8D7deL14kfU0HDCUB3zMdd0RY9rLAP_AOw1S2_9k8fdcZw8PORTYpF_cCeVTReGK3WvmTU0JZnGVUCJ9dy_FKR2t6hDytP82BA6bxhV7DIIk-bHcvCT70OpKALZvIqFnnz19Dn2TXIUqNBjFuKdhQ'},
             {'domain': '.work.weixin.qq.com', 'expiry': 1607134043, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        for cooike in cooikes:
            self.driver.add_cookie(cooike)
        self.driver.refresh()

        self.driver.find_element(By.XPATH,'//*[text()="添加成员"]').click()
        self.driver.find_element(By.ID,'username').send_keys('张4')
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('004')
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys('13500000004')
        self.driver.find_element(By.XPATH,'//*[@class="js_member_editor_form"]/div[1]/a[2]').click()

        time.sleep(3)

