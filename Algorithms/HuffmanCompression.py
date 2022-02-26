from math import log2
from pyclbr import Function
import time
from typing import Optional
from heapq import heapify, heappush, heappop


class Node(object):

    def __init__(self, freq: int, value: Optional[str] = None, left: 'Node' = None, right: 'Node' = None) -> None:
        """Get the frequency of the word"""

        # Check if it is a valid node
        if None in (left, right) and value is None:
            raise ValueError("Either nodes or value must be defined")

        if None not in (left, right) and value is not None:
            raise ValueError(
                f"Cannot define both left or right and value. Value: {value}, Left: {left}, Right: {right}")

        self.value = value
        self.freq = freq
        self.left = left
        self.right = right

    def merge(self, other: 'Node') -> 'Node':
        """Merge other node with current node"""
        return Node(self.freq + other.freq, left=self, right=other)

    def get_compressed_string(self, letter: str) -> Optional[str]:
        """Get the compressed string based on the tree"""

        # Leaf node
        if self.value is not None:
            return None if letter != self.value else ''

        # Not a leaf
        lresult = self.left.get_compressed_string(letter)
        if lresult is not None:
            return "0" + lresult
        rresult = self.right.get_compressed_string(letter)
        if rresult is not None:
            return "1" + rresult

        return None

    def __eq__(self, __o: object) -> bool:
        if type(__o) != type(self):
            return False
        return self.value == self.freq

    def __lt__(self, __o: object) -> bool:
        if type(__o) != type(self):
            raise ValueError(f"Cannot compare {type(self)} with {type(__o)}")
        return self.freq < __o.freq

    def __repr__(self) -> str:
        # Leaf
        if self.value is not None:
            return f"\tLeaf Node: '{self.value}': {self.freq}\n"

        # Node
        return f"""Node {self.freq}:\n{self.left}{self.right}"""


def get_frequency(text: str) -> dict:
    """Get word frequency from text"""
    freq_dict = {}
    for letter in text:
        freq_dict[letter] = freq_dict.get(letter, 0) + 1
    return freq_dict


def huffman_tree(text: str) -> Node:
    """Text data compression"""

    frequency = get_frequency(text)

    # Min heap with key (freq, value)
    min_heap = list(
        map(
            lambda x: Node(x[1], x[0]),
            frequency.items()
        )
    )
    heapify(min_heap)

    # Merge nodes
    while len(min_heap) > 1:
        min1 = heappop(min_heap)
        min2 = heappop(min_heap)
        new_node = min1.merge(min2)
        heappush(min_heap, new_node)

    return min_heap[0]


def huffman_compression_dict(text: str) -> dict[str, str]:
    """Compressions using huffman tree"""
    # Get tree
    tree = huffman_tree(text)

    # Get set of letters
    letter_set = set(text)

    # Encoding dict
    encoding_d = {}

    # Get encoding
    for letter in letter_set:

        result = tree.get_compressed_string(letter)
        if result is None:
            raise ValueError(f"Value not found in huffman tree {letter}")
        encoding_d[letter] = result

    return encoding_d


def conventional_compression_dict(text: str) -> dict[str, str]:
    """Compress the string using bits to represent them"""
    letters = list(set(text))

    # Get number of bits required to represent each character
    bits_required = log2(len(letters))
    if int(bits_required) != bits_required:
        bits_required = int(bits_required) + 1

    # Make encoding dict
    encode_d = {}

    # Assign bits to index
    for index, letter in enumerate(letters):
        encoded_val = bin(index)[2:]

        # Padding
        if len(encoded_val) < bits_required:
            encoded_val = "0" * (bits_required - len(encoded_val)) + encoded_val

        encode_d[letter] = encoded_val

    return encode_d


def compress(compress_dict: dict[str, str], text: str) -> str:
    # Compression
    acc = []
    for letter in text:
        acc.append(compress_dict[letter])

    return ''.join(acc)


def decompress(compress_dict: dict[str, str], encoded_text: str) -> str:
    # Invert dictionary
    decompress_dict = dict(map(lambda x: x[::-1], compress_dict.items()))

    index = 0
    length = 1
    buffer = []
    while index < len(encoded_text):
        curr = encoded_text[index: index+length+1]

        if index + length > len(encoded_text):
            raise ValueError(f"Error decoding: {buffer}, {curr}")

        if curr not in decompress_dict:
            length += 1
            continue

        buffer.append(decompress_dict[curr])
        index += length + 1
        length = 1

    return ''.join(buffer)
        


if __name__ == "__main__":
    text = "Hello world! This is the power of huffman encoding."
    print(f"Text to encode: {text}\n")

    start_time = time.time_ns()
    huffman_dict = huffman_compression_dict(text)
    huffman = compress(huffman_dict, text)
    huffman_time = time.time_ns() - start_time

    start_time = time.time_ns()
    conventional_dict = conventional_compression_dict(text)
    conven = compress(conventional_dict, text)
    conven_time = time.time_ns() - start_time

    print(f"Length of huffman compression result = {len(huffman)} Time taken: {huffman_time}ns")
    print(f"Length of conventional compression result = {len(conven)} Time taken: {conven_time}ns")

    print(f"Huffman decompress to text string: {decompress(huffman_dict, huffman)}")
    print(f"Conventional decompress to text string: {decompress(conventional_dict, conven)}")
