from .Constant import Constant


def test_constant_obj():
    """Test the Constant object"""
    const = Constant(5)
    assert const.name == "Constant"
    assert const.value == 5
    assert repr(const) == "5"


def test_constant_addition():
    """Test the addition of constants"""
    const1 = Constant(5)
    const2 = Constant(7)
    assert const1 + const2 == Constant(12)
    assert const1 + const2 == 12

def test_constant_multiplication():
    """Test the multiplication of constants"""
    const1 = Constant(5)
    const2 = Constant(7)
    result = Constant(35)
    assert repr(const1 * 7) == repr(result)
    assert repr(const2 * 5) == repr(result)

def test_constant_division():
    """Test the division of constants"""
    const1 = Constant(5)
    const2 = Constant(7)
    result = Constant(2.5)
    result2 = Constant(3.5)

    assert repr(const1 / 2) == repr(result)
    assert repr(const2 / 2) == repr(result2)
