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
        self.vars = set(map(lambda x: x.name, filter(
            lambda x: isinstance(x, Variable), (self.lhs + self.rhs))))

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
                acc += -term
                continue
            if term.name not in terms:
                terms[term.name] = term
            else:
                terms[term.name] += term

        new_rhs = [acc]

        return Equation(list(filter(lambda x: x.coeff != 0, terms.values())), new_rhs)

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

        if s_term is None:
            raise Exception(f"No term {var_name} found")

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

    def substitute(self, eqn: 'Equation') -> 'Equation':
        """Substitute a variable for another variable
            eqn: Equation to substitute (Must have 1 ter on the rhs)
        """
        if len(eqn.rhs) != 1:
            raise Exception("Equation must have 1 term on the rhs")

        s_term = eqn.rhs[0]

        lhs = []
        rhs = []

        for term in self.lhs:
            if term.name == s_term.name and term.coeff != 0:
                lhs += list(map(lambda x: x*term.coeff /
                            s_term.coeff, eqn.lhs))
                continue
            lhs.append(term)

        for term in self.rhs:
            if term.name == s_term.name:
                rhs += list(map(lambda x: x*term.coeff /
                            s_term.coeff, eqn.lhs))
                continue
            rhs.append(term)

        return Equation(lhs, rhs)

    def get_max_value_of_var(self, var_name: str) -> Constant:
        """Get the maximum possible value of a string"""
        result = Constant(0)
        t_term = None
        for term in self.lhs:
            if isinstance(term, Constant):
                result += -term
                continue

            if term.name != var_name:
                continue

            if t_term is None:
                t_term = term
                continue

            t_term += term

        for term in self.rhs:
            if isinstance(term, Constant):
                result += term
                continue
            if term.name != var_name:
                continue

            if t_term is None:
                t_term = -term
                continue

            t_term += -term

        return Constant(result.value / t_term.coeff)
