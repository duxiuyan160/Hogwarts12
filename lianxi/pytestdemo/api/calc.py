class Calc:
    # 加法api
    def add(self, a: int, b: int):
        return int(a + b)

    # 除法api
    def div(self, a, b):
        if b == 0:
            return None
        else:
            return a / b
