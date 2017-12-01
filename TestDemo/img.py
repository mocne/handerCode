# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
import urllib

import os
import pymysql
import requests as req
from PIL import Image
from io import BytesIO


def getUrl():
    pymysql.install_as_MySQLdb()
    conn = pymysql.connect(
            host='192.168.18.252',
            port=3306,
            user='aidaijava888',
            passwd='admin_123',
            db='credit',
            charset="utf8"
            )
    cur = conn.cursor()
    cur.execute("SELECT dmi.real_name,dmi.indetity_card_opposite,dmi.indetity_card_positive FROM credit.dw_member_identity dmi WHERE real_name IN (SELECT real_name FROM credit.dw_borrow_user WHERE user_name > 18244440000 AND user_name < 18244449999) ORDER BY id DESC;")
    data = cur.fetchall()
    conn.commit()
    conn.close()
    datas = {}
    tempStr = 'adtp.cnaidai.com'
    dic = {}
    for d in data:
        if d[1] is not None:
            name = str(d[0])[2:-1]
            zhengmian = str(d[1])[2:-1]
            fanmian = str(d[2])[2:-1]
            print(str(d[1])[2:3])
            fileTemp = open('./info.txt', 'a+')
            if str(d[1])[2:3] is '/':
                fileTemp.write("用户: " + name + ';  身份证正面照： \'' + tempStr + zhengmian + "\';  身份证反面照： \'" + tempStr + fanmian + '\'\n')
                print("用户: " + name + ';  身份证正面照： \'' + tempStr + zhengmian + "\';  身份证反面照： \'" + tempStr + fanmian + '\'\n')
                datas['name'] = name
                datas['font'] = 'http://adtp.cnaidai.com' + zhengmian
                datas['back'] = 'http://adtp.cnaidai.com' + fanmian
                dic[name] = datas
                datas = {}
            elif str(d[1])[2:3] is 'h':
                fileTemp.write("用户: " + name + ';  身份证正面照： \'' + zhengmian + "\';  身份证反面照： " + fanmian + '\n')
                print("用户: " + name + ';  身份证正面照： \'' + zhengmian + "\';  身份证反面照： \'" + fanmian + '\'')
                datas['name'] = name
                datas['font'] = 'http://adtp.cnaidai.com' + zhengmian
                datas['back'] = 'http://adtp.cnaidai.com' + fanmian
                dic[name] = datas
                datas = {}
            fileTemp.close()
    return dic


def saveAsImg(d):
    temp = 0
    names = d.keys()
    for name in names:
        url1 = d[name]['font']
        url2 = d[name]['back']
        urls = [url1, url2]
        for j in range(0, 2):
            response = req.get(urls[j])
            image = Image.open(BytesIO(response.content))
            imgfile = open('./img/' + str(temp) + str(j) + '.' + image.format, 'w+')
            temp += 1
            imgfile.write(str(image))
            imgfile.close()

if __name__ == '__main__':
    urls = getUrl()
    saveAsImg(urls)