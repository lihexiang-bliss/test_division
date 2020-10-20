# -*- coding: utf-8 -*-
import pytest, yaml


# 解析测试数据文件
def get_datas():
    with open('./datas/calc.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas


class TestCalc():
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()['add'])
    def test_calc_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', get_datas()['sub'])
    def test_calc_sub(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert result == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', get_datas()['mul'])
    def test_calc_mul(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert result == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', get_datas()['div'])
    def test_calc_div(self, get_calc, a, b, expect):
        try:
            result = get_calc.div(a, b)
        except ZeroDivisionError:
            result = 'False'
        finally:
            assert result == expect
