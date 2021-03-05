import unittest
from poc.poc_app.bmw_app import BMW_APP_1
from base.box_driver import BoxDriver,BoxBrowser

class test_share(unittest.TestCase):

    def setUp(self):
        desired_caps = dict()
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps["noReset"] = True  # 是否保留 session 信息，可以避免重新登录
        desired_caps['newCommandTimeout'] = '15000'  # 等待新指令时间，过了时间自动退出app
        desired_caps['appPackage'] = 'com.p3group.bmw'
        desired_caps['appActivity'] = '.page.aftersales.splash.SplashActivity'
        self.dr = BMW_APP_1(BoxDriver(BoxBrowser.APP, desired_caps=desired_caps))
        self.dr.huokezhongxin()

    def tearDown(self):
        self.dr.base_driver.quit()

    def test0_huokehaibao(self):
        self.dr.huokehaibao()
        self.dr.wexin()

    def test1_huokevideo(self):
        self.dr.huokevideo()
        self.dr.wexin()

    def test2_huokewenzhang(self):
        self.dr.huokewenzhang()
        self.dr.wexin()

    def test3_moments_material(self):
        self.dr.moments_material()
        self.dr.wexin()

    def test4_brochure(self):
        self.dr.brochure()
        self.dr.wexin()

    def test5_activity_library(self):
        self.dr.activity_library()
        self.dr.wexin()

    def test6_activity_form(self):
        self.dr.activity_form()
        self.dr.wexin()

    def test7_business_card(self):
        self.dr.business_card()
        self.dr.wexin()
