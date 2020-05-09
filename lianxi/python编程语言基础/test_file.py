def test_file():
    #f = open('txtfile','r')
    # print(f.read())
    # print(f.readable())
    # print(f.readline())
    #print(f.readlines())  #以列表的形式打印出来
    #f.close()


    with open("datas/txtfile","r") as f:
        while True:
            line = f.readline()
            if line:
                print(line)
            else:
                break
        #print(f.readlines())

