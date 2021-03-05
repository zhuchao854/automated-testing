from base.box_driver import BoxDriver,BoxBrowser
from time import sleep
import csv

class ChaoDao():

    USER = 'zhuchao'
    PWD = 'aa123456'
    BANBEN = '中信华 V43（02-21 UAT）'
    ZHIPAI = '朱超'
    STATUS = '研发完毕'
    NAME = '朱超'

    def test_chaodao_login(self):

        self.dr = BoxDriver(BoxBrowser.Chrome)
        dr = self.dr
        dr.maximize_window()
        dr.navigate("http://120.78.140.101/zentao/my/")
        dr.type('i,account', self.USER)
        dr.types('n,password', self.PWD)
        sleep(1)
        # 点击产品
        dr.click('x,/html/body/header/nav[1]/ul/li[2]/a')
        sleep(1)
        # 点击选择中信华
        dr.click('i,currentItem')
        sleep(0.2)
        dr.click('x,/html/body/header/nav[2]/ul/li[1]/div/div/div[1]/ul/li[2]/a')
        sleep(0.5)
        # 点击计划
        dr.click('x,/html/body/header/nav[2]/ul/li[4]/a')
        sleep(0.2)
        dr.click_by_text(self.BANBEN)
        sleep(0.5)

    def test_chandao_xuqiu(self):

        dr = self.dr
        # try:
        for m in range(50):
            m = m + 1
            try:
                dr.execute_script_element('x,/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[1]/form/table/tbody/tr[%s]/td[5]' %str(m))
            except:
                print('结束')
                break
            a = dr.get_text('x,/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[1]/form/table/tbody/tr[%s]/td[5]' %str(m))
            dr.execute_script_element('x,/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[1]/form/table/tbody/tr[%s]/td[8]' %str(m))
            b = dr.get_text('x,/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[1]/form/table/tbody/tr[%s]/td[8]' %str(m))
            if a == self.ZHIPAI and b == self.STATUS:
                dr.click('x,/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[1]/form/table/tbody/tr[%s]/td[3]/a' %str(m))
                sleep(0.5)
                dr.click('x,/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]')
                sleep(0.5)
                dr.select_by_value('i,stage','testing')
                dr.click('x,/html/body/div[1]/div[1]/form/div[2]/div[2]/div/fieldset[2]/table/tbody/tr[2]/td/div/a/div')
                dr.types('x,/html/body/div[1]/div[1]/form/div[2]/div[2]/div/fieldset[2]/table/tbody/tr[2]/td/div/div/div/input',self.NAME)
                dr.click('i,submit')
                dr.explicitly_wait('x,/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/a[1]',10)
                dr.click('x,/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/a[1]')
                sleep(0.5)

        # except:
        #     pass
    def test_chandao_bug(self):

        dr = self.dr
        # 选择bug
        dr.click('x,/html/body/div[1]/div[1]/div[2]/div[1]/div/div/ul/li[2]/a')
        sleep(0.5)
        try:
            for n in range(20):
                n = n + 1
                b = dr.get_text('x,/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[2]/form/table/tbody/tr[%s]/td[5]' %str(n))
                if b == self.STATUS:
                    dr.click('x,/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[2]/form/table/tbody/tr[%s]/td[3]/a'%str(n))
                    sleep(0.5)
                    dr.click('x,/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]')
                    dr.click('x,/html/body/div[1]/form/table/tbody/tr[1]/td[1]/div/a')
                    sleep(0.2)
                    dr.types('x,/html/body/div[1]/form/table/tbody/tr[1]/td[1]/div/div/div/input',self.NAME)
                    dr.click('id,submit')
        except:
            pass
    def wwwee(self):
        dr = self.dr
        csv_file = open("..\\data\\use.csv", mode='r', encoding='utf8')
        csv_reader = csv.reader(csv_file)
        lls = True
        for row in csv_reader:
            if lls == True:
                lls = False
                continue
            data = {'use': row[0]}
            dr.types('id,searchQuery',data['use'])
            sleep(0.5)
            dr.click('x,/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]')
            dr.click('x,//*[@id="mailto_chosen"]/ul/li/input')
            dr.types('x,//*[@id="mailto_chosen"]/ul/li/input','黄达')
            dr.click('id,submit')
            sleep(0.5)





if __name__ == '__main__':
    a = ChaoDao()
    a.test_chaodao_login()
    a.test_chandao_xuqiu()
