from calc import Calculator


def test_add():
    calc = Calculator()
    calc.add(5)
    assert calc.get_current == 5


def test_subtract():
    calc = Calculator()
    calc.subtract(10)
    assert calc.get_current == -10


def test_multiply():
    calc = Calculator()
    calc.subtract(5)
    calc.multiply(5)
    assert calc.get_current == -25


def test_divide():
    calc = Calculator()
    calc.add(1)
    calc.divide(2)
    assert calc.get_current == 0.5


def test_root():
    calc = Calculator()
    calc.add(4)
    calc.root()
    assert calc.get_current == 2
