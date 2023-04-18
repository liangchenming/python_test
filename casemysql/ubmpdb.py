import json
import pymysql as pymysql
from sshtunnel import SSHTunnelForwarder


class UbmpdbMysql:
    def __init__(self):
        # with SSHTunnelForwarder(
        #         ('fort.sinochemhx.com', 60022),
        #         ssh_pkey="/Users/motong/Public/id_rsa_liangchenming",
        #         ssh_username="liangchenming",
        #         ssh_password='',
        #         remote_bind_address=('172.16.50.120', 3306)
        # ) as server:
        #     self.ubmpdb = pymysql.connect(
        #         host='172.16.50.120',
        #         user='liangchenming',
        #         database='ubmpdb'
        #     )

        self.ubmpdb = pymysql.connect(
            host='192.168.100.66',
            user='salesuatdba',
            password='Salesdba#Uat2018',
            database='ubmpdb'
        )

    def select_info(self, sql):
        # 创建游标对象
        storehouse = self.ubmpdb.cursor()

        # 执行sql
        storehouse.execute(sql)

        # 获取执行结果
        stock_item = storehouse.fetchall()

        # 关闭游标对象
        storehouse.close()

        # 关闭数据库
        self.ubmpdb.close()

        # 表结构获取字段
        info = [datas[0] for datas in storehouse.description]
        # 获取value拼接表结构字段
        # info_value = [dict(zip(info, result)) for result in stock_info][0]
        #
        # # 处理datetime格式日期时间
        # data_str = json.dumps(info_value, default=str, ensure_ascii=False)
        # data_info = json.loads(data_str)
        # datas = dict(data_info)
        return info, stock_item
