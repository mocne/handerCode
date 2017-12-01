# -*- coding: utf-8 -*-

import logging
import time

def save2log(lev, msg):
    logging.basicConfig(level=logging.INFO, filename='../Logs/%s_log.txt' % time.strftime('%Y-%m-%d', time.localtime(time.time())), filemode='a+', format='[%(asctime)s]-【 %(levelname)s 】-(%(filename)s:line:%(lineno)d): %(message)s')
    # use logging
    if lev == 'info':
        logging.info(msg=msg)
    elif lev == 'debug':
        logging.debug(msg=msg)
    elif lev == 'warning':
        logging.warning(msg=msg)
    elif lev == 'error':
        logging.error(msg=msg)
    elif lev == 'critical':
        logging.critical(msg=msg)

if __name__ == '__main__':
    save2log('info', 'This is a info log.')
    save2log('error', 'your code do something wrong')