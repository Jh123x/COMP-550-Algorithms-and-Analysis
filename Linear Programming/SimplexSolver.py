from typing import List
from z3 import Solver, Real, sat
from EqnTools import Variable, Constant, Equation, ObjFunction


class SimplexSolver:
    def __init__(self, obj_func: ObjFunction, eqns: List[Equation] = []):
        """Linear Programming Solver using Simplex Algorithm"""
        self.eqns = eqns
        self.obj_func = obj_func
        self.variables = set(obj_func.varnames)
        for eqn in eqns:
            self.variables.update(eqn.vars)
        self.solution = None

    def add_eqn(self, eqn: Equation):
        """Add a new equation to the system"""
        self.eqns.append(eqn)

    def terminating_cond(self) -> bool:
        """Check if terminating condition is met"""

        # Check if variable is satisfied in constraints
        result = [eqn.to_z3() for eqn in self.eqns] + \
            [Real(var) >= 0 for var in self.variables]
        solver = Solver()
        r = solver.check(result)

        # Check if objective function is satisfied
        return r == sat and self.obj_func.get_max_coeff().coeff <= 0

    def solve(self):
        """Solve the system"""
        # While not solved
        while not self.terminating_cond():
            # Simplex algorithm
            # TODO
            pass

        # Return the solution
        self.solution = self.obj_func.simplify().get_constant()
        return self.solution
