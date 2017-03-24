import os
import sys
import ConfigParser
import optparse

sys.path.append(os.path.join(os.getenv("MONITOR_HOME", ".."), "lib"))
from alert import ShortMessage


def load_conf(confs = []):
    conf_dict = {}
    confLoader = ConfigParser.SafeConfigParser()
    confLoader.read(confs)
    for section in confLoader.sections():
        conf_dict[section] = dict(confLoader.items(section))
    return conf_dict

def parse_args(argv = []):
    parser = optparse.OptionParser()
    parser.add_option("-p", "--phone", dest = "phones")
    parser.add_option("-b", "--base", dest = "home", default = "..")
    parser.add_option("-C", "--conf", dest = "confpath", default = "conf/alarm.conf")
    opt, args = parser.parse_args(argv)
    print args
    if len(args) < 1:
        print "args error"
        parser.print_help()
        sys.exit(-1)
    return opt.home, opt.confpath.split(","), opt.phones.split(","), args[0]

def send_shortmessage():
    basepath, conffiles, phones, message = parse_args(sys.argv[1:])
    confpath = [os.path.join(basepath, conffile) for conffile in conffiles]
    conf = load_conf(confpath)
    shortmsg_conf = conf["shortmessage"]
    for key,value in shortmsg_conf.items():
        print key,value
    ShortMessage.ShortMessage(shortmsg_conf).send(message, shortmsg_conf, phones)


if __name__ == "__main__":
    send_shortmessage()

