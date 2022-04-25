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
