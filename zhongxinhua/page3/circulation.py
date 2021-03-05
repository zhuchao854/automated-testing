from base.box_driver import BoxDriver,BoxBrowser
from zhongxinhua.page2.zxh_commad1 import ZXH_COMMAD_LIUCHENG
import traceback
from time import sleep
URL = 'https://test.zxhwork.com/#/login'
URL_SUESS = 'https://test.zxhwork.com/#/desktopAction.action'

class CIRCULATION(ZXH_COMMAD_LIUCHENG):
    def login_zxh_zhengshi(self,data,handle=None):
        dr = self.base_driver
        dr.maximize_window()
        dr.navigate(URL)
        url = ''
        log = 0
        while URL_SUESS not in url:
            log += 1
            if log > 1:
                print('登录失败，正在尝试第%s次登录'%str(log))
            dr.type('x,//*[@placeholder="用户名"]', data['user'])
            # input('请输入验证码，然后进入控制台按回车键继续')
            dr.type('x,//*[@placeholder="密码"]', data['pwd'])
            dr.open_new_window('x,//span[text()="登录"]')
            sleep(1)
            url = dr.get_url()
        sleep(1)
        if handle is None:
            dr.remove_window()
        else:
            dr.remove_window(handle)
    def zxh(self,data):
        dr = self.base_driver
        self.login_zxh_zhengshi(data)
        qq = []
        for li in range(1,100):
            try:
                dr.click('x,//*[@theme="dark"]/div[%s]'%li)
                for sonli in range(1,100):
                    try:
                        dr.click('x,//*[@theme="dark"]/div[%s]//ul[@role="menu"]/li[%s]'%(li,sonli))
                        ww = dr.get_url()
                        qq.append(ww)
                    except:break
            except:print('主菜单已无数据')
        print(qq)

if __name__ == '__main__':
    data = {'user': 'jlsdev', 'pwd': 'jls123'}
    q = CIRCULATION(BoxDriver(BoxBrowser.Chrome))
    q.zxh(data)