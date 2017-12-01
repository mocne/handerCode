# -*- coding: utf-8 -*-

'''
    if beheaver == 'get':
        try:
            driver.get(parm)
        except Exception as e:
            screenshot2file(driver)
            logging.error('%s: %s False' % beheaver, parm)
            print(e)
            logging.error('%s: %s - %s' % beheaver, parm, e)
            try:
                driver.get(parm1)
            except Exception as e:
                print(e)
                screenshot2file(driver)
                logging.error('%: % False', beheaver1, parm1)
                logging.error('%s: %s - %s' % beheaver1, parm1, e)
                return False, beheaver1, parm1
            else:
                screenshot2file(driver)
                logging.error('%s: %s Success' % beheaver1, parm1)
        else:
            screenshot2file(driver)
            logging.error('%s: %s Success' % beheaver, parm)
            return True, beheaver, parm
    elif beheaver == 'clickXpath':
        try:
            driver.find_element_by_xpath(parm)
        except Exception as e:
            screenshot2file(driver)
            logging.error('%s: %s False' % beheaver, parm)
            print(e)
            logging.error('%s: %s - %s' % beheaver, parm, e)
            print(e)
            try:
                driver.find_element_by_xpath(parm1)
            except Exception as e:
                screenshot2file(driver)
                logging.error('%s: %s False' % beheaver1, parm1)
                print(e)
                logging.error('%s: %s - %s' % beheaver1, parm1, e)
                print(e)
                return False
            else:
                driver.find_element_by_xpath(parm1).click()
                time.sleep(1)
                screenshot2file(driver)
                logging.error('%s: %s Success' % beheaver1, parm1)
        else:
            driver.find_element_by_xpath(parm).click()
            time.sleep(1)
            screenshot2file(driver)
            logging.error('%s: %s Success' % beheaver, parm)
'''