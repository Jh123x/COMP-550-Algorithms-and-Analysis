from CukooHashing import CukooSet


def test_set_add_1_element():
    """Add 1 element to CukooSet"""
    mySet = CukooSet()
    assert mySet.insert("1")


def test_set_search_1_element():
    """Searching for element in cukoo set"""
    mySet = CukooSet()
    assert mySet.insert("1")
    assert mySet.contains("1")

def test_set_add_many_and_search_many():
    """Add many items"""
    items = [str(i) for i in range(100)]

    mySet = CukooSet()
    for item in items:
        assert mySet.insert(item)

    for item in items:
        assert mySet.contains(item)
        assert item in mySet

    for item in items:
        assert mySet.remove(item)
        assert not mySet.contains(item)
        assert item not in mySet