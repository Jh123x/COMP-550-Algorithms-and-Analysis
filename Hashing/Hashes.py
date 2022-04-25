def joaat_hash(key: str) -> int:
    """Joaat hash function"""
    hash = 0
    for char in key:
        hash += ord(char)
        hash += (hash << 13)
        hash ^= (hash >> 7)
    return hash


def myShittyHash(key: str):
    """My shitty hash function"""
    start = 23
    for i in range(len(key)):
        start *= ord(key[i]) * 101
    return start


HASH_FAMILY = [
    hash,
    joaat_hash,
    myShittyHash,
]
