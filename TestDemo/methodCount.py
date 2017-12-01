# -*- coding: utf-8 -*-
# 方法计数
import inspect

from TestDemo import myCode


def getMethodCount():

    mem = inspect.getmembers(myCode.AiDaiWangApp)
    for info in mem:
        if info[0] == '__dict__':
            temp = info[1]
            print('there are %s test case in this class' % (len(temp)-4))
            keys = list(temp.keys())
            keys.remove('__module__')
            keys.remove('setUp')
            keys.remove('tearDown')
            keys.remove('__doc__')
            for i in keys:
                print(i)
            break
