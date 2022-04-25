from UnionFindDisjointSet import UFDS

def test_ufds_for_items():
    ufds = UFDS(['a', 'b', 'c', 'd'])
    ufds.union('a', 'b')
    ufds.union('c', 'd')
    assert ufds.get_top('a') == 'a', f"{ufds.get_top('a')} != a"
    assert ufds.get_top('b') == 'a', f"{ufds.get_top('b')} != a"
    assert ufds.get_top('c') == 'c', f"{ufds.get_top('c')} != c"
    assert ufds.get_top('d') == 'c', f"{ufds.get_top('d')} != c"

    ufds.union('b', 'd')
    assert ufds.get_top('a') == 'a', f"{ufds.get_top('a')} != a"
    assert ufds.get_top('b') == 'a', f"{ufds.get_top('b')} != a"
    assert ufds.get_top('c') == 'a', f"{ufds.get_top('c')} != a"
    assert ufds.get_top('d') == 'a', f"{ufds.get_top('d')} != a"