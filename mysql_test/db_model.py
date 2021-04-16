import mysql_test.db_config
import pymysql

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

    my_sql = "select name,sex from user "
    cursor = mysql_conn.cursor()
    cursor.execute(my_sql)


    #获取sql执行受影响的行数
    def get_mysql_count(self):
        count = self.cursor.rowcount
        return count

    def print_mysql_count(self):
        print("sql执行结果受影响的行数：{}".format(self.get_mysql_count()))


    #获取sql执行结果
    def get_mysql_result(self):
        sql_result = self.cursor.fetchall()
        return sql_result

    def print_mysql_result(self):
        print("sql执行结果集：{}".format(self.get_mysql_result()))

    #查找性别为女生的人员
    def find(self):
        print("查找出的女生为：")
        mysql_result = self.get_mysql_result()
        for i in range(self.get_mysql_count()):
            a,b  = mysql_result[i]
            if b == '女':
                print("我的名字是{},我是一个{}生".format(a,b))
    cursor.close()
    mysql_conn.close()

    #one = cursor.fetchone()
    #many = cursor.fetchmany(2)