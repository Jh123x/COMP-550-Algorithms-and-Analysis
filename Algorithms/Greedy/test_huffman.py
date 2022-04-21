from HuffmanCompression import huffman_compression_dict, compress, decompress

def test_huffman_compression_empty_string():
    assert huffman_compression_dict("") == {}


def test_huffman_compression_single_char():
    assert huffman_compression_dict("aaab") == {'a': '1', 'b': '0'}

def test_huffman_compression_multiple_char():
    assert huffman_compression_dict("aaabbbccccddddd") == {'a': '01', 'b': '00', 'c':'10', 'd': '11'}


def test_conpress_decompress():
    text = "Hello World!"
    huffman_dict = huffman_compression_dict(text)
    huffman = compress(huffman_dict, text)
    decompressed = decompress(huffman_dict, huffman)
    assert decompressed == text