import json
import allure
import requests

class CoreHttp:
    """
    1、使用反射进行最直接简单的http核心业务--传入反射的对象，反射对象的方法名
    getattr(object,name) -> value
    2、重要区分json/data与params，前面是post后面是get
        1）区分方式判断data是不是json格式
            1）使用try...except...
            2）原因是判断出现异常，可以进行处理，且代码能继续进行
            3）使用json.dumps()方法
        2）设定一个flag判断条件，很简单方便
        3）如果不是，作为params形式传入
    3、json.dumps()把字典转换为json格式字符串
       json.loads()把json转换为字典
    """
    @allure.step("发送http请求")
    def core_http(self, url=None, method=None, headers=None, data=None, para_type=None, **kwargs):
        if para_type == 'json':
            # json 传参时，传参类型必须是str
            # 参数类型为dict的情况下,是无需将dict,转换为str的，因为在requests模块内部已经自动为你做了这件事
            # datas = eval(data)
            # try:
            #     json.dumps(data, ensure_ascii=False)   # 不把汉字进行转换
            # except Exception as e:
            #     print("无法转换为JSON格式")
            #     datas = data
            res = getattr(requests, method)(url=url, json=data, headers=headers, **kwargs)
        elif para_type == 'data':
            # data传入 dict 时，请求头 默认设置为Content-Type:application/x-www-form-urlencoded
            # data 传入str 时，请求头不会默认设置任何 内容类型，如果想要使用data传参str类型的参数时
            # 建议单独设置一个请求头并设置其内容类型为'Content-Type': 'application/json'
            res = getattr(requests, method)(url=url, data=data, headers=headers, **kwargs)
        else:
            res = getattr(requests, method)(url=url, params=data, headers=headers, **kwargs)

        return res