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

def test_simplify_hard():
    """Test the simplify function"""
    lhs = [Variable("x"), Variable("y"), Constant(-10)]
    rhs = [Constant(-5), Constant(7), Variable('x')]
    eqn = Equation(lhs, rhs)
    result = eqn.simplify()
    assert repr(result) == "y = 12"


def test_make_subject():
    lhs = [Variable("x"), Variable("y")]
    rhs = [Constant(-3)]
    eqn = Equation(lhs, rhs)
    r = eqn.make_subject('x')
    assert repr(r) == "-y + -3 = x", r
    r = eqn.simplify().make_subject('x')
    assert repr(r) == "-y + -3 = x", r
    r2 = r.simplify().make_subject('y')
    assert repr(r2) == "-x + -3 = y", r2


def test_make_subject_complex():
    lhs = [Variable("x"), Variable("y", 3), Variable("z", 4)]
    rhs = [Constant(-12)]
    eqn = Equation(lhs, rhs)
    r = eqn.make_subject('x')
    assert repr(r) == "-3y + -4z + -12 = x", r
    r2 = eqn.make_subject('y')
    assert repr(
        r2) == "-0.3333333333333333x + -1.3333333333333333z + -4 = y", r2


def test_get_max():
    lhs = [Variable("x"), Variable("y")]
    rhs = [Constant(5), Constant(7), Constant(12)]
    eqn = Equation(lhs, rhs)
    assert eqn.get_max_value_of_var('x') == Constant(24)
    assert eqn.get_max_value_of_var('y') == Constant(24)

def test_get_max_hard():
    lhs = [Variable('x', -1/3), Constant(4)]
    rhs = [Constant(5)]
    eqn = Equation(lhs, rhs)
    assert repr(eqn) == '-0.3333333333333333x + 4 = 5'
    assert eqn.get_max_value_of_var('x') == Constant(-3)

def test_get_max_diff():
    lhs = [Variable("x", -1/3), Constant(4)]
    rhs = [Constant(0)]
    eqn = Equation(lhs, rhs)
    assert eqn.get_max_value_of_var('x') == Constant(12)


def test_substitute_simple():
    lhs = [Variable('x')]
    rhs = [Constant('y')]
    eqn = Equation(lhs, rhs)
    assert repr(eqn) == 'x = y'
    eqn2 = Equation([Variable('z'), Constant(12)], [Variable('x')])
    r = eqn.substitute(eqn2)
    assert repr(r) == 'z + 12 = y'


def test_substitution_hard():
    lhs = [Variable('x')]
    rhs = [Variable('y'), Constant(5), Variable('z', -1)]
    eqn = Equation(lhs, rhs)
    assert repr(eqn) == 'x = y + 5 + -z'
    eqn2 = Equation([Variable('z')], [Variable('x')])
    r = eqn.substitute(eqn2).simplify()
    assert repr(r) == '-y + 2z = 5'
