# -*- coding: utf-8 -*-

import common.xlsx2json
import common.doSomethingWithElement
import time
import json
from DriverInit.initSeleniumDriver import initSeleniumWithInfo

def setUp(self):
    self.test_getData()
    global browser
    browser = initSeleniumWithInfo('Chrom')

def test_getData():

    common.xlsx2json.Excel2Json(file_path='../DATA/testData.xlsx')

    with open('../DATA/爱贷网-PC.json', 'r') as json_file:
        data = json.load(json_file)
        json_file.close()
    return data

def test_register(registerData):
    tmpData = registerData['children']['注册']
    for just2do in range(1, len(tmpData) + 1):
        common.doSomethingWithElement.doWithParm(driver=browser, params=just2do)

def tearDown():
    pass

def printMe(words):
    # fileData = open('../Logs/' + str(time.strftime('%Y%m%d')) + '.txt', 'a+')
    # print(fileData, '【%s】【info】：%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), words))
    # fileData.close()
    print(words)

    with open('../Logs/' + str(time.strftime('%Y%m%d')) + '.txt', 'w') as json_file:
        json_file.write('【%s】【info】：%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), words))
        json_file.close()

def justDo(driver, parms):
    common.doSomethingWithElement.doWithParm(driver=driver, beheaver=parms['脚本操作'], parm=parms['脚本数据'], behaver1=parms['备用脚本操作'], parm1=parms['备用脚本数据'])

if __name__ == '__main__':

    datas = test_getData()
    test_register(datas)