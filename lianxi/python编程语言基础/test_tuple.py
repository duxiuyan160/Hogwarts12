# 元组的定义
def test_tupledy():
    tuple_hogwarts = (1,2,3)
    tuple_hogwarts2= 1,2,3

    print("tuple_hogwarts",tuple_hogwarts)
    print(type(tuple_hogwarts))

    print("tuple_hogwarts2",tuple_hogwarts2)
    print(type(tuple_hogwarts2))

#元组的不可变特性   如果元组里面嵌套了列表，可以修改
def test_tuple():
    list_hogwarts = [1,2,3]
    list_hogwarts[0] = "a"
    print(list_hogwarts)

    a = [1,2,3]
    tuple_hogwarts = (1,2,'a',a)
    tuple_hogwarts[3][0] = "a"
    print(tuple_hogwarts)

    print(tuple_hogwarts.count("a"))
    print(tuple_hogwarts.index(2))