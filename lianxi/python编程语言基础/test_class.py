class TestClass:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def eat(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender} 我在吃")
    def drink(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender} 我在喝")
    def run(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender} 我在跑")
def test_aa():
    xiaoming = TestClass("xiaoming",10,"male")
    xiaohong = TestClass("xiaohong",10,"female")
    print(xiaoming.name)
    xiaoming.run()
    xiaohong.eat()
    #def test_class(self):
        #print("aa")
        # p = TestClass()
        # print(p.name)
        # print(p.get_name())
        # p.name = "duxiuyan"
        # TestClass.name = "shixiaojun"  #如果实例变量已修改，即使再修改类变量，也不影响实例变量的值
        # print(p.name)
        # name = "noname"
        # def get_name(self):
        #     return self.name






