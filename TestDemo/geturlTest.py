# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()

req = driver.get('http://www.baidu.com')
print()