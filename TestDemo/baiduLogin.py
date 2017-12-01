# -*- coding: utf-8 -*-

import json
import requests

cookieS = {"BDUSS": "kx4c3RnN1N4MzFNY35VZ0Z0ZHp3R090NWQtTUNUdzM5RC1wbUhLb0ZKZFRSaHBhTUFBQUFBJCQAAAAAAAAAAAEAAAApaOAJw~zUy9TaztXK1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFO58llTufJZS"}
url = "http://image.baidu.com/user/logininfo?src=pc&page=searchresult&time=1509079515748"

imgUrl = "Request URL:https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=1920x1080%E9%AB%98%E6%B8%85%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=1920x1080%E9%AB%98%E6%B8%85%E5%A3%81%E7%BA%B8&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=60&rn=30&gsm=3c&1509080011751="

datas = requests.get(url=imgUrl, cookies=cookieS).json()
print(json.dumps(datas, ensure_ascii=False, indent=4))
