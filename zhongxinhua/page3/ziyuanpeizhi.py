from base.box_driver import BoxDriver,BoxBrowser
from datetime import datetime
from datetime import timedelta
from time import sleep
import time
from zhongxinhua.page2.zxh_commad1 import ZXH_COMMAD_LIUCHENG
import csv

class ziyuan(ZXH_COMMAD_LIUCHENG):

    def vvv(self,path):
        dr = self.base_driver
        dr.type('x,//*[@placeholder="请输入搜索内容"]','资源链接')
        dr.click('x,//*[@id="app"]/div/div[1]/div[3]/div/ul[2]/div/li/ul/li')
        sleep(1)
        with open(path,mode='r',encoding='utf8') as f:
            configdata = csv.reader(f)
            for ziyuanname,ziyuanurl,pageid,ziyuanzu in configdata:
                if 'ziyuanname' in ziyuanname:
                    continue
                dr.switch_to_frame('id,iframeEle')
                dr.click('x,//*[@id="allProjectFrom"]/table/tbody/tr/td/div/table[1]/tbody/tr/td[2]/input[3]')
                dr.type('x,//*[@id="name"]',ziyuanname)#资源名称
                dr.type('x,//*[@id="RescManageAction_rescVO_resString"]',ziyuanurl)#资源url
                dr.type('x,//*[@id="RescManageAction_rescVO_pageId"]',pageid)#pageid
                dr.select_by_value('x,//*[@id="categoryCode"]','pcb')
                dr.select_by_visible_text('x,//*[@id="rescGroupId"]',ziyuanzu)#选择资源组
                dr.click('x,//*[@id="RescManageAction"]/table/tbody/tr/td/div/table[1]/tbody/tr/td[2]/input[1]')#保存
                dr.switch_to_default()
                sleep(2)


if __name__ == '__main__':
    dr = ziyuan(BoxDriver(BoxBrowser.Chrome))
    dr.login_zxh({'user': 'jlsdev', 'pwd': 'jls123'})
    dr.vvv('..\\data\\ziyuanpeizhi.csv')