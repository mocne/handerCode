# -*- coding:utf-8 -*-
import yaml
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def getYam(homeyaml):
    try:
        with open(homeyaml, encoding='utf-8') as f:
            x = yaml.load(f)
            return x
    except FileNotFoundError:
        print(u"找不到文件")