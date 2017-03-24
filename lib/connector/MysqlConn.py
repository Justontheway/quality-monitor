import MySQLdb

from Connector import Connector


class MysqlConn(Connector):
    def open(self):
        conf = self._conf
        _host = conf.get("host")
        _port = conf.get("port")
        _user = conf.get("user")
        _passwd = conf.get("password")
        _db = conf.get("database")
        _charset = conf.get("charset", "utf8")
        self._conn = MySQLdb.connect(host=_host, port=int(_port), user=_user, passwd=_passwd, db=_db, charset=_charset)
        self._cursor = self._conn.cursor()
        self._query = self._cursor.execute
        self._get_result = self._cursor.fetchall
        self._convert_datetime = lambda t: "%4d-%2d-%2d"%(t.year, t.month, t.day) if isinstance(t, datetime.date) else t

    def close(self):
        self._cursor.close()
        self._conn.close()

    def _get_sql_result(self, sql):
        self._query(sql)
        return self._get_result()

    def query(self, sql):
        return self._get_sql_result(sql)

