from .Variable import Variable
from .Constant import Constant
from .Equation import Equation


def test_eqn_obj_1_lhs_1_rhs():
    """Test the equation object"""
    lhs = [Variable("x")]
    rhs = [Constant(5)]
    eqn = Equation(lhs, rhs)
    assert repr(eqn) == "x = 5"


def test_eqn_empty_lhs():
    """Test the equation object"""
    lhs = []
    rhs = [Constant(5)]
    eqn = Equation(lhs, rhs)
    assert repr(eqn) == "0 = 5"


def test_eqn_more_vars():
    """Test the equation object"""
    lhs = [Variable("x"), Variable("y")]
    rhs = [Constant(5), Constant(7), Variable('x', -1)]
    eqn = Equation(lhs, rhs)
    assert repr(eqn) == "x + y = 5 + 7 + -x"

def test_simplify():
    """Test the simplify function"""
    lhs = [Variable("x"), Variable("y")]
    rhs = [Constant(5), Constant(7), Variable('x')]
    eqn = Equation(lhs, rhs)
    result = eqn.simplify()
    assert repr(result) == "y = 12"
    
def test_make_subject():
    lhs = [Variable("x"), Variable("y")]
    rhs = [Constant(12)]
    eqn = Equation(lhs, rhs)
    r = eqn.make_subject('x')
    assert repr(r) == "-y + 12.0 = x", r

def test_make_subject_complex():
    lhs = [Variable("x"), Variable("y", 3), Variable("z", 4)]
    rhs = [Constant(12)]
    eqn = Equation(lhs, rhs)
    r = eqn.make_subject('x')
    assert repr(r) == "-3.0y + -4.0z + 12.0 = x", r
    r2 = eqn.make_subject('y')
    assert repr(r2) == "-0.3333333333333333x + -1.3333333333333333z + 4.0 = y", r2


def test_get_max():
    lhs = [Variable("x"), Variable("y")]
    rhs = [Constant(5), Constant(7), Constant(12)]
    eqn = Equation(lhs, rhs)
    assert eqn.get_max_value_of_var('x') == Constant(24)
    assert eqn.get_max_value_of_var('y') == Constant(24)