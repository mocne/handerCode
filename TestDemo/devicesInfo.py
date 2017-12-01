# -*- coding: utf-8 -*-
import os


deviceSystemVersion = os.popen('adb shell getprop ro.build.version.release').read().strip()
bigV = int(deviceSystemVersion.split('*')[-1].split('.')[0])
deviceName = os.popen('adb get-serialno').read().strip()
print(deviceName, deviceSystemVersion, bigV)