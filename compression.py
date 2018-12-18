from heapq import *
from frequency import Frequency

def count_characters(filename):
  with open(filename, "rb") as file:
    data = file.read()
    freq_dict = {}
    for byte in data:
      if byte in freq_dict:
        freq_dict[byte] += 1
      else:
        freq_dict[byte] = 1

    frequencies = []
    for key, value in freq_dict.items():
      frequencies.append(Frequency(key, value, None, None))
    return frequencies

def build_min_heap(frequencies):
  min_heap = []
  for f in frequencies:
    heappush(min_heap, f)

  heapify(min_heap)
  return min_heap

def build_huffman_tree(frequencies):
  min_heap = build_min_heap(frequencies)
  n = len(min_heap)
  for i in range(n - 1):
    left = heappop(min_heap)
    right = heappop(min_heap)
    internal_node = Frequency(None, left.freq + right.freq, left, right)
    heappush(min_heap, internal_node)
    heapify(min_heap)

  return heappop(min_heap)

def set_code(node, codes_dict):
  if node.left is None and node.right is None:
    codes_dict[node.byte] = node.code
    return

  if node.left is not None:
    node.left.code = node.code + "0"
    set_code(node.left, codes_dict)
  if node.right is not None:
    node.right.code = node.code + "1"
    set_code(node.right, codes_dict)

def get_huffman_codes(filename):
  frequencies = count_characters(filename )
  root = build_huffman_tree(frequencies)
  huffman_codes_dict = {}
  set_code(root, huffman_codes_dict)
  return huffman_codes_dict

def bitstring_to_byte(s):
  return int(s, 2)

def compress(filename):
  codes = get_huffman_codes(filename)
  with open(filename, "rb") as file:
    try:
      data = file.read()
    finally:
      file.close()

  binary_str = ''
  for byte in data:
    binary_str += codes[byte]

  temp_str = ''
  bytes_data = []
  for bit in binary_str:
    temp_str += bit
    if len(temp_str) == 8:
      bytes_data.append(bitstring_to_byte(temp_str))
      temp_str = '' 

  with open(filename + ".compressed", "wb") as file:
    file.write(bytearray(bytes_data))
    