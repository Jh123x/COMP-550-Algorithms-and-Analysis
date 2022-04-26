from .ObjectiveFunction import ObjFunction
from .Variable import Variable
from .Constant import Constant


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
