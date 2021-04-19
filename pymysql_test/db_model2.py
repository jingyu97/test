import pymysql

import mysql_test.db_config


class db_utils:
    #连接数据库
    mysql_conn = pymysql.connect(
        host = mysql_test.db_config.host,
        port = mysql_test.db_config.port,
        user = mysql_test.db_config.user,
        passwd = mysql_test.db_config.passwd,
        db = mysql_test.db_config.db,
        charset = mysql_test.db_config.charset
    )

    sql =   "select name,sex from user "

    def mysql_execute(self,my_sql):
        cursor = self.mysql_conn.cursor()
        cursor.execute(my_sql)
        exec_result = cursor.fetchall()
        exec_count = cursor.rowcount
        return exec_count,exec_result

    def mysql_del(self):
        self.mysql_conn.close()

    #查找性别为女生的人员
    def find(self):
        print("查找出的女生为：")
        count,mysql_result = self.mysql_execute(self.sql)
        for i in range(6):
            a,b  = mysql_result[i]
            if b == '女':
                print("我的名字是{},我是一个{}生".format(a,b))

    #获取sql执行受影响的行数
    def mysql_count(self):
        count,mysql_result = self.mysql_execute(self.sql)
        print("sql执行结果受影响的行数：{}".format(count))

    #获取sql执行结果
    def mysql_result(self):
        count,mysql_result = self.mysql_execute(self.sql)
        print("sql执行结果集：{}".format(mysql_result))




