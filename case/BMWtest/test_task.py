import unittest
import time
from time import sleep
from poc.poc_app.bmw_app import BMW_APP_2_task
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
        self.dr = BMW_APP_2_task(BoxDriver(BoxBrowser.APP, desired_caps=desired_caps))
        self.dr.huokezhongxin()

    def tearDown(self):
        today = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.dr.base_driver.save_window_snapshot('../..//screenshot/%s.png'%today)
        print(self.text)
        self.dr.base_driver.quit()

    def test0_huokehaibao(self):
        self.dr.new_task()
        self.dr.edit_task(content='测试获客海报', type='获客海报', username='南总')
        self.dr.finish_task('获客海报')
        self.dr.wexin()
        self.dr.base_driver.back()
        self.dr.base_driver.back()
        sleep(2)
        self.dr.base_driver.swipdown(1000, 1)
        sleep(2)
        self.text = self.dr.base_driver.get_attribute('id,com.p3group.bmw:id/status_tv','text')

    def test1_huokevideo(self):
        self.dr.new_task()
        self.dr.edit_task(content='测试视频', type='视频', username='南总')
        self.dr.finish_task('视频')
        self.dr.wexin()
        self.dr.base_driver.back()
        self.dr.base_driver.back()
        sleep(2)
        self.dr.base_driver.swipdown(1000, 1)
        sleep(2)
        self.text = self.dr.base_driver.get_attribute('id,com.p3group.bmw:id/status_tv','text')

    def test2_huokewenzhang(self):
        self.dr.new_task()
        self.dr.edit_task(content='测试获客文章', type='获客文章', username='南总')
        self.dr.finish_task('获客文章')
        self.dr.wexin()
        self.dr.base_driver.back()
        self.dr.base_driver.back()
        sleep(2)
        self.dr.base_driver.swipdown(1000, 1)
        sleep(2)
        self.text = self.dr.base_driver.get_attribute('id,com.p3group.bmw:id/status_tv', 'text')

    def test3_moments_material(self):
        self.dr.new_task()
        self.dr.edit_task(content='测试朋友圈素材', type='朋友圈素材', username='南总')
        self.dr.finish_task('朋友圈素材')
        self.dr.wexin()
        self.dr.base_driver.back()
        sleep(2)
        self.dr.base_driver.swipdown(1000, 1)
        sleep(2)
        self.text = self.dr.base_driver.get_attribute('id,com.p3group.bmw:id/status_tv', 'text')

    def test4_brochure(self):
        self.dr.new_task()
        self.dr.edit_task(content='测试企业宣传册', type='企业宣传册', username='南总')
        self.dr.finish_task('企业宣传册')
        self.dr.wexin()
        self.dr.base_driver.back()
        self.dr.base_driver.back()
        sleep(2)
        self.dr.base_driver.swipdown(1000, 1)
        sleep(2)
        self.text = self.dr.base_driver.get_attribute('id,com.p3group.bmw:id/status_tv', 'text')

    def test5_activity_library(self):
        self.dr.new_task()
        self.dr.edit_task(content='测试案例', type='案例', username='南总')
        self.dr.finish_task('案例')
        self.dr.wexin()
        self.dr.base_driver.back()
        self.dr.base_driver.back()
        sleep(2)
        self.dr.base_driver.swipdown(1000, 1)
        sleep(2)
        self.text = self.dr.base_driver.get_attribute('id,com.p3group.bmw:id/status_tv', 'text')

    def test6_activity_form(self):
        self.dr.new_task()
        self.dr.edit_task(content='测试活动表单', type='活动表单', username='南总')
        self.dr.finish_task('活动表单')
        self.dr.wexin()
        self.dr.base_driver.back()
        self.dr.base_driver.back()
        sleep(2)
        self.dr.base_driver.swipdown(1000, 1)
        sleep(2)
        self.text = self.dr.base_driver.get_attribute('id,com.p3group.bmw:id/status_tv', 'text')

    def test7_commodity(self):
        self.dr.new_task()
        self.dr.edit_task(content='测试商品', type='商品', username='南总')
        self.dr.finish_task('商品')
        self.dr.wexin()
        self.dr.base_driver.back()
        self.dr.base_driver.back()
        sleep(2)
        self.dr.base_driver.swipdown(1000, 1)
        sleep(2)
        self.text = self.dr.base_driver.get_attribute('id,com.p3group.bmw:id/status_tv', 'text')
