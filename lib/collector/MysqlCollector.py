import datetime
from itertools import groupby

from Collector import Collector
from connector import MysqlConn


class MysqlCollector(Collector):
    def open(self):
        return
    def gen_sql(self):
        raise NotImplementedError
    def filter_data(self, raw_data):
        raise NotImplementedError
    def group_data(self, raw_data):
        raise NotImplementedError
    def get_data(self):
        with MysqlConn.MysqlConn(self._conf) as mc:
            raw_dataset = mc.query(self.gen_sql())
        return self.group_data(self.filter_data(raw_dataset))



class MysqlCollectorThreeColumn(MysqlCollector):
    def gen_sql(self):
        sql = """
            select
                totaldate, totalname, concat(totalvalue)
            from
                %(table)s
                order by totalname, totaldate desc
            """%(self._conf)
        return sql
    def filter_data(self, raw_data):
        def cvt(x):
            ok = True
            try:
                float(x)
            except Exception, e:
                print e
                print x
                ok = False
            finally:
                return ok
        return filter(lambda d:cvt(d[2]), raw_data)
    def group_data(self, raw_data):
        grouped_data = {}
        # @TODO sort all-data first manually with sorted().
        for key, values in groupby(raw_data, lambda d:d[1]):
            #grouped_data[key] = list(values)
            grouped_data[key] = [(v[0], v[2]) for v in values]
        return grouped_data

