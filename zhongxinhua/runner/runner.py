import time
import unittest

from base.html_test_runner import HtmlTestRunner
from base.html_email_attachment import HtmlEmailAttachment


class TestRunner:
    def runner(self):
        # 创建测试套件
        case_path = '..\\case'#用例路径
        testsuite = unittest.TestSuite()#创建套件

        # 给套件添加测试用例
        dicover = unittest.defaultTestLoader.discover(case_path, pattern="test_case.py",
                                                      top_level_dir=None)
        testsuite.addTests(dicover)
        # 生成报告的存放路径
        report_path = '..\\report\\reports_%s.html' \
                      % time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
        report_file = open(report_path, 'wb')
        test_runner = HtmlTestRunner(stream=report_file,
                                     title='中信华下单测试场景',
                                     description='测试详情')
        '''运行套件内的测试用例'''
        test_runner.run(testsuite)
        report_file.close()

        # '''发送附件测试报告到邮箱'''
        HtmlEmailAttachment().email_attachment(report_path)


if __name__ == '__main__':
    TestRunner().runner()
