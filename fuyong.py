#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 在chrome.exe的目录下 启动命令windows：chrome --remote-debugging-port=9222
# C:\Program Files (x86)\Google\Chrome\Application

class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        cookies = self.driver.get_cookies()
        print(cookies)
        # return cookies
