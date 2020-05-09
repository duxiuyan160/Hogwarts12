#list
def test_list():
    list_a = [1,2,3,"a","b"]
    print(list_a[0])
    print(list_a[1])
    print(list_a[-1])
    print(list_a[-3])
    print(list_a[0:3])

#if elif else
def test_ifelse():
    a = 3
    if a==0:
        print("a=0")
    elif a==1:
        print("a=1")
    elif a==2:
        print("a=2")
    else:
        print("a不等于0、1、1")
#分支
def test_fenzhi():
    x = -2
    if x>1:
        y=3*x-5
    else:
        if x>=-1:
            y = x+2
        else:
            y=5*x+3
    print (y)
#param
def methon(*daf):
    """
    :param a:
    :param b:
    :return:
    """
    print(daf[0])
    print(daf[1])
    print(daf[2])
    print(daf[3])
def test_method():
    print(test_aa(2))

def test_aa():
     y = lambda x:x*2