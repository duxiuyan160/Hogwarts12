def test_dict():
    hogwarts_dict = {"a":1,"b":2}
    hogwarts_dict2 = dict(a=1,b=2)

    print(hogwarts_dict.keys())
    print(hogwarts_dict.values())
    print(hogwarts_dict.pop("a"))   #把字典中a的键值对取出来并删掉
    print(hogwarts_dict)            #删除掉上面执行的键值对，还剩余的元素
    print(hogwarts_dict.popitem())   #随机删除的键值对

    a = {}
    b = a.fromkeys([1,2,3],"a,b,c")
    print(b)