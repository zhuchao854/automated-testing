from base.base_page import BasePage
from base.box_driver import BoxDriver,BoxBrowser
from datetime import datetime
from datetime import timedelta
from time import sleep
import time

def date_add(date_str, days_count=1):
    """日期加减"""
    date_list = time.strptime(date_str, "%Y-%m-%d")
    y, m, d = date_list[:3]
    whatday = datetime(y, m, d).strftime("%w")  # 判断星期几（注意：星期天为数字0）
    if whatday == '5':
        days_count = 3
    delta = timedelta(days=days_count)
    date_result = datetime(y, m, d) + delta
    date_result = date_result.strftime("%Y-%m-%d")
    return date_result


def num_to_char(num):
    """月份数字转中文"""
    num=str(num)
    listnum = list(num)
    if listnum[0] == '0':
        if str(len(listnum)) == '2':
            num = listnum[1]
    num_dict={"0":u"零","1":u"一","2":u"二","3":u"三","4":u"四","5":u"五","6":u"六","7":u"七","8":u"八","9":u"九","10":u"十","11":u"十一","12":u"十二",}
    new_str=num_dict[num]+'月'
    return new_str


class JIRA(BasePage):
    def jira_login(self,use,pwd):
        '''登录jira'''
        dr = self.base_driver
        dr.maximize_window()
        dr.implicitly_wait(1)
        dr.navigate('http://jr.sz-jlc.com:8080/')
        dr.type('x,//*[@id="login-form-username"]',use)
        dr.types('x,//*[@id="login-form-password"]',pwd)
        sleep(2)


    def jira_title_question(self,sizer='版本需求',status=('关闭','验收中')):
        '''设置测试计划'''
        dr = self.base_driver
        dr.click('x,//*[@id="find_link"]')
        dr.click('x,//*[@id="jira.top.navigation.bar:issues_drop_current_lnk"]')#当前搜索问题
        sleep(2)
        dr.click('x,//a[@title="%s"]'%sizer)#筛选器
        sleep(2)
        a = 1
        for i in range(150):
            if i/50 < a:pass
            else:
                try:
                    dr.click('x,//a[@class="icon icon-next"]')                      #下一页
                    a = a + 1
                    sleep(2)
                except:
                    print('无下页数据了')
                    break
            i = i-(50*(a-1))
            try:
                demand_a = dr._locate_elements('x,//td[@class="summary"]/p/a')[i]               # 需求标题链接
            except Exception as f:
                print(f)
                print('数据已处理完成')
                break
            exploit_time = dr._locate_elements('x,//td[@class="customfield_10217"]')[i]     # 开发完成时间元素
            test_time = dr._locate_elements('x,//td[@class="customfield_10503"]')[i]        # 需求链接
            statu = dr._locate_elements('x,//td[@class="status"]')[i]                      # 需求状态
            code = demand_a.get_attribute('data-issue-key')                     #需求/bug编号
            demand_text = demand_a.text                                         #需求文本
            statu_text = statu.text                                             #需求状态
            if exploit_time.text == '' or statu.text.strip() in status:     #开发完成时间为空，并且需求状态筛选
                continue
            else:
                time_param = date_add(exploit_time.text.split('00:00')[0].strip()).split('-')
            if test_time.text != '':                #存在测试时间就跳过。
                continue
            else:
                demand_a.click()
                try:
                    dr.click('x,//a/span[text()="工作流"]')
                except:
                    pass
                try:
                    dr.click('x,//a/span[text()="设置测试计划"]')
                    new_time = time_param[-1] +'/'+ num_to_char(str(time_param[1]))+'/' + time_param[0]  # 时间格式处理
                    dr.type('x,//*[text()="计划开始测试时间"]/following-sibling::input',new_time)
                    dr.type('x,//*[text()="计划完成测试时间"]/following-sibling::input',new_time)
                    dr.click('x,//*[@id="issue-workflow-transition-submit"]')#点击保存
                    sleep(2)
                except:
                    print(code,demand_text,statu_text)
                dr.click('x,//*[@id="return-to-search"]')#返回搜索列表
                sleep(2)

    def feipei_test_user(self,sizer='版本需求',user='zhuchao'):
        '''设置分配测试人'''
        dr = self.base_driver
        dr.click('x,//*[@id="find_link"]')
        dr.click('x,//*[@id="jira.top.navigation.bar:issues_drop_current_lnk"]')  # 当前搜索问题
        sleep(2)
        dr.click('x,//a[@title="%s"]' % sizer)  # 筛选器
        sleep(2)
        for i in range(50):
            try:
                test_user = dr._locate_elements('x,//td[@class="customfield_10201"]')[i]
            except:
                print('数据处理完成')
                break
            if test_user.text != '':
                continue
            else:
                demand_a = dr._locate_elements('x,//td[@class="summary"]/p/a')[i]
                demand_a_text = demand_a.text
                demand_a.click()#点击需求链接
                sleep(2)
                try:
                    dr.click('x,//span[@class="trigger-label" and text()="分配测试"]')#点击分配测试
                    sleep(0.5)
                    dr.type('x,//*[@id="customfield_10201"]',user)
                    dr.click('x,//*[@id="issue-workflow-transition-submit"]')
                    sleep(1)
                except:
                    print(demand_a_text+'：无分配测试按钮')
                dr.click('x,//*[@id="return-to-search"]')  # 返回搜索列表
                sleep(2)




if __name__ == '__main__':
    dr = JIRA(BoxDriver(BoxBrowser.Chrome))
    dr.jira_login(use='zhuchao',pwd='ZHuchao0505')
    dr.jira_title_question()
    # dr.feipei_test_user()
