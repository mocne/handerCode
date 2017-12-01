# -*- coding: utf-8 -*-

import time
from DriverInit import initAppiumDriver

def change2app(driver, package, activity):
    driver.quit()
    driver = initAppiumDriver.initAppiumWithInfo(package=package, activity=activity)
    time.sleep(10)
    driver.get_screenshot_as_file('./img/%s.png' % time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time())))
    time.sleep(3)