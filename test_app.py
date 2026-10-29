from app import calculate

def test_addition():
    assert calculate('add', 10, 5) == 15
    assert calculate('add', -1, 1) == 0

def test_subtraction():
    assert calculate('subtract', 10, 5) == 5
    assert calculate('subtract', 5, 10) == -5
