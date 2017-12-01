# -*- coding: utf-8 -*-

import requests
import win32api
import win32con
import time

cookieS = {"sdcm.sid": "s%3AUbr6CaXf99kwikScRCVPJO_f_qTS1exY.PQq51%2FwVSbOc39SSWsFTuUFWZjxDKw5UyH%2Bdhf0vD4E"}
getMoneyInfoUrl = "https://a.cnaidai.com/webjr/uc/indexCfg/getMoneyInfo.cgi?_=1509065388874"
moneyInfoJsonData = requests.get(url=getMoneyInfoUrl, cookies=cookieS).json()
accountUseMoney = moneyInfoJsonData["summary"]["accountUseMoney"]

haveShowed = False
while 1:
    now = int(time.strftime('%M', time.localtime(time.time())))
    second = int(time.strftime('%S', time.localtime(time.time())))
    while (now % 2) > 0:
        if haveShowed is False:
            print(now, second)
            investListPlanUrl = "https://a.cnaidai.com/webjr/invest/investListPlan.cgi?currentPage=1&pageSize=10&flag=0&timeLimitType=0&aprType=0&_=1509065792282"
            investListPlanJsonData = requests.get(url=investListPlanUrl, cookies=cookieS).json()
            planArr = investListPlanJsonData["list"]
            now = int(time.strftime('%M', time.localtime(time.time())))
            for datas in planArr:
                canDo = float(datas["remainAmount"])
                if canDo > 0:
                    if accountUseMoney > canDo:
                        toDay = int(time.strftime('d', time.localtime(time.time())))
                        if toDay > 24:
                            continue
                        print("You can buy some investListPlans and there is enough money!")
                        haveShowed = True
                        result = win32api.MessageBox(0, "You can buy some investListPlans and there is enough money!", "这是一个智投计划提示消息", win32con.MB_ICONASTERISK)
                        second = int(time.strftime('%S', time.localtime(time.time())))
                        if result == 1 and second % 3 == 0:
                            haveShowed = False

                    else:
                        print("You can buy some investListPlans, but you do not have enough money !")
                        if int(now % 3) == 0:
                            haveShowed = True
                            result = win32api.MessageBox(0, "You can buy some investListPlans, but you do not have enough money !", "这是一个智投计划提示消息", win32con.MB_ICONASTERISK)
                            second = int(time.strftime('%S', time.localtime(time.time())))
                            if result == 1 and second % 3 == 0:
                                haveShowed = False
