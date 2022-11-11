from .sum import sum


def test_sum():
    assert sum(1, 2) == 3


def test_sum2():
    assert sum(3, 1) == 4
    
    
def test_sum3():
    assert sum(4, 1) == 5
