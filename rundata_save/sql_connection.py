import pymysql
import datetime

def sql_into(table_name, values):
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password="12345678",
                           database='test',charset="utf8", autocommit=True)
    cur = conn.cursor()
    sql_ = f"""insert into {table_name}(caseId, testId, caseName, testResult) values {values}"""
    cur.execute(sql_)
    cur.close()
    conn.close()



def get_table_names(table_name):
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password="12345678",
                           database='test', charset="utf8", autocommit=True)
    cur = conn.cursor()
    sql_ = f"""show full columns from {table_name};"""
    cur.execute(sql_)
    # print(cur.fetchall())  #(('ID', 'int', None, 'NO', 'PRI', None, 'auto_increment', 'select,insert,update,references', ''),..)
    results = list()
    for i in cur.fetchall():
        results.append(i[0])
    # print(results)  # ['ID', 'caseId', 'testId', 'caseName', 'createTime', 'updateTime', 'testResult']
    cur.close()
    conn.close()

    return results


def sql_query(sql_):
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password="12345678",
                           database='test', charset="utf8", autocommit=True)
    cur = conn.cursor()
    cur.execute(sql_)
    results = cur.fetchall()
    # print(results)
    list_ = list()
    # 将结果转化为json格式的方式：
    table_names = get_table_names("test_cases")
    for result in results:
        # zip返回的是一个可以转化的对象：你转化成dict，他就会输出dict格式
        list_.append(dict(zip(table_names, result)))
    cur.close()
    conn.close()

    return list_




if __name__ == '__main__':
    # get_table_names("test_cases")
    # 组装一个拿最近七天的测试数据的sql语句
    # 得到七天内的数据语句
    res = sql_query("""
                select * from test_cases
                where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(createTime)
                order by createTime;
                """)
    # print(res)
    # 获取日期（天）
    date_list = list()
    for i in res:
        date_ = str(i['createTime']).split(",")[0].split(" ")[0]
        if date_ not in date_list:
            date_list.append(date_)
    # print(date_list)  # ['2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20', '2023-01-21', '2023-01-22']

    # 获取每天测试数据的条数，其方法最简单的就是依据时间；来进行sql查询
    tests_list = list()
    for i in date_list:
        test_sql = sql_query(f"""
                        select count(*) from test_cases
                        where createTime like '{i}%';
                    """)
        # print(test_sql)  # [{'ID': 2}]
        tests_list.append(test_sql[0]["ID"])
    print(tests_list)

    # 获取每天测试异常的数据
    failed_list = list()
    for i in date_list:
        failed_sql = sql_query(f"""
                        select count(*) from test_cases
                        where createTime like '{i}%'
                        and testResult != 'passed';
                    """)
        failed_list.append(failed_sql[0]["ID"])
    print(failed_list)

