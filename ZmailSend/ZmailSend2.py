# zmail封装
import zmail


class MySendEmail:
    def __init__(self, subject, content_txt=None, content_html=None, atta=None):
        self.mail_msg = None
        if content_txt:
            if atta:
                if isinstance(atta, list):
                    self.mail_msg = {
                        'subject': '主题：' + subject,
                        'content_text': '正文内容：\n' + content_txt,
                        'attachments': atta
                    }
                else:
                    print('附件类型不是列表类型~~')
            else:
                self.mail_msg = {
                    'subject': '主题：' + subject,
                    'content_text': '正文内容：\n' + content_txt
                }
        elif content_html:
            with open(content_html, 'r', encoding='utf-8') as file:
                self.cont_html = file.read()
            if atta:
                if isinstance(atta, list):
                    self.mail_msg = {
                        'subject': '主题：' + subject,
                        'content_html': '正文内容：\n' + self.cont_html,
                        'attachments': atta
                    }
                else:
                    print('附件类型不是列表类型~~')

            else:
                self.mail_msg = {
                    'subject': '主题：' + subject,
                    'content_html': '正文内容：\n' + self.cont_html
                }
        else:
            print('没有输入正文内容~~')

    def my_mail(self, recipients=None, cc=None, username='1985496797@qq.com',
                password='nhxzfwohvtgebjeb'):
        if recipients and isinstance(recipients, list):
            self.sever = zmail.server(username, password)
            if cc and isinstance(cc, list):
                self.sever.send_mail(recipients=recipients, mail=self.mail_msg, cc=cc)
            else:
                self.sever.send_mail(recipients=recipients, mail=self.mail_msg)
        else:
            print('没有输入收件人or收件人不是列表来存储的')


if __name__ == '__main__':
    # 调用
    rec = ['wangyan_921013@163.com', 'wangyan202210@126.com']
    cc = ['wangyan202210@126.com', '1985496797@qq.com']
    # ss = MySendEmail(subject='邮件封装3',
    #                  content_html='../htmlreport/report.html')
    ss = MySendEmail(subject='邮件封装4',
                     content_html='../allure_report1/index.html',
                     atta=['../allure_report1/index.html'])
    ss.my_mail(rec, cc)
