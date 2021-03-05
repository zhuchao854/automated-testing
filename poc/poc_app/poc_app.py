# coding=utf-8
from appium import webdriver
from time import sleep
from base.base_page import BasePage
from base.box_driver import BoxDriver,BoxBrowser


desired_caps={}
desired_caps['deviceName']='emulator-5554'
desired_caps['platformName']='Android'
desired_caps['platformVersion']= '6.0.1'
desired_caps["noReset"]= False #是否保留 session 信息，可以避免重新登录
desired_caps['newCommandTimeout']='8000' #等待新指令时间，过了时间自动退出app
desired_caps['appPackage']='com.guangqi.dmo.ecard'
desired_caps['appActivity']='com.jiatui.poc.SplashActivity'
desired_caps['dontStopAppOnReset'] = True  # 不关闭应用
desired_caps['autoGrantPermissions'] = True  # 自动获取权限
# desired_caps['app']='/Users/imac/Downloads/app-dmoaliInt-release.apk' #安装app
desired_caps['noSign']='true'  #设置来避免重签名
# desired_caps['unicodeKeyboard']=True  # 此两行是为了解决字符输入不正确的问题,使用 unicodeKeyboard 的编码方式来发送字符串
# desired_caps['resetKeyboard']=True  # 运行完成后重置软键盘的状态,将键盘给隐藏起来




class POC_ANDROID(BasePage):

    def login(self):
        '''
        登录poc
        :return:
        '''
        dr = self.base_driver
        dr.type_wait('x,//*[@text="请输入手机号"]', '18571495040')
        dr.type_wait('id,com.guangqi.dmo.ecard:id/phone_code', 1111)
        dr.click('x,//*[@text="获取验证码"]')
        dr.click('x,//*[@text="登录"]')

    def xuanchuance(self):
        '''
        企业宣传册分享流程
        :return:
        '''
        dr = self.base_driver
        dr.click_wait('x,//*[contains(@text,"企业宣传册")]')
        dr.click_wait('x,//android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
        dr.click_wait('x,//*[contains(@text,"分享")]')
        dr.click_wait('x,//*[@text="微信好友"]')

    def aaa(self):
        '''
        调用微信程序，打开与超O_o的微信聊天界面
        :return:
        '''
        dr = self.base_driver
        dr._base_driver.start_activity('com.tencent.mm','.ui.LauncherUI')
        sleep(6)
        # dr.quit()
        dr.click_wait('x,//*[@text="超O_o"]')
        # dr.click_wait('x,//android.widget.ImageView[@content-desc="超O_o头像"][last()]/../../android.widget.LinearLayout/android.widget.LinearLayout')
        # sleep(18)
        # print(dr._base_driver.context)
        # contexts = dr._base_driver.context
        # dr._base_driver.switch_to.context(contexts)
        # dr.click_wait('x,//android.view.View[@content-desc="商城"]',20)
        # dr.click_wait('x,//android.view.View[@content-desc="测试1"]',10)
        # sleep(2)
        # dr._base_driver.activate_app('com.guangqi.dmo.ecard')
        # sleep(6)
        # print(dr._base_driver.current_context)
        # dr._base_driver.switch_to.context(contexts)
        # dr.click_wait('x,//*[contains(@text,"企业宣传册")]',10)
        # dr.quit()

    def wexinsend(self):
        dr = self.base_driver
        dr.click('x,//*[@text="文件传输助手"]')
        sleep(2)
        dr.click('id,com.tencent.mm:id/doz')
        sleep(2)
        dr.click('id,com.tencent.mm:id/dom')
        sleep(2)
        dr.click('x,//*[@text="取消"]')
        dr.click('x,//android.widget.RelativeLayout[last()]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout')
        sleep(2)

if __name__ == '__main__':

    dr = POC_ANDROID(BoxDriver(BoxBrowser.APP,desired_caps=desired_caps))
    sleep(6)
    dr.base_driver.implicitly_wait(3)
    dr.aaa()
    dr.base_driver._base_driver.activate_app('com.guangqi.dmo.ecard')
    sleep(5)
    dr.login()
    dr.base_driver._base_driver.activate_app('com.tencent.mm')