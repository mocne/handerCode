# -*- coding: utf-8 -*-
# Mysql 数据库插入数据
import datetime
import time
import requests
import json
import pymysql

idArr = []
isEnd = False
currentPage = 1
sum = 0
arr = []
isIn = []

try:
    conn = pymysql.connect(host='localhost', user='mocne', passwd='111111', db='pkf_useful', port=3306, charset='utf8')
except Exception:
    conn.rollback()
    print("connect fail")
else:
    if not isEnd:
        print("aaaa")
        currentTS = int(time.mktime(datetime.datetime.now().timetuple()) * 1000)
        urls = "https://a.cnaidai.com/webjr/invest/investListPlan.cgi?currentPage=" + str(
            currentPage) + "&pageSize=100&timeLimitType=null&aprType=null&_=" + str(currentTS)

        session = requests.session()
        d1 = session.get(urls)
        d2 = d1.content
        d3 = json.loads(d2)
        arr = d3["list"]
        if len(arr) < 100:
            isEnd = True
        for i in range(0, len(arr)):
            for obj in idArr:
                if obj == arr[i]["id"]:
                    isIn.append(arr[i]["id"])
            if arr[i]["id"] not in isIn:
                idArr.append(arr[i]["id"])

        if len(arr) > 0:
            datasA = arr
            for i in range(0, len(datasA)):
                cur = conn.cursor()  # 获取一个游标
                timeLimitDay = datasA[i]["timeLimitDay"]
                alreadyInvestTotal = datasA[i]["alreadyInvestTotal"]
                apr = datasA[i]["apr"]
                remainAmount = datasA[i]["remainAmount"]
                scales = datasA[i]["scales"]
                status = datasA[i]["status"]   # 0:预售  1：出售  2：售罄
                canMoneyCoupon = datasA[i]["canMoneyCoupon"]
                isDay = datasA[i]["isDay"]
                minPay = datasA[i]["minPay"]
                timeLimitMonth = datasA[i]["timeLimitMonth"]
                plan_id = datasA[i]["id"]
                tenderTimes = datasA[i]["tenderTimes"]
                realTotal = datasA[i]["realTotal"]
                canAprCoupon = datasA[i]["canAprCoupon"]
                account = datasA[i]["account"]
                cur.execute("INSERT INTO invest_List_Plan (timeLimitDay,alreadyInvestTotal,apr,remainAmount,scales,status,canMoneyCoupon,isDay,minPay,timeLimitMonth,plan_id,tenderTimes,realTotal,canAprCoupon,account) VALUES (%d, %d, %d, %s, %.2f, %d, %s, %d, %d, %d, %d, %d, %d, %s, %d)" % (timeLimitDay, alreadyInvestTotal, apr, remainAmount, scales, status, canMoneyCoupon, isDay, minPay, timeLimitMonth, plan_id, tenderTimes, realTotal, canAprCoupon, account))
                conn.commit()
                print(datasA[i]["name"])
                data = cur.fetchall()
                print(data)
                cur.close()  # 关闭游标
        currentPage += 1
    else:
        conn.close()  # 释放数据库资源