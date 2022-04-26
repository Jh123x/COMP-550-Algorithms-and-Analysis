from .ObjectiveFunction import ObjFunction
from .Variable import Variable
from .Constant import Constant
from .Equation import Equation


def test_objfunc():
    """Test the objective function"""
    variables = [Variable("x"), Variable("y")]
    objfunc = ObjFunction(variables)
    assert repr(objfunc) == "Maximize: x + y"


def test_objfunc_simplify():
    """Test the objective function"""
    variables = [Variable("x"), Variable("y"), Variable('x', -1), Constant(100), Constant(-100)]
    objfunc = ObjFunction(variables)
    assert repr(objfunc.simplify()) == "Maximize: y"

def test_objfunc_get_max():
    """Test the objective function"""
    variables = [Variable("x"), Variable("y", 2), Constant(100)]
    objfunc = ObjFunction(variables)
    assert repr(objfunc.simplify()) == "Maximize: x + 2y + 100"
    assert repr(objfunc.get_max_coeff()) == "2y"

def test_objfunc_substitute():
    """Test the substitute function"""
    variables = [Variable("x"), Variable("y"), Constant(13)]
    objfunc = ObjFunction(variables)
    eqn1 = Equation([Constant(12)], [Variable('x')])
    assert repr(objfunc.substitute(eqn1)) == "Maximize: y + 25"

def test_objfunc_substitute_hard():
    """Test the substitute function"""
    variables = [Variable("x", 0.5), Variable("y"), Constant(13)]
    objfunc = ObjFunction(variables)
    eqn1 = Equation([Constant(12), Variable('y', 12)], [Variable('x')])
    assert repr(objfunc.substitute(eqn1)) == "Maximize: 7y + 19"
