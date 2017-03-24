#-*- coding:utf-8 -*-

import os
import sys
import ConfigParser
import optparse

sys.path.append(os.path.join(os.getenv("MONITOR_HOME", ".."), "lib"))

from collector import MysqlCollector


def load_conf(confs = []):
    conf_dict = {}
    confLoader = ConfigParser.SafeConfigParser()
    confLoader.read(confs)
    for section in confLoader.sections():
        conf_dict[section] = dict(confLoader.items(section))
    return conf_dict

def parse_args(argv = []):
    parser = optparse.OptionParser()
    parser.add_option("-b", "--base", dest = "home", default = "..")
    parser.add_option("-C", "--conf", dest = "confpath", default = "conf/mysql.conf")
    parser.add_option("-d", "--db", dest = "database", default = "report")
    parser.add_option("-t", "--table", dest = "table")
    parser.add_option("-H", "--host", dest = "host")
    parser.add_option("-P", "--port", dest = "port")
    parser.add_option("-u", "--user", dest = "user")
    parser.add_option("-p", "--passwd", dest = "password")
    parser.add_option("-f", "--file", dest = "datafile")
    parser.add_option("-s", "--short", dest = "mysqlalias")
    opt, args = parser.parse_args(argv)
    return opt.home, opt.confpath.split(","), opt.host, opt.port, opt.user, opt.password, opt.database, opt.table, opt.datafile, opt.mysqlalias

def data_gen():
    basepath, conffiles, host, port, user, password, database, table, datafile, mysqlalias = parse_args(sys.argv[1:])
    confpath = [os.path.join(basepath, conffile) for conffile in conffiles]
    conf = load_conf(confpath)
    mysql_conf = conf[mysqlalias] if mysqlalias else conf["mysql30"]
    mysql_conf["table"] = table
    if host and port and user and password and database:
        mysql_conf.update({"host":host, "port":port, "user":user, "password":password, "database":database})
    mctc = MysqlCollector.MysqlCollectorThreeColumn(mysql_conf)
    ds = mctc.get_data()
    return ds


if __name__ == "__main__":
    data_gen()

