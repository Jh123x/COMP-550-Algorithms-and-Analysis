from EditDistance import edit_distance


def test_edit_distance_0():
    """2 words are the same"""
    word = "hello"
    assert edit_distance(
        word, word) == 0, "The same word has edit distance of 0"


def test_edit_distance_1():
    """Test edit distance of 1"""
    word1 = "Jay"
    word2 = "Joy"
    assert edit_distance(word1, word2) == 1

def test_edit_distance_long_words():
    word1 = "altruism"
    word2 = "plasma"
    assert edit_distance(word1, word2) == 6


def test_edit_distance_substring():
    """Test edit distance where one string is substring of another"""
    word1 = "part"
    word2 = "spartan"
    assert edit_distance(word1, word2) == 3
