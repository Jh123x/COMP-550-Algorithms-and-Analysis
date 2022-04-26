from EqnTools import Constant, Variable, Equation, ObjFunction
from SimplexSolver import SimplexSolver

def test_simplex_terminating_success():
    obj = ObjFunction([Constant(1), Variable('x', -1), Variable('y', -1)])
    eqn = Equation([Constant(1), Variable('x')], [Constant(1)])
    eqn1 = Equation([Variable('y')], [Constant(1)])
    eqn2 = Equation([Variable('x'), Variable('y')], [Constant(1)])
    solver = SimplexSolver(obj, [eqn, eqn1, eqn2])
    assert solver.terminating_cond()

def test_simplex_terminating_fail_constraint():
    obj = ObjFunction([Constant(1), Variable('x', -1), Variable('y', -1)])
    eqn = Equation([Constant(1), Variable('x')], [Constant(2)])
    eqn1 = Equation([Variable('y')], [Constant(1)])
    eqn2 = Equation([Variable('x'), Variable('y')], [Constant(1)])
    solver = SimplexSolver(obj, [eqn, eqn1, eqn2])
    assert not solver.terminating_cond()

def test_simplex_terminating_fail_obj():
    obj = ObjFunction([Constant(1), Variable('x'), Variable('y')])
    eqn = Equation([Variable('x')], [Constant(1)])
    eqn1 = Equation([Variable('y')], [Constant(2)])
    solver = SimplexSolver(obj, [eqn, eqn1])
    assert not solver.terminating_cond()