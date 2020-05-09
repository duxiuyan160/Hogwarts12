def test_list():
    """
    list.append(x):在列表的末尾沫加一个元素。相当于a[len(a):] = [x]
    list.insert(i,x):在给定的位置插入一个元素。第一个参数是要插入的元素的索引，以a.insert(0,x)插入列表头部，a.insert(len(a),x) 等同于a.append
    list.remove(x):移除列表中第一个值为x的元素。如果没有这样的元素，则抛出ValueError异常
    list.pop([i]):删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop()将会删除并返回列表中的最后一个元素
    list.sort(key=None,reverse=False):对列表中的元素进行排序(参数可用于自定义排序，解释请参见 sorted())
    list.reverse():反转列表中的元素
    :return:
    """
    list_hogwarts = [1,5,4,6,3]
    list_hogwarts.append(0)
    list_hogwarts.insert(1,0)
    #list_hogwarts.remove(0)
    #y = list_hogwarts.pop()
    #list_hogwarts.sort(reverse=True)
    list_hogwarts.reverse()
    print(list_hogwarts.count(0))
    print(list_hogwarts)

def test_listandfor():
    """
    如果我们想生成一个平方列表，比如[1,4,9]，使用for循环应该怎么写，使用列表生成式又应该怎么写呢？
    :return:
    """
    list_square = []
    for i in range(1,5):
        list_square.append(i**2)
    print(list_square)

    list_square2 = [i**2 for i in range(1,5)]
    print("list_square",list_square2)

    list_square3 = [i*j for i in range(1,4) for j in range(1,4)]

