import os

def test_os():
    #os.mkdir("testdir") #创建目录
    # print(os.listdir("./")) #列出当前目录下的文件
    # os.removedirs("testdir") #删除目录
    # print(os.getcwd()) #获取当前目录

    #判断当前目录下是否有b目录，如果没有则创建；判断b目录下是否有text.txt文件，如果没有则创建text.txt文件并写入内容
    if not os.path.exists("b"):
        os.mkdir("b")
    if not os.path.exists("b/text.txt"):
        # f = open("b/text.txt","w")
        # f.write("hello duxiuyan")
        # f.close()
        with open("b/text.txt","w") as f:
            f.write("hello duxiuyan and duxiuyan")

