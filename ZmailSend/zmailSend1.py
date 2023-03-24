import zmail


class ZmailSend:

    def __init__(self, fsz, jsz, csz):
        self.mail_sender = fsz
        self.mail_receiver = jsz
        self.mail_server = zmail.server(*self.mail_sender)
        self.mail_cc = csz

    def MailContent(self, cont):
        # if con_text:

        if cont != '':
            self.con_text = None
            self.con_html = None
            if isinstance(cont, str):
                self.con_text = cont
                return self.con_text, self.con_html
            else:
                with open(cont, 'r', encoding='utf-8') as file:
                    self.con_html = file.read()
                    return self.con_text, self.con_html
        else:
            return 'FIY'

    def SendMail(self, title, att, con):
        mail_content = {
            'subject': title,
            'attachments': att,
            'content_text': self.MailContent(con)[0],
            'context_html': self.MailContent(con)[1]
        }
        self.mail_server.send_mail(recipients=self.mail_receiver,
                                   mail=mail_content, cc=self.mail_cc)



if __name__ == '__main__':
    es = ZmailSend(fsz=['1985496797@qq.com','nhxzfwohvtgebjeb'],
                   jsz=['wangyan_921013@163.com'],
                   csz=['1985496797@qq.com'])
    es.SendMail("邮件封装测试2", ['../htmlreport/report.html'], '../htmlreport/report.html')
