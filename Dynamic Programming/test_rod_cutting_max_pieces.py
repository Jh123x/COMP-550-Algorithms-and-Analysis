from RodCuttingMaxPieces import rod_cutting_max_pieces


def test_trivial_case():
    pieces = [1]
    length = 16
    result, dp = rod_cutting_max_pieces(pieces, length)
    assert result == length, f"{dp}"


def test_case_1():
    piece_size = [2, 3, 8]
    length = 15
    result, dp = rod_cutting_max_pieces(piece_size, length)
    assert result == 7, f"{dp}"


def test_case_2():
    piece_size = [2, 3, 5]
    length = 9
    result, dp = rod_cutting_max_pieces(piece_size, length)
    assert result == 4, f"{dp}"
