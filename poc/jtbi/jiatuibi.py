# coding=utf-8
from appium import webdriver
from time import sleep
from base.base_page import BasePage
from base.box_driver import BoxDriver,BoxBrowser


desired_caps={}
desired_caps['deviceName']='emulator-5554'
desired_caps['platformName']='Android'
desired_caps['platformVersion']= '6.0.1'
desired_caps["noReset"]= True #是否保留 session 信息，可以避免重新登录
desired_caps['newCommandTimeout']='8000' #等待新指令时间，过了时间自动退出app
desired_caps['appPackage']='com.jiatui.app.radar'
desired_caps['appActivity']='com.jiatui.radar.mvp.ui.activity.SplashActivity'
desired_caps['dontStopAppOnReset'] = True  # 不关闭应用
desired_caps['autoGrantPermissions'] = True  # 自动获取权限
desired_caps["automationName"] = "UiAutomator2"
# desired_caps['app']='/Users/imac/Downloads/app-dmoaliInt-release.apk' #安装app
desired_caps['noSign']='true'  #设置来避免重签名
# desired_caps['unicodeKeyboard']=True  # 此两行是为了解决字符输入不正确的问题,使用 unicodeKeyboard 的编码方式来发送字符串
# desired_caps['resetKeyboard']=True  # 运行完成后重置软键盘的状态,将键盘给隐藏起来

a = BoxDriver(BoxBrowser.APP, desired_caps=desired_caps)
a.click_wait2('x,//android.view.View[@content-desc="稍后完善"]')

def wexin(dimingpian=None):
    """
    微信分享操作
    :return:
    """
    sleep(3)
    if  dimingpian in ['di_ming_pian','shang_pin','peng_you_quan']:
        a.click('x,//*[@text="微信好友"]')
    else:
        a.click('x,//*[@content-desc="微信好友"]')
    sleep(3)
    a.explicitly_wait('x,//*[@text="文件传输助手"]',15)
    a.back()
    # a.click_wait2('x,//*[@text="文件传输助手"]', 20)
    # a.click_wait2('id,com.tencent.mm:id/doz')
    # a.click_wait2('id,com.tencent.mm:id/dom')
    bb = ''
    for i in range(10):
        sleep(0.5)
        try:
            try:
                bb = a.get_attribute('x,//*[contains(@content-desc,"推广币")]','content-desc')
            except:
                a._locate_element('x,//*[@text="分享勋章"]')
                a.tap_click([404, 1245], [810, 1440])
                bb = '0'
            break
        except:
            pass
    sleep(3)
    try:
        a.click('x,//*[@text="取消"]')
    except:
        pass
    print(bb)
    if bb == '':
        cc = False
    else:
        cc = True
    return cc

def di_ming_pian():
    a.click_wait2('x,//*[@content-desc="递名片"]')
    a.click_wait2('x,//*[@text="递名片"]')

def xuan_chuan_ce():
    a.click_wait2('x,//*[@content-desc="宣传册"]')
    a.click_wait2('x,//*[contains(@content-desc,"立即分享")]')

def an_li_ku():
    a.click_wait2('x,//*[@content-desc="案例库"]')
    a.click_wait2('x,//android.view.View[@content-desc="分享案例"]')

def shang_pin():
    a.click_wait2('x,//*[@content-desc="商品"]')
    a.click_wait2('x,//*[contains(@text,"立即分享")]')

def wen_ku():
    '''
    后退两次到主页面
    :return:
    '''
    a.click_wait2('x,//*[@content-desc="文库"]')
    a.click_wait2('x,//*[contains(@content-desc,"立即分享")]')
    a.click_wait2('x,//*[contains(@content-desc,"立即分享")]')

def haibao2():
    for i in range(10):
        try:
            a.click_wait2('x,//android.view.View[@content-desc="生成海报"]')
            sleep(2)
            res = a.get_displayed('x,//*[@content-desc="微信好友"]')
        except:
            res = False
        if res is True:
            break

def haibao():
    '''
    后退两次到主页面
    :return:
    '''
    a.click_wait2('x,//*[@content-desc="海报"]')
    a.click_wait2('x,//android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.FrameLayout')
    haibao2()

def shi_pin():
    '''
    后退两次到主页面
    :return:
    '''
    a.click_wait2('x,//*[@content-desc="视频"]')
    #选择第一条数据
    a.click_wait2('x,//android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout')
    a.click_wait2('x,//*[contains(@text,"立即分享")]')

def peng_you_quan():
    a.click_wait2('x,//*[@content-desc="朋友圈素材"]')
    a.click_wait2('x,//*[contains(@content-desc,"立即分享")]')

def wen_juan():
    a.click_wait2('x,//*[@content-desc="问卷"]')
    a.click_wait2('x,//*[contains(@content-desc,"立即分享")]')

def kk(q):
    '''
    配置每个内容的重复分享的按钮
    :param q: 分装类的名称，用作自动判断使用分享的按钮
    :return:
    '''
    sleep(3)
    if q.__name__ in ['shi_pin','shang_pin']:
        a.click('x,//*[contains(@text,"立即分享")]')
    elif q.__name__ == 'haibao':
        haibao2()
    elif q.__name__ == 'an_li_ku':
        a.click('x,//android.view.View[@content-desc="分享案例"]')
    elif q.__name__ == 'di_ming_pian':
        a.click('x,//*[@text="递名片"]')
    else:
        a.click('x,//*[contains(@content-desc,"立即分享")]')

def uu(q,p):
    q()
    print(q.__name__)
    for i in range(10):
        b = wexin(q.__name__)
        if b is False:
            for i in range(p):
                a.back()
                sleep(3)
            try:
                a.click('x,//android.view.View[@content-desc="稍后完善"]')
            except:
                pass
            break
        else:
            kk(q)

w = [(di_ming_pian, 1),(xuan_chuan_ce, 1),(an_li_ku, 1),(shang_pin, 1),(wen_ku, 2),(haibao, 2),(shi_pin, 2),(wen_juan, 1)]

for u,t in w:
    uu(u,t)


# a.click_wait2('x,//*[@content-desc="稍后完善"]')
# a.click_wait2('x,//*[@content-desc="递名片"]')
# a.click_wait2('id,com.jiatui.app.radar:id/tv_wechat')