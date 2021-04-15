import mysql_test.db_config
import pymysql

class db_utils:
    #连接数据库
    conn = pymysql.connect(
        host = mysql_test.db_config.host,
        port = mysql_test.db_config.port,
        user = mysql_test.db_config.user,
        passwd = mysql_test.db_config.passwd,
        db = mysql_test.db_config.db,
        charset = mysql_test.db_config.charset
    )
    cursor = conn.cursor()
    my_sql = "select name,sex from user "
    cursor.execute(my_sql)
    #one = cursor.fetchone()
    #many = cursor.fetchmany(2)
    all = cursor.fetchall()
    count = cursor.rowcount


    #打印sql执行结果
    def Print(self):
        #print(db_utils.one)
        #print(db_utils.many)
        print("sql执行结果：{}".format(db_utils.all))

    #查找性别为女生的人员
    def Find(self):
        print("查找出的女生为：")
        for i in range(db_utils.count):
            a,b  = db_utils.all[i]
            if b == '女':
                print("我的名字是{},我是一个{}生".format(a,b))


    cursor.close()
    conn.close()