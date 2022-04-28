from LongestCommonSubseq import longest_common_subsequence, trace_table


def test_trivial_1_match():
    """One letter should match itself"""
    a1 = "A"
    result, sequence = longest_common_subsequence(a1, a1)
    assert result == 1
    assert sequence == ["A"]


def test_trivial_1_no_match():
    a1 = "A"
    a2 = "B"
    result, sequence = longest_common_subsequence(a1, a2)
    assert result == 0
    assert sequence == []


def test_case_1():
    a1 = ["A", "T", "C", "A", "C", "C", "T"]
    a2 = ["A", "T", "A", "A", "C", "T"]
    result, seq = longest_common_subsequence(a1, a2)
    assert result == 5
    assert seq == ["A", "T", "A", "C", "T"]

def test_case_2():
    a1 = "ABCDEFG"
    result, seq = longest_common_subsequence(a1, a1)
    assert result == len(a1)
    assert seq == list(a1)

def test_case_3():
    a1 = "ABCDEFG"
    a2 = "ABCEFG"
    result, seq = longest_common_subsequence(a1, a2)
    assert result == len(a2)
    assert seq == list(a2)

