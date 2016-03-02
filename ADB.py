import os
import re


def getDevice():
    print("getDevice >>>")
    output = os.popen('./adb/adb devices')
    shell_devices = output.read()
    print(shell_devices)

    shell_devices = shell_devices.replace("\tdevice", "").replace("List of devices attached", "").replace(" ", "")
    shell_devices = re.compile(r'(\n){2,}').sub("", shell_devices)
    devices = shell_devices.split("\n")

    for x in devices:
        if not len(x):
            devices.remove(x)

    print("getDevice <<<")
    return devices


def killServer():
    print("killServer >>>")
    output = os.popen('./adb/adb kill-server')
    shell = output.read()
    print(shell)
    print("killServer <<<")
    return shell


def startServer():
    print("startServer >>>")
    output = os.popen('./adb/adb start-server')
    shell = output.read()
    print(shell)
    print("startServer <<<")
    return shell


def startTesting(device):
    print("startTesting >>>")
    output = os.popen(
        "./adb/adb -s " + device + " shell am instrument -w OpenGamePad.Support.Library/android.support.test.runner.AndroidJUnitRunner")
    shell = output.read()
    print(shell)
    print("startTesting <<<")
    return shell


def startHelperApp(device, info):
    print("startHelperApp >>>")
    output = os.popen("./adb/adb -s " + device + " shell am start -n cn.gavinliu.open.gamepad.helper/.ui.MainActivity")
    shell = output.read()
    print(shell)
    print("startHelperApp <<<")

    info.setText("请在手机上编辑映射规则，后点击[获取映射列表]")
    return shell


def startForward(device, port, remote):
    print("startForward >>>")
    output = os.popen("./adb/adb -s " + device + " forward tcp:" + port + " tcp:" + remote)
    shell = output.read()
    print(shell)
    print("startForward <<<")
    return shell


def checkAPK(device, info):
    print("checkAPK >>>")

    output = os.popen("./adb/adb -s " + device + " shell pm list instrumentation")
    shell = output.read()
    index = shell.find("OpenGamePad.Support.Library")
    if index == -1:
        info.setText("检测到没有安装OpenGpad-Support，正在安装...")
        install(device, "apk/OpenGpad-Support-androidTest.apk")

    output = os.popen("./adb/adb -s " + device + " shell pm list package")
    shell = output.read()
    index = shell.find("cn.gavinliu.open.gamepad.support")
    if index == -1:
        info.setText("检测到没有安装OpenGpad-Support，正在安装...")
        install(device, "apk/OpenGpad-Support.apk")

    index = shell.find("cn.gavinliu.open.gamepad.helper")
    if index == -1:
        info.setText("检测到没有安装OpenGpad-Helper，正在安装...")
        install(device, "apk/OpenGpad-Helper.apk")

    print("checkAPK <<<")

def install(device, apk):
    print("install >>>")
    output = os.popen("./adb/adb -s " + device + " install " + apk)
    shell = output.read()
    print(shell)
    print("install <<<")
    return shell


def getAppListCMD(device):
    return "./adb/adb -s " + device + " shell pm list package"


def getTestListCMD(device):
    return "./adb/adb -s " + device + " shell pm list instrumentation"
