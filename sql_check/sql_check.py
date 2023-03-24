import pymysql


class CheckSql:

    def __init__(self, user, passwd, host, port, database):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.database = database
        self.conn = pymysql.connect(user=self.user, password=self.passwd, host=self.host,
                                    port=self.port, database=self.database, charset="utf8",
                                    autocommit=True)
        self.cursor = self.conn.cursor()

    def chSql(self, sql, size=0):
        """

        :param sql: 传入查询的sql语句，字符串格式
        :param size: 返还结果记录条数，不传时默认查询全部
        :return: self.res返回查询结果数据，self.cnt返回查询记录总行数
        """
        if sql.startswith('select'):
            self.cursor.execute(sql)  # 执行sql
            self.cnt = self.cursor.rowcount  # 统计查询结果数据
            if size == 0:
                self.res = self.cursor.fetchall()  # 获取所有查询结果
            else:
                self.res = self.cursor.fetchmany(size)  # 获取指定条数查询结果
        else:
            print('非查询sql语句')

        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()
        return self.res

    def AddDelUp(self, sql):

        if sql.startswith('insert'):
            print('插入数据到数据库表')
            self.cursor.execute(sql)

        elif sql.startswith('delete'):
            print('删除数据库表内容')
            self.cursor.execute(sql)

        else:
            print('更新数据库表内容')
            self.cursor.execute(sql)

        self.cursor.close()
        self.conn.close()


# if __name__ == '__main__':
#     DB_connect = CheckSql('root','12345678','127.0.0.1',3305,'test')
#     chk_sql = 'select * from student;'
#     del_sql = 'delete from student where id=17'
#     add_sql = "insert into student values (5,'WY',30)"
#     up_sql = "update student set age=21 where id=5"
#
    # check_res = DB_connect.chSql(chk_sql, 1)
    # print(check_res)
#     # DB_connect.AddDelUp(up_sql)

