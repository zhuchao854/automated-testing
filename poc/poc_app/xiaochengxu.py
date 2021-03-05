# coding=utf-8
from time import sleep

from base.base_page import BasePage
from base.box_driver import BoxDriver, BoxBrowser

desired_caps = dict()
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps["noReset"] = True  # 是否保留 session 信息，可以避免重新登录
desired_caps['newCommandTimeout'] = '150000'  # 等待新指令时间，过了时间自动退出app
desired_caps["automationName"] = "UiAutomator2"
# desired_caps['appPackage'] = 'com.tencent.mm'
# desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['appPackage'] = 'com.p3group.bmw'
desired_caps['appActivity'] = '.page.aftersales.splash.SplashActivity'

dr = BoxDriver(BoxBrowser.APP,desired_caps=desired_caps)
dr.long_click('id,com.p3group.bmw:id/public_toolbar_back')
print(1)


# # 点击文件传输助手
# dr.click_wait('x,//*[@text="文件传输助手"]')
# # 点击小程序名片。进入小程序
# dr.click_wait('x,//android.widget.RelativeLayout[last()]/android.widget.LinearLayout/android.widget.LinearLayout')
# print(dr._base_driver.context)
# sleep(20)
# dr.tap_click((425,645),(810,1440))
# dr.click_wait('x,//android.view.View[@content-desc="交换联系方式"]')
# sleep(5)
dr.tap_click((552,1341),(810,1440))


# #点击同意测试协议
# dr.click_wait('x,//android.webkit.WebView[@content-desc="wx26ffca0c0c8066c4:pages/tabbar/card/card.html:VISIBLE"]/android.widget.Image[1]')
# dr.click_wait('x,//android.view.View[@content-desc="同意"]')
# #点击同意测试协议
