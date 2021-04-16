
from mysql_test.db_model import db_utils




if __name__ == '__main__':
    sql_result = db_utils()
    sql_result.print_mysql_count()
    #sql_result.print_mysql_result()
    sql_result.find()