package com.example.tests;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.testng.annotations.*;
import static org.testng.Assert.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class Jtn {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @BeforeClass(alwaysRun = true)
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
    baseUrl = "http://192.168.18.247:8003";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testJtn() throws Exception {
    driver.get(baseUrl + "/credit-admin-web/admin/common/main.cgi");
    driver.findElement(By.cssSelector("a.mod-arrow.mod-arrow-next")).click();
    driver.findElement(By.cssSelector("#J_gameChannel > div.box-right-bd > div.mod-slide > a.mod-arrow.mod-arrow-next")).click();
    driver.findElement(By.id("password")).clear();
    driver.findElement(By.id("password")).sendKeys("admin123");
    driver.findElement(By.cssSelector("a.mod-arrow.mod-arrow-next")).click();
    driver.findElement(By.cssSelector("#J_gameChannel > div.box-right-bd > div.mod-slide > a.mod-arrow.mod-arrow-next")).click();
    driver.findElement(By.id("captcha")).clear();
    driver.findElement(By.id("captcha")).sendKeys("8813");
    driver.findElement(By.id("login_btn")).click();
  }

  @AfterClass(alwaysRun = true)
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
