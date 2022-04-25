from typing import List, Union
from .Constant import Constant
from .Variable import Variable

Numbers = Union[Constant, Variable]


class Equation(object):
    def __init__(self, lhs: List[Numbers], rhs: List[Numbers]) -> None:
        """
        lhs: left hand side of the equation
        rhs: right hand side of the equation
        """
        self.lhs = lhs
        self.rhs = rhs

    def simplify(self) -> 'Equation':
        """Simplify the equation"""
        terms = {}

        # Add all the constants together
        acc = Constant(0)
        for term in self.rhs:
            if isinstance(term, Constant):
                acc += term
                continue
            if term.name not in terms:
                terms[term.name] = -term
            else:
                terms[term.name] += -term

        for term in self.lhs:
            if isinstance(term, Constant):
                acc += term
                continue
            if term.name not in terms:
                terms[term.name] = term
            else:
                terms[term.name] += term

        new_rhs = [acc]
            
        return Equation(list(terms.values()), new_rhs)

    def __repr__(self):
        """Representation of the Equation"""
        lhs = 0
        rhs = 0
        if len(self.lhs):
            lhs = ' + '.join(filter(lambda x: len(x) > 0, map(str, self.lhs)))
        if len(self.rhs):
            rhs = ' + '.join(filter(lambda x: len(x) > 0, map(str, self.rhs)))
        return f"{lhs} = {rhs}"

    def __str__(self):
        """String representation of the Equation"""
        return repr(self)
