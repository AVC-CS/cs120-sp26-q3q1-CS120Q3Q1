import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # Input: 1.0 -1.0 -6.0 → roots 3.00 -2.00
    content = open('result1.txt').read()
    print(content)
    regex_test([r'3\.00', r'-2\.00'], content)


@pytest.mark.T2
def test_main_2():
    # Input: 2 4 -6 → roots 1.00 -3.00
    content = open('result2.txt').read()
    print(content)
    regex_test([r'1\.00', r'-3\.00'], content)


@pytest.mark.T3
def test_main_3():
    # Input: 1 -5 6 → roots 3.00 2.00
    content = open('result3.txt').read()
    print(content)
    regex_test([r'3\.00', r'2\.00'], content)


@pytest.mark.T4
def test_main_4():
    # Input: 1 -3 2 → roots 2.00 1.00
    content = open('result4.txt').read()
    print(content)
    regex_test([r'2\.00', r'1\.00'], content)
