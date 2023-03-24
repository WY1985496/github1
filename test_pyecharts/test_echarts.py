from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
from rundata_save.sql_connection import *


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
# print(tests_list)

# 获取每天测试异常的数据
failed_list = list()
for i in date_list:
    failed_sql = sql_query(f"""
                    select count(*) from test_cases
                    where createTime like '{i}%'
                    and testResult != 'passed';
                """)
    failed_list.append(failed_sql[0]["ID"])
# print(failed_list)

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(date_list)
    .add_yaxis("测试用例", tests_list)
    .add_yaxis("异常数量", failed_list)
    .set_global_opts(title_opts=opts.TitleOpts(title="测试数据统计", subtitle="副标题"))
)

bar.render()
