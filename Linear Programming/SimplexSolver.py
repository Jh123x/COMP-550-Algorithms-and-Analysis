from typing import List, Tuple
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

    def add_eqn(self, eqn: Equation):
        """Add a new equation to the system"""
        self.eqns.append(eqn)

    def __satisfy_eqns(self):
        result = [eqn.to_z3() for eqn in self.eqns] + \
            [Real(var) >= 0 for var in self.variables]
        solver = Solver()
        r = solver.check(result)
        return r == sat

    def terminating_cond(self) -> bool:
        """Check if terminating condition is met"""

        # Check if objective function is satisfied
        max_coeff = self.obj_func.get_max_coeff()
        return self.__satisfy_eqns() and (isinstance(max_coeff, Constant) or max_coeff.coeff <= 0)

    def find_pivot(self) -> Tuple[Variable, Equation]:
        """Find the pivot and the most restrictive eqn for pivot"""
        max_var = self.obj_func.get_max_coeff()
        max_eqn = None
        for eqn in self.eqns:
            if max_var.name not in eqn.vars:
                continue
            if max_eqn is None:
                max_eqn = eqn
                continue
            eqn1_max = eqn.get_max_value_of_var(max_var.name)
            eqn2_max = max_eqn.get_max_value_of_var(max_var.name)
            if eqn1_max < eqn2_max:
                max_eqn = eqn

        return max_var, max_eqn

    def solve(self):
        """Solve the system"""
        # While not solved
        while not self.terminating_cond():
            max_var, eqn = self.find_pivot()
            print(f"Obj F: {self.obj_func}\nEntering var: {max_var}, Eqn: {eqn}")
            print('Eqns: ' + '\n'.join([str(eqn) for eqn in self.eqns]), end="\n\n============================\n")

            if eqn is None:
                break

            # Pivot eqn around max_var
            new_eqn = eqn.make_subject(max_var.name)
            self.eqns.remove(eqn)
            new_constraints = [new_eqn]

            # Substitute it into the rest of the eqn
            for eqn in self.eqns:
                curr_sub = eqn.rhs[0]
                new_eqn = eqn.substitute(new_eqn).simplify()
                try:
                    new_eqn = new_eqn.make_subject(curr_sub.name)
                except Exception:
                    pass
                new_constraints.append(
                    new_eqn
                )

            # Substitute it into the objective function
            self.obj_func = self.obj_func.substitute(new_eqn).simplify()
            self.eqns = new_constraints

        # Return the solution
        return self.obj_func.simplify().get_constant()


if __name__ == '__main__':
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
    print(r)
