import main

def test_add():
    assert main.add(1, 2) == 3

def test_subtract():
    assert main.subtract(4, 2) == 2

def test_result():
    assert main.result == 25


def test_out1():
    assert main.out1 == 4, "Wrong answer dude!"
