import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class HtmlEmailAttachment:
    def email_attachment(self, report_path):
        '''配置发送附件测试报告到邮箱'''
        '''发件相关参数'''
        smtpserver = 'smtp.qq.com'  # 发件服务器
        port = 465
        sender = '337464862@qq.com'
        psw = '199405zczc'
        # receiver = 'xxx@qq.com'	单人接收
        receiver = ['337464862@qq.com']  # 接收人
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        msg['from'] = sender  # 发件人
        # msg['to'] = receiver	单人接收
        msg['to'] = ';'.join(receiver)  # 多人接收（返回一个以分隔符;连接各个元素后生成的字符串）
        msg['subject'] = '中信华自动化测试报告'  # 主题
        '''读取测试报告内容'''
        with open(report_path, 'rb') as rp:
            ruisi_mail_body = rp.read()
        '''正文'''
        # MIMEText有三个参数，第一个对应文本内容，第二个对应文本的格式，第三个对应文本编码
        body = MIMEText(ruisi_mail_body, 'html', 'utf8')
        msg.attach(body)
        '''附件'''
        att = MIMEText(ruisi_mail_body, 'base64', 'utf8')
        # Content-Type,说明内容类型，txt/plain是纯文本类型。Application/octet-stream是添加附件类型。
        att['Content-Type'] = 'application/octet-stream'
        # 服务端向客户端游览器发送文件时，如果是浏览器支持的文件类型，一般会默认使用浏览器打开，
        # 比如txt、jpg等，会直接在浏览器中显示，如果需要提示用户保存，
        # 就要利用Content-Disposition进行一下处理，关键在于一定要加上attachment
        # 这样浏览器会提示保存还是打开，即使选择打开，也会使用相关联的程序比如记事本打开，而不是IE直接打开了。
        att['Content-Disposition'] = 'attachment;filename = "%s"' % report_path
        msg.attach(att)
        '''发送邮件'''
        # SMTP_SSL是smtplib.SMTP派生出的新类，用来处理ssl连接
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)  # 登录
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送
        smtp.close()  # 关闭
