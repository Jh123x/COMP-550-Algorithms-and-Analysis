from typing import Any, List


class UFDS(object):
    def __init__(self, elements: List[Any]) -> None:
        """
        Union Find to check if they are part of the same set
        List of items
        """
        self.set = dict(map(lambda x: (x, None), elements))

    def get_top(self, elem: Any) -> Any:
        curr = elem

        while self.set[curr] != None:
            curr = self.set[curr]

        if curr != elem:
            self.set[elem] = curr

        return curr

    def union(self, elem1: Any, elem2: Any) -> None:
        """
        Union two sets
        """
        top1 = self.get_top(elem1)
        top2 = self.get_top(elem2)
        if top1 == top2:
            return

        self.set[top2] = top1


if __name__ == '__main__':
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
