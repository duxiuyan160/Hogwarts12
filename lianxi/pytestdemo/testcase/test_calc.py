import math

import pytest
import yaml

from lianxi.pytestdemo.api.calc import Calc


class TestCalc:
    # setup里实例化Calc api  ,测试方法中每个都需要调用
    def setup(self):
        self.calc = Calc()

    # 参数化测试用例，测试self.calc.add api
    @pytest.mark.parametrize("a,b,c", yaml.safe_load(open("./data/add_data.yaml")))
    def test_add(self, a, b, c):
        assert self.calc.add(a, b) == c

    @pytest.mark.parametrize("a,b,c",yaml.safe_load(open("./data/div_data.yaml")))
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c
