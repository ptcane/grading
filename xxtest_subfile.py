from scripts import subfile

def test_add():
    assert subfile.add(1, 2) == 3

def test_subtract():
    assert subfile.subtract(4, 2) == 2

def test_result():
    assert subfile.result == 25


def test_out1():
    assert subfile.out1 == 4, "Wrong answer dude!"


def test_xx():
    assert subfile.xx == 45

def test_yy():
    assert subfile.yy == 47