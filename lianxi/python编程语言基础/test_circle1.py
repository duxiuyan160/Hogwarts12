"""
    猜数字游戏
    计算机出一个1~100之间的随机数由人来猜
    计算机根据人猜的数字分别给出提示一个大一点/小一点/猜对了
    """
import random

person_nubmer = 0
computer_number = random.randint(1,100)
print(computer_number)
while True:
    person_nubmer = int(input("请输入一个数字"))
    if person_nubmer >computer_number:
        print("小一点")
    elif person_nubmer < computer_number:
        print("大一点")
    elif person_nubmer == computer_number:
        print("猜对了")
        break