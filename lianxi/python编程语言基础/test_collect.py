def test_collet():
    a = {1,2,3}
    b = {1,4,5}
    print(type(a))
    print(type(b))

    print(a.union(b)) #并集
    print(a.intersection(b)) #交集
    print(a.difference(b)) #差集
    print(a.add("a"))

   #print({i for i in "asdawqeqopqwiaaaaaa"})
    #集合去重
    c = "asdawqeqopqwiaaaaaa"
    print(set(c))