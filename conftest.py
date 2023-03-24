"""
pytest的钩子函数，可以解决获取数据的问题
"""
import pytest
from rundata_save.sql_connection import sql_into


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
　　  每个测试用例执行后，制作测试报告
　　  :param item:测试用例对象
　　  :param call:测试用例的测试步骤
　　         执行完常规钩子函数返回的report报告有个属性叫report.when
            先执行when=’setup’ 返回setup 的执行结果
            然后执行when=’call’ 返回call 的执行结果
           最后执行when=’teardown’返回teardown 的执行结果
　　  :return:
    """
    # 获取常规钩子方法的调用结果,返回一个result对象
    out = yield   # 是通过yield关键字做轮循
    # 获取调用结果的测试报告，返回一个report对象, report对象的属性包括
    # when（steup, call, teardown三个值）、nodeid(测试用例的名字)、
    # outcome(用例的执行结果，passed,failed)
    report = out.get_result()
    if report.when == "call": # 固定写法（固定过滤语句）   # call阶段不运行skip用例
        # caseId, testId, caseName, testResult
        print(report.__dict__)
        sql_into(
            table_name='test_cases',
            values=(report.location[0], report.nodeid, report.location[-1], report.outcome)
        )
        print("测试结果：", report.outcome)