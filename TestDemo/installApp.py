# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import DriverInit.initAppiumDriver
import unittest


class Asdsdasdasdasdasdas(unittest.TestCase):
    def setUp(self):
        self.driver = DriverInit.initAppiumDriver.initAppiumWithInfo(appName='zhuishushenqi')

    def test_asdsdasdasdasdasdas(self):
        driver = self.driver
        driver.get("/?tn=78000241_5_hao_pg")


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            print(e)
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            print(e)
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
