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


HASH_FAMILY = [
    hash,
    joaat_hash,
    myShittyHash,
]
