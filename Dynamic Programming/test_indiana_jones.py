from IndianaJones import indiana_jones


def test_trivial_case():
    ladder_size = [1]
    height = 1
    assert indiana_jones(height, ladder_size) == 1


def test_case_1():
    ladder_size = [1, 5, 10]
    height = 6
    assert indiana_jones(height, ladder_size) == 3


def test_case_2():
    ladder_size = [1, 2, 5]
    height = 1
    assert indiana_jones(height, ladder_size) == 1


def test_case_2():
    ladder_size = [1, 2, 5]
    height = 3
    assert indiana_jones(height, ladder_size) == 3


def test_case_3():
    ladder_size = [1, 2, 5]
    height = 10
    assert indiana_jones(height, ladder_size) == 128


def test_case_4():
    ladder_size = [1, 2, 5]
    height = 18
    assert indiana_jones(height, ladder_size) == 9133


def test_case_5():
    ladder_size = [1, 2, 5]
    height = 21
    assert indiana_jones(height, ladder_size) == 45260


def test_case_6():
    ladder_size = [1, 2, 5]
    height = 27
    assert indiana_jones(height, ladder_size) == 1111508

def test_case_7():
    ladder_size = [1, 2, 5]
    height = 11
    assert indiana_jones(height, ladder_size) == 218