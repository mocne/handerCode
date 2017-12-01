package com.example.tests;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class Ju {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
    baseUrl = "http://192.168.18.247:8003/credit-admin-web/admin/common/main.cgi";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testJu() throws Exception {
    driver.get(baseUrl + "/credit-admin-web/admin/common/main.cgi");
    driver.findElement(By.linkText("注销")).click();
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

  @After
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
