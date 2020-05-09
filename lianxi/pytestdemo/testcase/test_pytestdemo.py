import pytest

class TestPytestDemo:
    def test_one(self):
        print("开始执行 test_one 方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two 方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a = 'hello'
        b = 'hello word'
        assert a in b

if __name__ == '__main__':
        #pytestdemo.main("-v -x TestPytestDemo")
        pytest.main(["-v","-s","TestPytestDemo"])
        #pytestdemo.main()