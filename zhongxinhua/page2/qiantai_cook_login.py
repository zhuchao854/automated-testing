from base.base_page import BasePage
from base.box_driver import BoxDriver,BoxBrowser
from time import sleep

class ZXG_QianTai(BasePage):

    COOKIE = {'httpOnly': False, 'name': 'JSESSIONID', 'secure': False, 'value': '9AAA05E6B96B6418AAD37F274CDD9242'}
    MENU = '— 在线下单'

    def zxh_login(self):
        dr = self.base_driver
        dr.maximize_window()
        dr.clear_cookies()
        dr.navigate("http://www.zxhgroup.com:8069/home/login.html")
        sleep(2)
        dr.add_cookie(self.COOKIE)
        sleep(1)
        dr.refresh()
        sleep(1)
        dr.click('x,//*[@id="yet_login"]/ul/li[3]/table/tbody/tr/td[1]/input')
        sleep(2)
        dr.click('x,//*[@id="pcbOrder"]/table/tbody/tr[3]/td/a')
        sleep(0.5)
        dr.switch_to_frame('i,client_context_frame')
        dr.type('i,length','1')
        dr.type('i,width', '1')
        dr.click('i,makeupDataSource1')
        dr.type('i,makeupLen','1')
        dr.type('i,makeupWid', '1')
        # 板子层数
        dr.click('i,board_layer_number_2')
        # 板子数量
        dr.click('i,stencil_Counts')
        sleep(10)
        print(9)
        dr.click('id,countNumer200')
        print(99)
        dr.click('x,//*[@id="board_number"]/div[1]/div[1]/ur[1]/li[6]/table/tbody/tr/td[1]/input[1]')
        # 焊盘喷镀
        dr.click('i,sprayStannum1')
        # 最小线宽线距
        dr.click('i,threadWide1')
        # 字符颜色
        dr.click('i,faceChar5')
        # 特殊工艺
        dr.click('i,halfHole')
        # 出货要求
        dr.click('i,charMarkReport')
        # 印周期
        dr.click('i,printPeriod1')
        # 需要发票
        dr.click('i,invoice1')
        dr.click('x,//*[@id="allProjectFrom"]/div[2]/table/tbody/tr/td/input')



if __name__ == '__main__':
    a = BoxDriver(BoxBrowser.Ie)
    b = ZXG_QianTai(a)
    b.zxh_login()
