from .NamedVariable import NamedVariable


class Constant(NamedVariable):
    NAME = "Constant"
    ALLOWED_TYPES = (int, )
    CONVERSION_HANDLERS = {
        int: lambda self, other: Constant(self.value + other),
    }
    EQ_HANDLER = {
        int: lambda self, other: self.value == other,
    }

    def __init__(self, value: int) -> None:
        """Value of the constants"""
        super().__init__(self.NAME)
        self.value = value

    def __neg__(self) -> 'Constant':
        """Negation of the Constant"""
        return Constant(-self.value)

    def to_z3(self) -> int:
        """Convert to z3.Int"""
        return self.value

    def __truediv__(self, other: int) -> 'Constant':
        """Division of constants"""
        return Constant(self.value / other)

    def __add__(self, other) -> 'Constant':
        """Addition of constants"""
        if type(other) not in self.ALLOWED_TYPES and type(other) != Constant:
            raise TypeError("Can only add constants to constants or integers")

        if type(other) == Constant:
            return Constant(self.value + other.value)

        return self.CONVERSION_HANDLERS[type(other)](self, other)

    def __eq__(self, other):
        """Equality of constants"""
        if type(other) not in self.ALLOWED_TYPES and type(other) != Constant:
            raise TypeError(
                "Can only compare constants to constants or integers")
        if type(other) == Constant:
            return self.value == other.value
        return self.EQ_HANDLER[type(other)](self, other)

    def __repr__(self):
        """Representation of the Constant"""
        return f"{self.value}"

    def __str__(self) -> str:
        """String representation of the Constant"""
        return repr(self)
