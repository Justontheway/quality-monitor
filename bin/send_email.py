#-*- coding:utf-8 -*-
import os
import sys
import ConfigParser
import optparse

sys.path.append(os.path.join(os.getenv("MONITOR_HOME", ".."), "lib"))

from alert import Email
reload(sys)
sys.setdefaultencoding('utf8')


def load_conf(confs = []):
    conf_dict = {}
    confLoader = ConfigParser.SafeConfigParser()
    confLoader.read(confs)
    for section in confLoader.sections():
        conf_dict[section] = dict(confLoader.items(section))
    return conf_dict

def parse_args(argv = []):
    parser = optparse.OptionParser()
    parser.add_option("-a", "--attachment", dest = "attachment", default = None)
    parser.add_option("-b", "--base", dest = "home", default = "..")
    parser.add_option("-C", "--conf", dest = "confpath", default = "conf/alarm.conf")
    parser.add_option("-s", "--subject", dest = "subject")
    parser.add_option("-f", "--from", dest = "_from")
    parser.add_option("-t", "--to", dest = "_to")
    opt, args = parser.parse_args(argv)
    print args
    if len(args) < 1:
        print "args error"
        parser.print_help()
        sys.exit(-1)
    attachment = [tuple(attach.split(":")) for attach in opt.attachment.split(",")] if opt.attachment else None
    return opt.home, opt.confpath.split(","), opt._from, opt._to.split(","), opt.subject, attachment, args[0]

def send_email():
    basepath, conffiles, _from, _to, subject, attachment, message = parse_args(sys.argv[1:])
    confpath = [os.path.join(basepath, conffile) for conffile in conffiles]
    conf = load_conf(confpath)
    email_conf = conf["email"]
    for key,value in email_conf.items():
        print key,value
    email_conf["from"] = _from.decode("utf8") if _from else u"日常统计"
    email_conf["subject"] = subject
    email_conf["attachment"] = attachment
    import template
    message = template.test().encode("utf8")
    Email.Email(email_conf).send(message, email_conf, _to)


if __name__ == "__main__":
    send_email()

