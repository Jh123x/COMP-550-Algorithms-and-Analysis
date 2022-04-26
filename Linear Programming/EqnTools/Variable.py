import z3

from typing import Any
from .NamedVariable import NamedVariable


class Variable(NamedVariable):
    COEFF_MAP = {
        1: "",
        -1: "-",
    }

    def __init__(self, name: str, coeff: int = 1) -> None:
        """Initialize the Variable"""
        super().__init__(name)
        self.coeff = coeff

    def to_z3(self) -> z3.Real:
        return z3.Real(self.name)

    def __neg__(self) -> 'Variable':
        """Negate the Variable"""
        return Variable(self.name, -self.coeff)

    def __truediv__(self, other: int) -> 'Variable':
        """Divide the variable"""
        return Variable(self.name, self.coeff / other)

    def __add__(self, other: Any):
        """Addition of the Variable"""
        if type(other) != Variable:
            raise TypeError(
                "Can only add Variable objects with Variable objects")
        if self.name != other.name:
            raise ValueError(
                "Can only add 2 variables with the same name")
        return Variable(self.name, self.coeff + other.coeff)

    def __eq__(self, other: Any) -> bool:
        """Equality of the Variable"""
        if type(other) != Variable:
            raise TypeError(
                "Can only compare Variable objects with Variable objects")
        return self.name == other.name

    def __repr__(self):
        """Representation of the Variable"""
        if self.coeff == 0:
            return ''
        coeff = self.COEFF_MAP.get(self.coeff, self.coeff)
        return f"{coeff}{self.name}"

    def __str__(self):
        """String representation of the Variable"""
        return repr(self)
