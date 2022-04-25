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
    print(result, result.lhs, result.rhs)
    assert repr(result) == "y = 12"
    
