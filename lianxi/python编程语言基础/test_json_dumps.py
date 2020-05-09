import json
def test_dumps():
    info = [{
                "name":"tome",
                "gender":"male",
                "other":None
            },{
                "name":"jack",
                "gender":"male",
                "other":None
            }]

    #dumps:将python中的字典转换为字符串
    data = json.dumps(info,sort_keys=True,indent=4)#indent 以缩进的形式进行输出
    print(data)
    print(type(data))