from .Variable import Variable


def test_variable_obj():
    """Test the Variable object"""
    var = Variable("x")
    assert var.name == "x"
    assert repr(var) == "x"

    var = Variable("x", 0)
    assert var.coeff == 0
    assert repr(var) == ""


def test_variable_addition():
    """Test the addition of variables"""
    var1 = Variable("x")
    var2 = Variable("y")
    try:
        var1 + var2
    except ValueError:
        pass
    else:
        assert False, "Cannot add 2 variables with different names"

    var3 = Variable("x")
    assert var1 + var3 == Variable("x", 2)

    var4 = Variable("x", -1)
    assert var4 + var3 == Variable("x", 0)
