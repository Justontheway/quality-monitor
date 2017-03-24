from Alert import Alert

import urllib
import urllib2


class ShortMessage(Alert):
    def open(self):
        return
    def send(self, msg, msg_info, someone):
        try:
            sms_url = self._conf["server"]
            user = self._conf["user"]
            passwd = self._conf["passwd"]
            templateId = msg_info["templateid"]
            traceId = msg_info["traceid"]
            msgType = msg_info["msgtype"]
            for phone in someone:
                data = {"mobiles" : phone,
                        "templateId" : templateId,
                        "username" : user,
                        "password" : passwd,
                        "sendTime" : "",
                        "traceId" : traceId,
                        "msgType" : msgType,
                        "message" : msg
                        }
                body = urllib.urlencode(data)
                request = urllib2.Request(sms_url, body)
                urllib2.urlopen(request)
                print "send to " + phone
        except Exception, ex:
            print Exception,":", ex
            print "Send sms Error!"

