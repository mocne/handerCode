# -*- coding: utf-8 -*-
import time
import os
from appium import webdriver
import platform
import common.readYaml
import common.doSomethingWithElement

def start2test(appName):
    driver = initAppiumWithInfo(appName)
    time.sleep(5)
    el = driver.find_element_by_android_uiautomator("new UiSelector().text('追书社区')")
    el.click()

def initAppiumWithInfo(appName):

    dir = os.path.dirname(os.getcwd())
    app = appName + '.apk'
    # commandStr = 'aapt dump badging ' + dir + '\\app\\' + app
    #
    # info = os.popen(commandStr).read()
    # pnN = info.find('versionCode=')
    # packageName = info[15:pnN-2]
    apps = common.readYaml.getYam('../YAML/appInfo.yml')
    appPackage = apps[appName]['PackageName']
    appActivity = apps[appName]['LanchableActivity']

    # os.system('adb uninstall ' + appPackage)
    # os.system('adb install ' + dir + '\\app\\' + app)

    deviceSystemVersion = os.popen('adb shell getprop ro.build.version.release').read().strip().split('*')[-1]
    tmp = deviceSystemVersion.split('.')
    if len(tmp) > 2:
        bigV = float(tmp[0] + '.' + tmp[1])
        if bigV < 4.4:
            automationName = 'Selendroid'
        else:
            automationName = 'Appium'

    deviceName = os.popen('adb get-serialno').read().strip()


    desired_caps = {
        'platformName': 'Android',
        'platformVersion': deviceSystemVersion,
        'deviceName': deviceName,
        # 'udid': '',                                     # 连接的物理设备的唯一设备标识,Android可以不设置
        # 'app': '',
        'appPackage': appPackage,
        'appActivity': appActivity,
        'appWaitActivity': appActivity,                          # 你想要等待启动的Android Activity名称
        'newCommandTimeout': 300,
        # 'browserName': '',
        'automationName': 'appium',                     # 你想使用的自动化测试引擎：Appium (默认) 或 Selendroid(4.4以下可使用)
        'unicodeKeyboard': 'True',                      # 支持中文输入，会自动安装Unicode 输入法。默认值为 false
        "resetKeyboard": "True",                        # 在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态
        'noReset': True,
        'noSign': True
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps, browser_profile=None, proxy=None, keep_alive=True)
    time.sleep(5)
    print('************************ start **************************')
    driver.find_element_by_android_uiautomator('new')
    return driver

def kill_appium():
    if platform.system() == 'Darwin':      # Mac 操作系统
        os.popen('lsof -n -i:4723 | grep LISTEN | awk \'{print $2}\' | xargs kill')
        os.popen('ps -A | grep node | grep -v grep | awk \'NR=1 {print $1}\' | xargs kill -9')
    elif platform.system() == 'Windows':     # Windows操作系统
        os.system('taskkill /f /fi "imagename eq node.exe"')

def start_appium():
    os.system('appium --address 127.0.0.1 --port 4723 --bootstrap-port 4725 --session-override --no-reset')

'''# 下拉刷新20次
for i in range(0, 20):
    time.sleep(2)
    driver.swipe(500, 700, 500, 1500, 500)


 #淘宝领金币
el = driver.find_element_by_android_uiautomator('new UiSelector().description("领金币")')
el.click()
time.sleep(5)
el1 = driver.find_element_by_android_uiautomator('new UiSelector().description("\\u70B9\\u51FB\\u5F00\\u5B9D\\u7BB1\\u9886\\u91D1\\u5E01")')
el1.click()

'# 点击搜索
time.sleep(3)
elF = findAUByID(driver, 'com.taobao.taobao:id/home_searchedit')
inputText(elF, 'web')


driver.HideKeyboard();//隐藏键盘
driver.BackgroundApp(60);//60秒后把当前应用放到后台去
driver.LockDevice(3); //锁定屏幕

//在当前应用中打开一个 activity 或者启动一个新应用并打开一个 activity
driver.StartActivity("com.iwobanas.screenrecorder.pro", "com.iwobanas.screenrecorder.RecorderActivity");
driver.OpenNotifications();//打开下拉通知栏 只能在 Android 上使用
driver.IsAppInstalled("com.example.android.apis-");//检查应用是否已经安装
driver.InstallApp("path/to/my.apk");//安装应用到设备中去
driver.RemoveApp("com.example.android.apis");//从设备中删除一个应用
driver.ShakeDevice();//模拟设备摇晃
driver.CloseApp();//关闭应用
driver.LaunchApp();//根据服务关键字 (desired capabilities) 启动会话 (session) 。请注意这必须在设定 autoLaunch=false 关键字时才能生效。这不是用于启动指定的 app/activities
driver.ResetApp();//应用重置
driver.GetContexts();//列出所有的可用上下文
driver.GetContext();//列出当前上下文
driver.SetContext("name");//将上下文切换到默认上下文
driver.GetAppStrings();//获取应用的字符串
driver.KeyEvent(176);//给设备发送一个按键事件:keycode
driver.GetCurrentActivity();//获取当前 activity。只能在 Android 上使用
//driver.Pinch(25, 25);//捏屏幕 (双指往内移动来缩小屏幕)
//driver.Zoom(100, 200);//放大屏幕 (双指往外移动来放大屏幕)
driver.PullFile("Library/AddressBook/AddressBook.sqlitedb");//从设备中拉出文件
driver.PushFile("/data/local/tmp/file.txt", "some data for the file");//推送文件到设备中去

driver.FindElement(By.Name(""));
driver.FindElementById("id");
driver.FindElementByName("text");
driver.FindElementByXPath("//*[@name='62']");


driver.KeyEvent(3); //KEYCODE_HOME 按键Home 3
driver.KeyEvent(26);  //KEYCODE_POWER 电源键 26
driver.KeyEvent(67);  //KEYCODE_DEL 退格键 67
driver.KeyEvent(66);  //KEYCODE_ENTER 回车键
driver.KeyEvent(122); //KEYCODE_MOVE_HOME 光标移动到开始
driver.KeyEvent(123); //KEYCODE_MOVE_END 光标移动到末尾

double Screen_X = driver.Manage().Window.Size.Width;//获取手机屏幕宽度
double Screen_Y = driver.Manage().Window.Size.Height;//获取手机屏幕高度
double startX = element.Location.X; //获取元素的起点坐标，即元素最左上角点的横坐标
double startY = element.Location.Y; //获取元素的起点坐标，即元素最左上角点的纵坐标
double elementWidth = element.Size.Width;  //获取元素的宽度
double elementHight = element.Size.Height; //获取元素的宽度
'''

if __name__ == '__main__':
    # kill_appium()
    # start_appium()
    start2test('zhuishushenqi')
