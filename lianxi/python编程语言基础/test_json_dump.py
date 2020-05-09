import json
#dump把数据类型转换成字符串并存储在文件中
def test_dump():
    info = [{
                "name":"tome",
                "gender":"male",
                "other":None
            },{
                "name":"jack",
                "gender":"male",
                "other":None
            }]
    print("读取json文件")
    json.dump(info,open("datas/json_jump.json","w"),indent=4)