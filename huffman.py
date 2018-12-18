from heapq import *

class Frequency:
  def __init__(self, byte, freq, left, right):
    self.byte = byte
    self.freq = freq
    self.left = left
    self.right = right
    self.code = ''

  def __lt__(self, other):
    return self.freq < other.freq

  def __str__(self):
    return "(" + str(self.byte) + ": " + str(self.freq) + ", " + self.code + ")"

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

huffman_codes = []

def set_code(node):
  if node.left is None and node.right is None:
    huffman_codes.append(node)
    return

  if node.left is not None:
    node.left.code = node.code + "0"
    set_code(node.left)
  if node.right is not None:
    node.right.code = node.code + "1"
    set_code(node.right)

frequencies = count_characters("bee_movie_script.txt")
root = build_huffman_tree(frequencies)
set_code(root)
huffman_codes.sort()
huffman_codes = reversed(huffman_codes)
for h in huffman_codes:
  print(h)
