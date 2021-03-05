# coding=utf-8
from time import sleep
from base.base_page import BasePage
from base.box_driver import BoxDriver,BoxBrowser

class YunYing(BasePage):

    def login(self,user='zhuchao',pwd='123456'):
        """
        登录运营
        :param user:
        :param pwd:
        :return:
        """
        dr = self.base_driver
        dr.maximize_window()
        dr.navigate('https://poc-dev-bob.aijiatui.com/')
        dr.type('x,//*[@id="userName"]',user)
        dr.types('x,//*[@id="password"]',pwd)
        sleep(2)

    def list_click(self):
        """
        遍历所有菜单
        :return:
        """
        dr = self.base_driver
        #获取主菜单的数量
        numbers_em = dr.count_elements('x,//*[@id="root"]//li[@class="ant-menu-submenu ant-menu-submenu-inline"]')
        for i in range(numbers_em):
            sleep(1)
            #遍历点击主菜单
            dr.click_wait('x,//*[@id="root"]/div/section/aside/div/ul/li[%s]'%str(i+2))
            #获取次级菜单的数量
            numbers_cd = dr.count_elements('x,//*[@id="root"]/div/section/aside/div/ul/li[%s]//li[@class="ant-menu-item"]'%str(i+2))
            #遍历点击次级菜单
            for n in range(numbers_cd):
                sleep(1)
                dr.click_wait('x,//*[@id="root"]/div/section/aside/div/ul/li[%s]/ul/li[%s]'%(str(i+2),str(n+1)))

if __name__ == '__main__':
    dr = YunYing(BoxDriver(BoxBrowser.Chrome))
    dr.login()
    dr.list_click()

