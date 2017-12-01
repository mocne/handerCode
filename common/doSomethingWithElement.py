# -*- coding: utf-8 -*-

import logging
import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get_screenshot_as_file('../img/%s.png' % time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time())))

def findByID(driver, ID):
    try:
        driver.find_element_by_id(ID)
    except Exception as e:
        print(e)
        return False
    else:
        el = driver.find_element_by_id(ID)
        return el

def findByCN(driver, CN):
    try:
        driver.find_element_by_class_name(CN)
    except Exception as e:
        print(e)
        return False
    else:
        el = driver.find_element_by_class_name(CN)
        return el

def findByLT(driver, LT):
    try:
        driver.find_element_by_link_text(LT)
    except Exception as e:
        print(e)
        return False
    else:
        el = driver.find_element_by_link_text(LT)
        return el

def findByXP(driver, XP):
    try:
        driver.find_element_by_xpath(XP)
    except Exception as e:
        print(e)
        return False
    else:
        el = driver.find_element_by_xpath(XP)
        return el

def findByCS(driver, CS):
    try:
        driver.find_element_by_css_selector(CS)
    except Exception as e:
        print(e)
        return False
    else:
        el = driver.find_element_by_css_selector(CS)
        return el

def findByAI(driver, AI):
    try:
        driver.find_element_by_accessibility_id(AI)
    except Exception as e:
        print(e)
        return False
    else:
        el = driver.find_element_by_accessibility_id(AI)
        return el

def findAUByID(driver, ID):
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().id(%s)' % ID)
    except Exception as e:
        print(e)
        return False
    else:
        el = driver.find_element_by_android_uiautomator('new UiSelector().id(%s)' % ID)
        return el

def findAUByTEXT(driver, TEXT):
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text(%s)' % TEXT)
    except Exception as e:
        print(e)
        return False
    else:
        el = driver.find_element_by_android_uiautomator('new UiSelector().text(%s)' % TEXT)
        return el

def findAUByDescription(driver, description):
    el = driver.find_element_by_android_uiautomator('new UiSelector().description("%s")' % description)
    return el

def findsByCN(driver, CN, index):
    el = driver.find_elements_by_class_name(CN)[index]
    return el

def get2url(Driver, Url):
    try:
        Driver.get(Url)
    except Exception as e:
        logging.error('The Driver get url: %  Fail' % Url)
        logging.error('The Driver can not open the url: %s' % e)
    else:
        time.sleep(2)
        screenshot2file(Driver)
        logging.info('The Driver open url: %s  Success' % Url)

def inputText(el, text):
    el.click()
    el.clear()
    el.send_keys(text)

# logging.basicConfig(level=logging.WARNING, filename='../Logs/log.txt' % time.strftime('%Y-%m-%d', time.localtime(time.time())), filemode='w', format='%(asctime)s - 【 %(levelname)s 】 - %(filename)s [ line:%(lineno)d ] : %(message)s')

def screenshot2file(driver):
    driver.get_screenshot_as_file('../img/%s.png' % time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time())))

def start2do(driver, Beheaver, Param, data):

    if Beheaver == 'get':
        get2url(Driver=driver, Url=Param)
        return True
    elif Beheaver == 'clickXpath':
        result = findByXP(driver=driver, XP=Param)
        return True

def doWithParm(driver, params):

    Beheaver = params['脚本操作']
    Param = params['脚本数据']
    tmpBeheaver = params['备用脚本操作']
    tmpParam = params['备用脚本数据']
    checkedData = params['数据']

    result = start2do(driver=driver, Beheaver=Beheaver, Param=Param, data=checkedData)
    if not result:
        final = start2do(driver=driver, Beheaver=tmpBeheaver, Param=tmpParam, data=checkedData)
        if not final:
            logging.error('%s: %s  fail' % tmpBeheaver, tmpParam)
