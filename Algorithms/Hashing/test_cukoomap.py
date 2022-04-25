import pytest

from CukooHashMap import CukooHashMap

KEY_VALUE1 = ("key1", "value1")
KEY_VALUE2 = ("key2", "value2")


def test_insertion_one_value():
    """Test the insertion of one value"""
    cukoo_map = CukooHashMap()
    cukoo_map.insert(KEY_VALUE1)
    assert cukoo_map[KEY_VALUE1[0]] == KEY_VALUE1[1]


def test_override_same_key_value():
    """Test the insertion and update of one value"""
    cukoo_map = CukooHashMap()
    cukoo_map.insert(KEY_VALUE1)
    assert cukoo_map[KEY_VALUE1[0]] == KEY_VALUE1[1]
    cukoo_map.insert(KEY_VALUE2)
    assert cukoo_map[KEY_VALUE2[0]] == KEY_VALUE2[1]
    assert len(cukoo_map) == 2


def test_searching_for_value():
    """Test to see if the key exists"""
    cukoo_map = CukooHashMap()
    cukoo_map.insert(KEY_VALUE1)
    assert KEY_VALUE1[0] in cukoo_map
    assert len(cukoo_map) == 1


def test_insert_and_remove():
    """Test inserting and removal"""
    cukoo_map = CukooHashMap()
    cukoo_map.insert(KEY_VALUE1)
    assert cukoo_map[KEY_VALUE1[0]] == KEY_VALUE1[1]

    cukoo_map.remove(KEY_VALUE1[0])

    assert len(cukoo_map) == 0, f"{cukoo_map.t1} {cukoo_map.t2}"
    assert KEY_VALUE1[0] not in cukoo_map

def test_insert_and_remove_a_lot_of_values():
    """Test to see if rehash is correct exists"""
    cukoo_map = CukooHashMap()
    size = 50
    for i in range(size):
        i_s = str(i)
        cukoo_map.insert((i_s, i_s))

        for k in range(i + 1):
            k_s = str(k)
            assert cukoo_map[k_s] == k_s
            assert k_s in cukoo_map

    assert len(cukoo_map) == size

    curr_size = size
    for i in range(size):
        i_s = str(i)
        cukoo_map.remove(i_s)
        curr_size -= 1
        assert len(cukoo_map) == curr_size
        assert i_s not in cukoo_map
    
    len(cukoo_map) == 0
    