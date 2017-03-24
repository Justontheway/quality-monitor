#-*- coding:utf-8 -*-
from Alert import Alert

import smtplib
from email.mime.text import MIMEText
from email.header import Header

from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication


class Email(Alert):
    def open(self):
        return
    def _send_email(self, _email, _to_list):
        user = self._conf["user"]
        passwd = self._conf["passwd"]
        server = self._conf["server"]
        port = self._conf["port"]
        # send with SMTP_SSL
        conn = smtplib.SMTP_SSL(timeout = 20)
        conn.connect(server, port)
        conn.login(user, passwd)
        conn.sendmail(user, ",".join(_to_list), _email.as_string())
        conn.quit()
        print "send email to %s."%(_email["to"])
    def _gen_email_without_attach(self, _msg, msg_info, someone):
        return MIMEText(_msg, "html", msg_info["encoding"])
    def _gen_email_with_attach(self, _msg, msg_info, someone):
        msg = MIMEMultipart()
        # main email content
        content = MIMEText(_msg, "html", msg_info["encoding"])
        msg.attach(content)
        # attachment
        attachments = msg_info["attachment"]
        for attachpath, attachname in attachments:
            attach = MIMEApplication(open(attachpath, 'rb').read())
            attach.add_header('Content-Disposition', 'attachment', filename = attachname)
            msg.attach(attach)
        return msg
    def send(self, msg, msg_info, someone):
        gen_email = self._gen_email_with_attach if msg_info["attachment"] else self._gen_email_without_attach
        try:
            msg = gen_email(msg, msg_info, someone)
            msg["Subject"] = Header(msg_info["subject"], msg_info["encoding"])
            #msg["from"] = Header(msg_info["from"], msg_info["encoding"])
            msg["from"] = msg_info["from"]
            msg["to"] = ",".join(someone)
            print msg["Subject"]
            print msg["from"]
            self._send_email(msg, someone)
        except Exception, ex:
        #except NotImplementedError, ex:
            print Exception,":", ex
            print "Send Email Error!"

