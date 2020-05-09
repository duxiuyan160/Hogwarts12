"""
1、计算1~100求和
2、加入分支结构实现1~100之间的偶数求和
3、使用python实现1~100之间的偶数求和
"""
def test_for():
    result = 0
    for i in range(101): #问题1  #for i in range(2,101,2):问题3
        if i%2 == 0: #问题2
            print(i)
            result = result+i
    print(result)

def test_while():
    a = 1
    while a==1:
        print("a==1")
        a = a+1
    else:
        print("a != 1")
        print(a)


def test_breakandcontinue():
    for i in range(1,10):
        if i ==5:
            continue
        print(i)





