import time
import os
from enum import Enum, unique
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver as appwebdriver
from appium.webdriver.common.touch_action import TouchAction
from base.command import Command

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
PLUGIN_PATH = os.path.join(BASE_PATH, 'plugin')

@unique
class BoxBrowser(Enum):
    """
    定义支持的浏览器，支持Chrome，Firefox，Ie
    """
    Chrome = 0
    Firefox = 1
    Ie = 2
    APP = 3


class BoxDriver(object):
    """
    a simple demo of selenium framework tool
    """

    """
    私有全局变量
    """
    _base_driver = None
    _by_char = None

    """
    构造方法
    """

    def __init__(self, browser_type=0, by_char=",", profile=None ,desired_caps=None):
        """
        构造方法：实例化 BoxDriver 时候使用
        :param browser_type: 浏览器类型
        :param by_char: 分隔符，默认使用","
        :param profile:
            可选择的参数，如果不传递，就是None
            如果传递一个 profile，就会按照预先的设定启动火狐
            去掉遮挡元素的提示框等
        """
        self._by_char = by_char
        if browser_type == BoxBrowser.Chrome or browser_type == 0:
            profile = webdriver.ChromeOptions()
            # profile.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            # profile.add_argument('--headless')
            prefs = {'profile.default_content_settings.popups': 0}
            profile.add_experimental_option('prefs', prefs)
            extension_path1 = PLUGIN_PATH + '\谷歌插件_2_0_4.crx'
            # profile.add_extension(extension_path1)
            driver = webdriver.Chrome(chrome_options=profile)
            # 添加谷歌嘉立创插件方法
        elif browser_type == BoxBrowser.Firefox or browser_type == 1:
            if profile is not None:
                profile = FirefoxProfile(profile)
            driver = webdriver.Firefox(firefox_profile=profile)
        elif browser_type == BoxBrowser.Ie or browser_type == 2:
            driver = webdriver.Ie()

        elif browser_type == BoxBrowser.APP or browser_type == 3:
            driver = appwebdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(8)
        else:
            driver = webdriver.PhantomJS()
        try:
            self._base_driver = driver
            self._by_char = by_char
        except Exception:
            raise NameError("Browser %s Not Found! " % browser_type)

    """
    私有方法
    """

    def _convert_selector_to_locator(self, selector):
        """
        转换自定义的 selector 为 Selenium 支持的 locator
        :param selector: 定位字符，字符串类型，"i, xxx"
        :return: locator
        """
        if self._by_char not in selector:
            return By.ID, selector

        selector_by = selector.split(self._by_char,1)[0].strip()
        selector_value = selector.split(self._by_char,1)[1].strip()
        if selector_by == "i" or selector_by == 'id':
            locator = (By.ID, selector_value)
        elif selector_by == "n" or selector_by == 'name':
            locator = (By.NAME, selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            locator = (By.CLASS_NAME, selector_value)
        elif selector_by == "l" or selector_by == 'link_text' or selector_by == 'link':
            locator = (By.LINK_TEXT, selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            locator = (By.TAG_NAME, selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            locator = (By.XPATH, selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            locator = (By.CSS_SELECTOR, selector_value)
        else:
            raise NameError("Please enter a valid selector of targeting elements.")

        return locator

    def _locate_element(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            element = self._base_driver.find_element(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")

        return element

    def _locate_elements(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            elements = self._base_driver.find_elements(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")

        return elements

    """
    cookie 相关方法
    """

    def get_cookies(self):
        """
        Returns a set of dictionaries, corresponding to cookies visible in the current session.

        :Usage:
            driver.get_cookies()
        """
        return self._base_driver.execute(Command.GET_ALL_COOKIES)['value']

    def get_cookie(self, name):
        """
        Get a single cookie by name. Returns the cookie if found, None if not.

        :Usage:
            driver.get_cookie('my_cookie')
        """
        cookies = self.get_cookies()
        for cookie in cookies:
            if cookie['name'] == name:
                return cookie
        return None

    def clear_cookies(self):
        """
        clear all cookies after driver init
        """
        self._base_driver.delete_all_cookies()

    def add_cookies(self, cookies):
        """
        Add cookie by dict
        :param cookies:
        :return:
        """
        for cookie in cookies:
            self._base_driver.add_cookie(cookie)

    def add_cookie(self, cookie_dict):
        """
        Add single cookie by dict
        添加 单个 cookie
        如果该 cookie 已经存在，就先删除后，再添加
        :param cookie_dict: 字典类型，有两个key：name 和 value
        :return:
        """
        cookie_name = cookie_dict["name"]
        cookie_value = self._base_driver.get_cookie(cookie_name)
        if cookie_value is not None:
            self._base_driver.delete_cookie(cookie_name)

        self._base_driver.add_cookie(cookie_dict)

    def remove_cookie(self, name):
        """
        移除指定 name 的cookie
        :param name:
        :return:
        """
        # 检查 cookie 是否存在，存在就移除
        old_cookie_value = self._base_driver.get_cookie(name)
        if old_cookie_value is not None:
            self._base_driver.delete_cookie(name)

    """
    浏览器本身相关方法
    """

    def refresh(self, url=None):
        """
        刷新页面
        如果 url 是空值，就刷新当前页面，否则就刷新指定页面
        :param url: 默认值是空的
        :return:
        """
        if url is None:
            self._base_driver.refresh()
        else:
            self._base_driver.get(url)

    def maximize_window(self):
        """
        最大化当前浏览器的窗口
        :return:
        """
        self._base_driver.maximize_window()

    def navigate(self, url):
        """
        打开 URL
        :param url:
        :return:
        """
        self._base_driver.get(url)

    def quit(self):
        """
        退出驱动
        :return:
        """
        self._base_driver.quit()

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self._base_driver.close()

    """
    基本元素相关方法
    """

    def type(self, selector, text):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        el = self._locate_element(selector)
        el.clear()
        el.send_keys(text)

    def type_wait(self, selector, text,time=10):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        self.explicitly_wait(selector, time)
        self.type(selector,text)

    def types(self, selector, text):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        el = self._locate_element(selector)
        el.clear()
        el.send_keys(text + Keys.ENTER)

    def click(self, selector):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("i,el")
        """
        el = self._locate_element(selector)
        el.click()

    def click_wait(self, selector,time=10):

        self.explicitly_wait(selector, time)
        self.click(selector)

    def click_wait2(self,selector,n=5):
        for i in range(n):
            time.sleep(1)
            try:
                self._locate_element(selector).click()
                break
            except:pass
            if i == n-1:
                raise NameError('超时，元素未找到')

    def click_more(self, selector):
        """
        对一组元素进行逐一点击
        :return:
        """
        els = self._locate_elements(selector)
        for el in els:
            el.click()

    def click_index(self, selector, n):
        '''
        对一组元素指定点击某个元素
        :param selector:
        :param n: 想点击的第几个元素
        :return:
        '''
        els = self._locate_elements(selector)
        els[n].click()

    def click_by_enter(self, selector):
        """
        It can type any text / image can be located  with ENTER key

        Usage:
        driver.click_by_enter("i,el")
        """
        el = self._locate_element(selector)
        el.send_keys(Keys.ENTER)

    def click_by_text(self, text):
        """
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        """
        self._locate_element('p,' + text).click()

    def submit(self, selector):
        """
        Submit the specified form.

        Usage:
        driver.submit("i,el")
        """
        el = self._locate_element(selector)
        el.submit()

    def move_to(self, selector):
        """
        to move mouse pointer to selector
        :param selector:
        :return:
        """
        el = self._locate_element(selector)
        ActionChains(self._base_driver).move_to_element(el).perform()

    def right_click(self, selector):
        """
        to click the selector by the right button of mouse
        :param selector:
        :return:
        """
        el = self._locate_element(selector)
        ActionChains(self._base_driver).context_click(el).perform()

    def count_elements(self, selector):
        """
        数一下元素的个数
        :param selector: 定位符
        :return:
        """
        els = self._locate_elements(selector)
        return len(els)
    def long_click(self,selector):
        """
        长按元素
        :param selector:
        :param t:单位秒
        :return:
        """
        el_source = self._locate_element(selector)
        TouchAction(self._base_driver).long_press(el_source,None,None,10000).perform()

    def drag_element(self, source, target):
        """
        拖拽元素
        :param source:
        :param target:
        :return:
        """

        el_source = self._locate_element(source)
        el_target = self._locate_element(target)

        if self._base_driver.w3c:
            ActionChains(self._base_driver).drag_and_drop(el_source, el_target).perform()
        else:
            ActionChains(self._base_driver).click_and_hold(el_source).perform()
            ActionChains(self._base_driver).move_to_element(el_target).perform()
            ActionChains(self._base_driver).release(el_target).perform()

    def double_click(self, selector):
        """
        双击鼠标
        :param selector:
        :return:
        """
        el = self._locate_element(selector)
        ActionChains(self._base_driver).double_click(el).perform()

    def drag_element_coord(self, source, x, y):
        """
        拖拽元素至指定位置
        :param source:
        :param target:
        :return:
        """
        el_source = self._locate_element(source)
        ActionChains(self._base_driver).click_and_hold(el_source).perform()
        ActionChains(self._base_driver).move_by_offset(x, y).perform()
        ActionChains(self._base_driver).release().perform()

    def lost_focus(self):
        """
        当前元素丢失焦点
        :return:
        """
        ActionChains(self._base_driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()

    """
    <select> 元素相关
    """

    def select_by_index(self, selector, index):
        """
        It can click any text / image can be clicked
        点击任何文本/图像
        连接，复选框，单选按钮，甚至下拉框等等。
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self._locate_element(selector)
        Select(el).select_by_index(index)

    def get_selected_text(self, selector):
        """
        获取 Select 元素的选择的内容
        :param selector: 选择字符 "i, xxx"
        :return: 字符串
        """
        el = self._locate_element(selector)
        selected_opt = Select(el).first_selected_option()
        return selected_opt.text

    def select_by_visible_text(self, selector, text):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self._locate_element(selector)
        Select(el).select_by_visible_text(text)

    def select_by_value(self, selector, value):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self._locate_element(selector)
        Select(el).select_by_value(value)

    """
    JavaScript 相关
    """

    def execute_js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self._base_driver.execute_script(script)

    """
    元素属性相关方法
    """

    def get_value(self, selector):
        """
        返回元素的 value
        :param selector: 定位字符串
        :return:
        """
        el = self._locate_element(selector)
        return el.get_attribute("value")

    def get_attribute(self, selector, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("i,el","type")
        """
        el = self._locate_element(selector)
        return el.get_attribute(attribute)

    def get_text(self, selector):
        """
        Get element text information.

        Usage:
        driver.get_text("i,el")
        """
        el = self._locate_element(selector)
        return el.text

    def get_displayed(self, selector):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("i,el")
        """
        el = self._locate_element(selector)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self._base_driver.title


    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self._base_driver.current_url

    def get_selected(self, selector):
        """
        to return the selected status of an WebElement
        :param selector: selector to locate
        :return: True False
        """
        el = self._locate_element(selector)
        return el.is_selected()

    def get_text_list(self, selector):
        """
        根据selector 获取多个元素，取得元素的text 列表
        :param selector:
        :param url ddddd
        :return: list
        """

        el_list = self._locate_elements(selector)
        results = []
        for el in el_list:
            results.append(el.text)

        return results


    """
    窗口相关方法
    """

    def accept_alert(self):
        '''
            Accept warning box.

            Usage:
            driver.accept_alert()
            '''
        self._base_driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismissAlert()
        '''
        self._base_driver.switch_to.alert.dismiss()

    def switch_to_alert(self):

        return self._base_driver.switch_to.alert.text

    def switch_to_frame(self, selector):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("i,el")
        """
        el = self._locate_element(selector)
        self._base_driver.switch_to.frame(el)

    def switch_to_default(self):
        """
        
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self._base_driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        """
        退出到上一层frame
        :return:
        """
        self._base_driver.switch_to.parent_frame()

    def switch_to_window_by_title(self, title):
        '''
        跳转到指定标签页
        :param title:
        :return:
        '''
        for handle in self._base_driver.window_handles:
            self._base_driver.switch_to.window(handle)
            if self._base_driver.title == title:
                break

            self._base_driver.switch_to.default_content()

    def open_new_window(self, selector,n=None):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''

        original_windows = self._base_driver.current_window_handle
        all_handles1 = self._base_driver.window_handles
        el = self._locate_elements(selector)
        if n is None:
            n = 0
        el[n].click()
        a = 0
        while a < 5:
            a += 1
            if all_handles1 != self._base_driver.window_handles:
                break
            time.sleep(1)
        else:'未获取新窗口句柄'
        all_handles2 = self._base_driver.window_handles
        for handle in all_handles2:
            if handle != original_windows:
                self._base_driver._switch_to.window(handle)
                continue
        return original_windows

    def remove_window(self, gubing1=None):
        '''
        关闭除了当前标签的其他标签
        :return:
        '''
        handd = self._base_driver.current_window_handle
        dd = self._base_driver.window_handles
        for hand in dd:
            if gubing1 is None:
                if hand != handd:
                    self._base_driver.switch_to_window(hand)
                    self._base_driver.close()
            else:
                if hand != handd and hand != gubing1:
                    self._base_driver.switch_to_window(hand)
                    self._base_driver.close()
        self._base_driver.switch_to_window(handd)

    def current_window_handle(self):
        q = self._base_driver.current_window_handle
        return q

    def window_handles(self):
        q = self._base_driver.window_handles
        return q

    def switch_to_window(self, w):
        self._base_driver.switch_to_window(w)

    def save_window_snapshot(self, file_name):
        """
        save screen snapshot
        :param file_name: the image file name and path
        :return:
        """
        driver = self._base_driver
        driver.save_screenshot(file_name)

    """
    等待方法
    """

    def forced_wait(self, seconds):
        """
        强制等待
        :param seconds:
        :return:
        """
        time.sleep(seconds)

    def implicitly_wait(self, seconds):
        """
        Implicitly wait. All elements on the page.
        :param seconds 等待时间 秒
        隐式等待

        Usage:
        driver.implicitly_wait(10)
        """
        self._base_driver.implicitly_wait(seconds)

    def explicitly_wait(self, selector, seconds):
        """
        显式等待
        :param selector: 定位字符
        :param seconds: 最长等待时间，秒
        :return:
        """
        locator = self._convert_selector_to_locator(selector)

        WebDriverWait(self._base_driver, seconds,0.3).until(expected_conditions.presence_of_element_located(locator))

    def swipLeft(self, t, n):
        '''
        屏幕向左滑动
        :param t: 执行时间
        :param n: 滑动次数
        :return:
        '''
        l = self._base_driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.05
        for i in range(n):
            self._base_driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t, n):
        '''
        屏幕向右滑动
        :param t: 执行时间
        :param n: 滑动次数
        :return:
        '''
        l = self._base_driver.get_window_size()
        x1 = l['width'] * 0.05
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self._base_driver.swipe(x1, y1, x2, y1, t)

    def swipup(self, t, n):
        '''
        屏幕向上滑动
        :param t: 执行时间
        :param n: 滑动次数
        :return:
        '''
        l = self._base_driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.25
        for i in range(n):
            self._base_driver.swipe(x1, y1, x1, y2, t)

    def swipdown(self, t, n):
        '''
        屏幕向下滑动
        :param t: 执行时间
        :param n: 滑动次数
        :return:
        '''
        l = self._base_driver.get_window_size()
        x1 = l['width'] * 0.35
        y1 = l['height'] * 0.45
        y2 = l['height'] * 0.75
        for i in range(n):
            self._base_driver.swipe(x1, y1, x1, y2, t)

    def back(self):
        """
        返回
        :return:
        """
        self._base_driver.back()

    def tap_click(self,xy1,xy2):
        """
        :param xy1: 点击坐标
        :param xy2: 最大坐标
        例：driver.tap_click((552,1341),(810,1440))
        :return:
        """
        n = xy1[0] / xy2[0]
        m = xy1[1] / xy2[1]
        w = self._base_driver.get_window_size()['width']
        h = self._base_driver.get_window_size()['height']
        self._base_driver.tap([(n*w, m*h)],500)

    def execute_script_element(self, selector):
        '''
        滑动鼠标找到需要的元素
        :param script:
        :param args:
        :param selector:
        :return:
        '''
        el = self._locate_element(selector)
        self._base_driver.execute_script("arguments[0].scrollIntoView(false);", el)

    def execute_script(self, script, *args):

        self._base_driver.execute_script(self, script, *args)

    def add_window(self, js):
        '''
        打开浏览器新窗口
        并且切换到新开窗口的句柄中
        :param js:
        :return: 新开窗口的句柄
        '''
        lh1 = self._base_driver.window_handles
        js = js
        self._base_driver.execute_script(js)
        lh2 = self._base_driver.window_handles
        for lh in lh2:
            if lh not in lh1:
                self._base_driver.switch_to_window(lh)
        return self._base_driver.current_window_handle


    @staticmethod
    def change_name(path):
        '''
        改系统文件名称
        :param path: 文件绝对路径
        :return:
        '''
        import os
        try:
            os.makedirs(path)
            print("新建目录"+path)
        except:
            pass
        #
        flg = False
        list = os.listdir(path)
        for i in list:
            if i.endswith('.rar'):
                src = os.path.join(os.path.abspath(path), i)
                dst = os.path.join(os.path.abspath(path), '测试'+time.strftime('%Y%m%d %H_%M_%S', time.localtime()) + '.rar')
                os.rename(src, dst)
                flg = True
                break

        if flg is False:
            today = '测试'+time.strftime('%Y%m%d %H_%M_%S', time.localtime())
            with open(path + '/' +  today + '.txt', 'a+') as fp:
                fp.write('<>')
            src = os.path.join(os.path.abspath(path), today + '.txt')
            dst = os.path.join(os.path.abspath(path), today + '.rar')
            os.rename(src, dst)
        return dst

    def change_html(self, a_on, b_of):
        '''切换到跳转页面句柄'''

        for hh in range(10):
            if a_on == b_of:
                time.sleep(0.5)
                b = self._base_driver.window_handles()
            else:
                break
        for hh in b_of:
            if a_on.__contains__(hh):
                continue
            else:
                self._base_driver.switch_to_window(hh)

    @staticmethod
    def qukongge(a):
        '''去掉空格'''
        d = ''
        if ' ' in a:
            b = a.split(' ')
            for c in b:
                if c not in ' ':
                    d = d + c
            return d
        else:
            return a

    def add_info_windows(self, js):
        ha = self._base_driver.current_window_handle
        self.add_window(js)
        ah = self._base_driver.window_handles
        for hh in ah:
            if ha != hh:
                self._base_driver.switch_to_window(hh)
                break
        aa = self._base_driver.current_window_handle
        return ha, aa

    def wait_selenium(self,seletor,n=None):
        '''
        等待元素存在且可见
        :param seletor:
        :param n:等待时间。默认3s
        :return:
        '''
        if n is not None:
            pass
        else:
            n = 5
        for a in range(n):
            if a+1 == n:
                element = self._locate_element(seletor)
            else:
                try:
                    re = self.get_displayed(seletor)
                    if re == True:
                        element = self._locate_element(seletor)
                        break
                    elif re == False:
                        time.sleep(1)
                except:time.sleep(1)

        return element

    @staticmethod
    def reserved_string(st,type):
        '''
        提取字符串中的内容
        :param st: 参数
        :param type: 类型。'c'是指提取汉字。's'提取字母。'd'提取数字
        :return:
        '''
        import re
        if type == 'c':
            st = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", st)
        elif type == 'd':
            st = re.sub("[^\d.]+" ,"", st)
        elif type == 's':
            st = ''.join(re.findall(r'[A-Za-z]', st))
        return st
