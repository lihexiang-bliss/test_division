import pytest


# -*- coding: utf-8 -*-

class TestDiv():

    def div(self, a, b):
        return round(a / b, 2)

    def setup_class(self):
        print('计算开始')

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize('a,b,expect', [
        [100, 10, 10], [100, 10.5, 9.52], [1.2, 0.3, 4], [10, 0, 'False'], [0, 10, 0],
        [-100, -10, 10], [100.5, -10, -10.05]])
    def test_div(self, a, b, expect):
        try:
            result = TestDiv.div(self, a, b)
            print(result)
        except ZeroDivisionError as e:
            result = 'False'
        finally:
            assert result == expect
