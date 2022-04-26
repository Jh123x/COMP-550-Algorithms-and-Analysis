
from typing import Union, List

from .Variable import Variable
from .Constant import Constant
from .Equation import Equation


Numbers = Union[Variable, Constant]


class ObjFunction:
    def __init__(self, variables: List[Numbers] = []) -> None:
        """Objective Function to be maximized"""
        self.variables = variables
        self.varnames = set(map(lambda x: x.name, filter(lambda x: isinstance(x, Variable), self.variables)))

    def get_constant(self):
        """Get the constant value if everything else is 0"""
        r = Constant(0)
        for var in self.variables:
            if isinstance(var, Constant):
                r += var
        return r

    def simplify(self):
        """Simplify the objective function"""
        bucket = {}
        acc = Constant(0)
        for var in self.variables:
            if isinstance(var, Constant):
                acc += var
                continue
            if var.name not in bucket:
                bucket[var.name] = var
                continue
            bucket[var.name] += var
        variables = list(filter(lambda x: x.coeff !=
                         0, tuple(bucket.values())))
        if acc.value != 0:
            variables.append(acc)
        return ObjFunction(variables)

    def __repr__(self) -> str:
        """Print the objective function"""
        return "Maximize: " + " + ".join([str(var) for var in self.variables])

    def get_max_coeff(self) -> Variable:
        """Get the maximum coefficient for the current values"""
        if len(self.varnames) == 0:
            acc = Constant(0)
            for var in self.variables:
                acc += var
            return acc
        return max(filter(lambda x: isinstance(x, Variable), self.variables), key=lambda x: x.coeff)

    def substitute(self, other: Equation) -> 'ObjFunction':
        """Substitute the variables in the objective function
            eqn: Equation to substitute (Must have 1 term on the rhs)
        """
        if len(other.rhs) != 1:
            raise Exception("Equation must have 1 term on the rhs")

        s_term = other.rhs[0]
        
        new_vars = []
        for var in self.variables:
            if var.name == s_term.name and var.coeff != 0:
                new_vars += list(map(lambda x: x*var.coeff / s_term.coeff, other.lhs))
                continue
            new_vars.append(var)
        return ObjFunction(new_vars).simplify()
