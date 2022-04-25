from typing import Any, List, Tuple

from CukooHashSet import CukooSet


Pair = Tuple[str, str]


class CukooHashMap(CukooSet):
    def __init__(self, curr: List[Tuple[str, str]] = {}) -> None:
        """A Hash map based on Cukoo hashing
            :param curr: Must be a list of tuples of Strings
        """
        for index, item in enumerate(curr):
            if len(item) == 2:
                continue
            raise ValueError(f"Invalid input at index {index}: {item}")
        super().__init__(curr)

    def __getitem__(self, key: str) -> Any:
        """Get the value of the key"""
        h1 = super()._get_hash1_of(key)
        h2 = super()._get_hash2_of(key)

        if h1 is None or h2 is None:
            return None

        if self.t1[h1][0] == key:
            return self.t1[h1][1]
        return self.t2[h2][1]

    def _get_hash1_of(self, pair: Tuple[str, Any]) -> int:
        return super()._get_hash1_of(pair[0])

    def _get_hash2_of(self, pair: Tuple[str, Any]) -> int:
        return super()._get_hash2_of(pair[0])

    def insert(self, pair: Tuple[str, Any]) -> bool:
        """Insert the key and value into the map"""
        key, value = pair
        if key in self:
            h1 = super()._get_hash1_of(key)
            h2 = super()._get_hash2_of(key)
            if self.t1[h1][0] == key:
                self.t1[h1] = (key, value)
                return True
            self.t2[h2] = (key, value)
            return True

        return super().insert((key, value))

    def remove(self, key: str) -> bool:
        """Remove key value pair"""
        if key not in self:
            return False

        h1 = super()._get_hash1_of(key)
        h2 = super()._get_hash2_of(key)
        self.just_rehash = False

        self.size -= 1
        if self.t1[h1] is not None and self.t1[h1][0] == key:
            self.t1[h1] = None
            return True
        self.t2[h2] = None
        return True

    def __initialize__(self, curr: List[Tuple[str, Any]]) -> None:
        """Initialize the map with the given list"""
        for k, v in curr:
            super().insert((k, v))

    def _contains(self, pair: str):
        """Check if the map contains the key"""
        return super()._contains(pair[0])

    def __contains__(self, key: str):
        """Check if the map contains the key"""
        h1 = super()._get_hash1_of(key)
        h2 = super()._get_hash2_of(key)

        if h1 is None or h2 is None:
            return False

        v1, v2 = self.t1[h1], self.t2[h2]
        return v1 is not None and v1[0] == key or v2 is not None and v2[0] == key

    def __len__(self):
        """Get the size of the map"""
        return super().__len__()