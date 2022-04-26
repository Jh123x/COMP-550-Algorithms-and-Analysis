import pytest
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

@pytest.mark.timeout(1)
def test_simplex_solve_easy():
    """Easy simplex solve"""
    # x + y
    obj = ObjFunction([Variable('x'), Variable('y')])

    # x + y = 2
    eqn = Equation([Variable('x'), Constant(-2)], [Variable('y', -1)])

    # x - y = 0
    eqn1 = Equation([Variable('x')], [Variable('y')])

    solver = SimplexSolver(obj, [eqn, eqn1])
    r = solver.solve()
    assert r == 2

@pytest.mark.timeout(1)
@pytest.
def test_simplex_solve_hard():
    """Hard simplex solve"""
    # 4*x1 + 5*x2 + 6*x3​‌‌
    obj = ObjFunction(
        [Variable('x1', 4), Variable('x2', 5), Variable('x3', 6)])
    # 12 - x1 - 2 * x2 - 3*x3​‌‌
    eqn = Equation([Variable('x1', -1), Variable('x2', -2),
                   Variable('x3', -3), Constant(12)], [Variable('x4')])

    # 20 -3*x1 - x2 - 2*x3​‌‌
    eqn1 = Equation([Variable('x1', -3), Variable('x2', -1),
                    Variable('x3', -2), Constant(20)], [Variable('x5')])

    # 16 - 4*x1 -x2 -x3​‌‌
    eqn2 = Equation([Variable('x1', -4), Variable('x2', -1),
                    Variable('x3', -1), Constant(16)], [Variable('x6')])

    solver = SimplexSolver(obj, [eqn, eqn1, eqn2])
    r = solver.solve()
    assert r == 2/11 * (168 + 9/14 * 32)
