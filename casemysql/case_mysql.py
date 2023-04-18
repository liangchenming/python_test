import json

from casemysql.ubmpdb import UbmpdbMysql
from common.csv_sample import CsvUtil


class SampleInfo:
    def test_saplme(self):
        sql = "SELECT s.TEAM_ID,s.TEAM_NAME,s.TEAM_MASTER,s.ACTIVE_TIME,s.CORP_ID FROM sys_team_info s WHERE s.team_name like '%组'"
        stock = UbmpdbMysql().select_info(sql)
        p = CsvUtil().write_sample_csv(stock)
        print(type(stock))
