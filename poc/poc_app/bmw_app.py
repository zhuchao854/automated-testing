# coding=utf-8
from time import sleep

from base.base_page import BasePage
from base.box_driver import BoxDriver, BoxBrowser

desired_caps = dict()
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps["noReset"] = True  # 是否保留 session 信息，可以避免重新登录
desired_caps['newCommandTimeout'] = '3000'  # 等待新指令时间，过了时间自动退出app
desired_caps['appPackage'] = 'com.p3group.bmw'
desired_caps['appActivity'] = '.page.aftersales.splash.SplashActivity'


# desired_caps['dontStopAppOnReset'] = True  # 不关闭应用
# desired_caps['autoGrantPermissions'] = True  # 自动获取权限
# desired_caps['app']='/Users/imac/Downloads/app-dmoaliInt-release.apk' #安装app
# desired_caps['noSign']='true'  #设置来避免重签名
# desired_caps['unicodeKeyboard']=True  # 此两行是为了解决字符输入不正确的问题,使用 unicodeKeyboard 的编码方式来发送字符串
# desired_caps['resetKeyboard']=True  # 运行完成后重置软键盘的状态,将键盘给隐藏起来


class BMW_APP_1(BasePage):

    def login(self):
        """
        BMW登录
        :return:
        """
        dr = self.base_driver
        dr.type_wait('x,//*[@text="用户名"]', 'zong.nan')
        dr.type_wait('id,com.p3group.bmw:id/login_password', '123')
        dr.click_wait('x,//*[@text="登录"]')

    def huokezhongxin(self):
        """
        获客中心
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//*[@text="获客中心"]')

    def dianzimingpian(self):
        """
        电子名片
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//*[@text="电子名片"]')

    def huokehaibao(self):
        """
        获客海报
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//*[@text="获客海报"]')
        # 点击热门类里的第一个海报
        dr.click_wait(
            'x,//*[@resource-id="com.p3group.bmw:id/hot_flag" and @text="热门海报"]/../androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[1]')
        sleep(3)
        time = 1
        while time < 5:
            sleep(1)
            try:
                dr._locate_element('x,//*[@text="点击切换二维码"]')
                print('获取成功')
                break
            except:
                print('第%s次尝试获取海报二维码失败' % str(time))
            time += 1
        # 点击生成海报按钮。
        # dr.click_wait('id,com.p3group.bmw:id/create_poster')

    def huokevideo(self):
        """
        获客视频
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//*[@text="获客视频"]')
        # dr.click_wait('x,//android.view.ViewGroup/android.widget.ImageView[1]')
        # 点击本周最热的第一个视频
        dr.click_wait('x,//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
        dr.click_wait('x,//*[@text="立即分享"]')

    def huokewenzhang(self):
        dr = self.base_driver
        dr.click_wait('x,//*[@text="获客文章"]')
        # 点击第一篇文章
        dr.explicitly_wait('id,com.p3group.bmw:id/article_item_cl', 5)
        dr._locate_elements('id,com.p3group.bmw:id/article_item_cl')[0].click()
        dr.click_wait('x,//*[@text="立即分享"]')

    def moments_material(self):
        """
        朋友圈素材
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//*[@text="朋友圈素材"]')
        dr.click_wait('x,//*[@text="推广获客"]')
        # # 朋友圈第一张照片
        # dr.click_wait('x,//android.widget.LinearLayout[1]/android.view.ViewGroup[2]/android.widget.ImageView')

    def brochure(self):
        """
        企业宣传册
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//*[@text="企业宣传册"]')
        # 宣传册第一条数据
        dr.click_wait('x,//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
        dr.click_wait('x,//*[@text="分享"]')

    def activity_library(self):
        """
        活动案例库
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//*[@text="活动案例库"]')
        # 案例库第一条数据
        dr.click_wait('x,//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]')
        dr.click_wait('x,//android.view.View[@content-desc="立即分享" and @class="android.view.View"]')

    def activity_form(self):
        """
        活动表单
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//*[@text="活动表单"]')
        # 案例库第一条数据
        dr.click_wait('id,com.p3group.bmw:id/form_item_cv')
        dr.click_wait('x,//android.view.View[@content-desc="立即分享" and @class="android.view.View"]')

    def business_card(self):
        """
        递名片
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//*[@text="递名片"]')
        dr.click_wait('x,//*[@text="分享名片"]')

    def common_back(self, mold='其他'):
        """
        返回操作
        如：文章详情返回，视频详情,递名片返回
        :return:
        """
        dr = self.base_driver
        if mold == '获客海报':
            dr.click_wait('id,com.p3group.bmw:id/close')
        elif mold == '获客视频':
            dr.click_wait('id,com.p3group.bmw:id/back_img')
        elif mold == '递名片':
            dr.click_wait('id,com.p3group.bmw:id/iv_cancel')
        else:
            try:
                dr.click_wait('id,com.p3group.bmw:id/public_toolbar_back')
            except:
                dr.click_wait('id,com.p3group.bmw:id/top_toolbar_back')

    def wexin(self):
        """
        微信分享操作
        :return:
        """
        dr = self.base_driver
        sleep(1)
        dr.click_wait('x,//*[@text="微信好友"]', 20)
        sleep(2)
        dr.click_wait('x,//*[@text="文件传输助手"]', 20)
        dr.click_wait('id,com.tencent.mm:id/doz')
        dr.click_wait('id,com.tencent.mm:id/dom')
        try:
            dr.click_wait('x,//*[@text="取消"]')
        except:
            pass


class BMW_APP_2_task(BMW_APP_1):

    def new_task(self):
        dr = self.base_driver
        dr.click_wait('id,com.p3group.bmw:id/floatButton')
        dr.click_wait('x,//*[@text="建任务"]')

    def edit_task(self, content, type, username='南总'):
        dr = self.base_driver
        dr.type_wait('x,//*[@text="请输入任务描述"]', content)
        # 点击指定推广内容
        dr.click_wait('id,com.p3group.bmw:id/add_switch_iv')
        # 点击选择推广内容
        dr.click_wait('id,com.p3group.bmw:id/choose_content')
        # 选择推荐内容
        dr.click_wait('x,//*[@text="%s"]' % type)
        if type == '获客文章':
            # 选择一篇文章
            dr.click_wait('id,com.p3group.bmw:id/article_item_cl')
        elif type == '获客海报':
            dr.click_wait('id,com.p3group.bmw:id/poster_cl')
        elif type == '企业宣传册':
            dr.click_wait('id,com.p3group.bmw:id/iv_checked')
        elif type == '商品':
            dr.click_wait('id,com.p3group.bmw:id/cb_push')
        elif type == '朋友圈素材':
            dr.click_wait('id,com.p3group.bmw:id/moments_ll')
        elif type == "案例":
            dr.click_wait('x,//*[@resource-id="com.p3group.bmw:id/rv_case"]/android.view.ViewGroup[1]')
        elif type == "活动表单":
            dr.click_wait('id,com.p3group.bmw:id/form_item_cv')
        elif type == "视频":
            dr.click_wait('id,com.p3group.bmw:id/iv_checked')
        sleep(2)
        try:
            dr.click_wait('x,//*[contains(@text,"选好了")]')
        except:
            dr.click_wait('x,//*[@text="确定"]')
        # 点击添加
        sleep(2)
        dr.swipup(1500, 1)
        sleep(1)
        dr.click_wait('id,com.p3group.bmw:id/receiver_add_tv')
        # 搜索
        dr.click_wait('id,com.p3group.bmw:id/search_bar')
        # 搜索框输入
        dr.type_wait('id,com.p3group.bmw:id/search_input', username)
        # 选中搜索人
        dr.click_wait('id,com.p3group.bmw:id/checkbox')
        # 点击确定
        dr.click_wait('id,com.p3group.bmw:id/confirm_btn')
        # 选择任务类型点击紧急
        dr.click_wait('id,com.p3group.bmw:id/ll_tap')
        # 点击选择时间
        dr.click_wait('id,com.p3group.bmw:id/urgent_tips')
        # 选中时间
        dr.click_wait('x,//*[@text="15分钟"]')
        # 点击发布
        dr.click_wait('x,//*[@text="发布"]')

    def finish_task(self, mold):
        dr = self.base_driver
        # 点击任务中心
        dr.click_wait('id,com.p3group.bmw:id/arrow')
        # 点击去完成任务
        dr.click_wait('id,com.p3group.bmw:id/to_com_tv')
        # 完成任务
        dr.click_wait('x,//*[@text="去完成任务" and @class="android.widget.TextView"]')
        # 点击分享
        sleep(3)
        if mold == '获客海报':
            dr.click('id,com.p3group.bmw:id/create_poster')  # 生成海报
        elif mold == '企业宣传册':
            dr.click('x,//*[@text="分享"]')
        elif mold in ['案例', '活动表单']:
            dr.click('x,//android.view.View[@content-desc="立即分享" and @class="android.view.View"]')
        elif mold in ['视频', '获客文章']:
            dr.click('x,//*[@text="立即分享"]')


if __name__ == '__main__':
    dr = BMW_APP_2_task(BoxDriver(BoxBrowser.APP, desired_caps=desired_caps))
    # dr.login()
    dr.huokezhongxin()
    dr.huokehaibao()
    # dr.wexin()
    # dr.common_back('获客海报')
    # dr.common_back()
    # dr.base_driver.implicitly_wait(1)
    # dr.huokevideo()
    # dr.wexin()
    # dr.common_back('获客视频')
    # dr.common_back()
    # dr.huokewenzhang()
    # dr.wexin()
    # dr.common_back('获客文章')
    # dr.common_back()
    # dr.moments_material()
    # dr.wexin()
    # dr.common_back()
    # dr.brochure()
    # dr.wexin()
    # dr.common_back()
    # dr.common_back()
    # dr.activity_library()
    # dr.wexin()
    # dr.common_back()
    # dr.common_back()
    # dr.activity_form()
    # dr.wexin()
    # dr.common_back()
    # dr.common_back()
    # dr.business_card()
    # dr.wexin()
    # dr.common_back('递名片')
    # dr.new_task()
    # dr.edit_task(content='案例',type='案例',username='南总')
    # dr.finish_task()
    # dr.wexin()
    # dr.common_back()
    # dr.common_back()
