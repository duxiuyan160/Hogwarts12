import json

#loads:将 字符串 转换为 json
def test_loads():
    str = '''
    [{
        "name":"Tom",
        "gender":"male"
    },{
        "name":"Jack",
        "gender":"male"
    }]
    '''
    print(type(str))
    data = json.loads(str)
    print(type(data))
    print(data)