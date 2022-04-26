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
        self.vars = set(map(lambda x: x.name, filter(lambda x: isinstance(x, Variable), (self.lhs + self.rhs))))

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

    def make_subject(self, var_name: str) -> 'Equation':
        """Make a subject variable"""
        curr = self.simplify()
        lhs = []
        s_term = None
        for term in curr.lhs:
            if term.name != var_name:
                lhs.append(term)
                continue
            s_term = term

        assert len(curr.rhs) == 1

        lhs.append(-curr.rhs[0])
        coeff = -s_term.coeff
        rhs = [Variable(s_term.name)]

        return Equation(list(map(lambda x: x/coeff, lhs)), rhs)

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

    def to_z3(self):
        arr1 = list(map(lambda x: x.to_z3(), self.lhs))
        arr2 = list(map(lambda x: x.to_z3(), self.rhs))
        return sum(arr1) == sum(arr2)

    def get_max_value_of_var(self, var_name: str) -> Constant:
        """Get the maximum possible value of a string"""
        result = Constant(0)
        t_term = None
        for term in self.lhs + self.rhs:
            if isinstance(term, Constant):
                result += term
                continue

            if term.name != var_name:
                continue

            if t_term is None:
                t_term = term
                continue

            t_term += term

        return Equation([t_term], [result]).make_subject(var_name).lhs[0]