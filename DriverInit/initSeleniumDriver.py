# -*- coding: utf-8 -*-

from selenium import webdriver
import time

def initSeleniumWithInfo(browserName):

    global browser
    if browserName == 'Chrom':
        browser = webdriver.Chrome()
    elif browserName == 'Firefox':
        browser = webdriver.Firefox()
    elif browserName == 'IE':
        browser = webdriver.Ie()
    elif browserName == 'Opera':
        browser = webdriver.Opera()
    browser.maximize_window()
    browser.implicitly_wait(10)
    time.sleep(2)

    return browser