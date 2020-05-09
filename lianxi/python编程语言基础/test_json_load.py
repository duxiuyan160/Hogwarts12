import json
def test_load():
    #load 把文件打开从字符串转换成json
    jsobj = json.load(open("datas/test.json","r"))
    print(jsobj)
    print(type(jsobj))
    print(jsobj[0]['itemId'])