from typing import Any, List
from random import choices


def joaat_hash(key: str) -> int:
    """Joaat hash function"""
    hash = 0
    for char in key:
        hash += ord(char)
        hash += (hash << 10)
        hash ^= (hash >> 6)
    return hash


def myShittyHash(key: str):
    """My shitty hash function"""
    hash = 0
    for char in key:
        hash += ord(char)
    return hash


class CukooSet(object):
    HASH_FAMILY = [
        hash,
        joaat_hash,
    ]

    def __init__(self, curr: List[str] = {}) -> None:
        """A Hash set based on Cukoo hashing
            :param curr: Must be a list of Strings
        """
        self.t1 = [None] * 2
        self.t2 = [None] * 2
        self.hash1, self.hash2 = choices(self.HASH_FAMILY, k=2)
        self.size = 0
        self.array_size = 2
        self.__initialize(curr)

    def _get_hash1_of(self, key: str) -> int:
        if key is None:
            return None
        return self.hash1(key) % self.array_size

    def _get_hash2_of(self, key: str) -> int:
        if key is None:
            return None
        return self.hash2(key) % self.array_size

    def insert(self, item: str):
        """Insert an item into the set"""
        if item in self:
            return False

        isTable1 = True
        for _ in range(self.array_size):
            if isTable1:
                hash1 = self._get_hash1_of(item)
                if self.t1[hash1] is None:
                    self.t1[hash1] = item
                    self.size += 1
                    return True
                isTable1 = False
                self.t1[hash1], item = item, self.t1[hash1]
                continue

            hash2 = self._get_hash2_of(item)
            if self.t2[hash2] is None:
                self.t2[hash2] = item
                self.size += 1
                return True
            isTable1 = True
            self.t2[hash2], item = item, self.t2[hash2]

        # Table is full
        self.rehash_all()
        return self.insert(item)

    def rehash_all(self):
        """Rehash all the elements and double the space"""
        all_items = tuple(filter(lambda x: x is not None, self.t1 + self.t2))
        self.array_size *= 2
        self.t1 = [None] * self.array_size
        self.t2 = [None] * self.array_size
        self.__initialize(all_items)

    def __contains__(self, key: str):
        """Check if the key is in the set"""
        h1 = self._get_hash1_of(key)
        h2 = self._get_hash2_of(key)
        if h1 is None or h2 is None:
            return False

        return self.t1[h1] == key or self.t2[h2] == key

    def remove(self, key: str) -> bool:
        """Remove an element from a set"""
        if key not in self:
            return False

        hash1 = self._get_hash1_of(key)
        if self.t1[hash1] == key:
            self.t1[hash1] = None
            self.size -= 1
            return True

        hash2 = self._get_hash2_of(key)
        if self.t2[hash2] == key:
            self.t2[hash2] = None
            self.size -= 1
            return True

        return False

    def contains(self, key: str) -> bool:
        """Find the element"""
        return key in self

    def __initialize(self, curr: List[str]) -> None:
        """Initialize the set"""
        for item in curr:
            self.insert(item)

    def __len__(self) -> int:
        return self.size


if __name__ == '__main__':
    mySet = CukooSet()
    assert mySet.insert('1')
    assert mySet.insert('2')
    assert not mySet.insert('1')
    assert '1' in mySet
    assert '2' in mySet
    assert '3' not in mySet
    assert mySet.remove('2')
    assert not mySet.remove('2')

    for i in range(5, 10):
        assert mySet.insert(str(i)), i
