import json

a = '{"name":"王雁", "age":17}'
b = json.dumps(a, ensure_ascii=False)
d= "{\"name\":\"王雁\", \"age\":17}"
c = eval(a)
# print(b)
# print(type(b))
print(c)
print(type(c))