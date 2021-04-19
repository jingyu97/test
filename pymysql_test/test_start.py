from pymysql_test.db_model2 import db_utils

if __name__ == '__main__':
    sql_result = db_utils()
    sql_result.mysql_count()
    sql_result.mysql_result()
    sql_result.find()
    sql_result.mysql_del()