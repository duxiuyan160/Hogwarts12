def test_exception():
    # try:
    #     num1 = int(input("输入一个除数"))
    #     num2 = int(input("输入一个被除数"))
    #     print(num1/num2)
    # # except:
    # #     print("这是一个通用异常")
    # except ZeroDivisionError:
    #     print("被除数不能为0")
    # except ValueError:
    #     print("输入的需要是数值型整数")
    # else:
    #     print("程序没有发生异常")
    # finally:
    #     print("无论发没发生异常，都扫行")
    x = 10
    if x > 5:
        raise "aa"