# coding=utf-8
from time import sleep
from base.base_page import BasePage
from base.box_driver import BoxDriver,BoxBrowser

from zhongxinhua.page2.HtmlHandler import HtmlHandler
import requests




class QiGuan(BasePage):

    def login_token(self):
        body = dict()
        body['account'] = '18718282711'
        body['accountId'] = '755023659898241024'
        body['companyId'] = '755023659814354944'

        data = dict()
        data['url'] = 'https://poc-dev.aijiatui.com/arch-login-center/corp/check'
        data['method'] = 'post'
        data['body'] = body
        data['type'] = 'json'
        data['headers'] = None
        data['params'] = None

        r = requests.session()
        a = r.request(method=data['method'],
                  url=data['url'],
                  params=data['params'],
                  headers=data['headers'],
                  data=data['body'],
                  verify=False)
        import re

        b = a.content.decode("utf-8")
        self.token = re.findall(r"""token":"(.*?)"}""",str(b))[0]

    def login1(self):
        """
        登录企管
        :param user:
        :param pwd:
        :return:
        """
        dr = self.base_driver
        dr.maximize_window()
        dr.navigate('http://poc-dev.aijiatui.com/')
        dr.type('x,//*[@id="account"]','18718282711')
        dr.type('x,//*[@id="password"]','123')
        dr.click('x,/html/body/div[1]/div/div/div/button')
        sleep(1)
        a = dr.get_text('x,/html/body/div[2]/span/div/div/div')
        print(1)

    def login(self):
        """
        登录企管
        :param user:
        :param pwd:
        :return:
        """
        dr = self.base_driver
        dr.maximize_window()
        dr.navigate('http://poc-dev.aijiatui.com/')
        cookies = {'domain': 'poc-dev.aijiatui.com',
                 'httpOnly': False,
                 'name': 'i-token',
                 'path': '/',
                 'secure': False,
                 'value': self.token}
        dr.clear_cookies()
        dr.add_cookie(cookies)
        sleep(1)
        dr.refresh()
        sleep(4)
        try:
            # 尝试点击关闭'知道了'悬浮窗
            dr._base_driver.click('x,/html/body/div[2]/div/div/div/div[2]/div/div/div/button')
        except:
            pass
    def list_click(self):
        """
        遍历所有菜单
        :return:
        """
        dr = self.base_driver
        dr.click_wait('x,//span[text()="数据总览"]')
        dr.click_wait('x,//span[text()="用户画像"]')
        #获取主菜单数量
        numbers_em = dr.count_elements('x,//li[contains(@class,"ant-menu-submenu ant-menu-submenu-inline") and @role="menuitem"]')
        for i in range(1,numbers_em):
            sleep(2)
            #点击主菜单
            dr.click_wait('x,/html/body/div/div/div[1]/div[1]/ul/li[%s]'%str(i+1))
            #获取次级菜单数量和元素列表
            numbers_cd_list = dr._locate_elements('x,/html/body/div/div/div[1]/div[1]/ul/li[%s]//li[@class="ant-menu-item"]'%str(i+1))
            numbers_cd = len(numbers_cd_list)
            for n in range(numbers_cd):
                sleep(2)
                name = numbers_cd_list[n].text
                numbers_cd_list[n].click()
                sleep(1)
                try:
                    text = dr.get_text('x,/html/body/div[2]/span/div/div/div')
                    print(name+'页面错误。错误内容：',text)
                except:
                    pass

if __name__ == '__main__':
    dr = QiGuan(BoxDriver(BoxBrowser.Chrome))
    # dr.login_token()
    dr.login1()
    # dr.list_click()