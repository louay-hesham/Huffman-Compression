from heapq import *
from frequency import Frequency
import time

def count_characters(filename):
  with open(filename, "rb") as file:
    data = file.read()
    file.close()
  freq_dict = {}
  for byte in data:
    if byte in freq_dict:
      freq_dict[byte] += 1
    else:
      freq_dict[byte] = 1

  frequencies = []
  for key, value in freq_dict.items():
    frequencies.append(Frequency(key, value, None, None))
  return frequencies, data

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
  frequencies, data = count_characters(filename)
  root = build_huffman_tree(frequencies)
  huffman_codes_dict = {}
  set_code(root, huffman_codes_dict)
  print("\n\nByte\t\tFrequency\tOld Code\tNew Code")
  frequencies.sort()
  for f in frequencies[::-1]:
    print(f)
  print("\n")
  return huffman_codes_dict, data

def bitstring_to_byte(s):
  return int(s, 2)

def create_header(codes, bits_length):
  header = str(bits_length) + ';'
  for key, value in codes.items():
    header += (str(key) + ':' + value + '#')
  header += '~'
  return bytearray(header.encode())

def compress(filename):
  t1 = time.time() * 1000
  codes, data = get_huffman_codes(filename)
  t2 = time.time() * 1000
  binary_str = ''
  bytes_data = []
  bits_length = 0
  for byte in data:
    binary_str += codes[byte]
    bits_length += len(codes[byte])
    if len(binary_str) >= 8:
      byte_str = binary_str[0:8]
      bytes_data.append(bitstring_to_byte(byte_str))
      binary_str = binary_str[8:]

  if len(binary_str) < 8 and len(binary_str) > 0:
    bytes_data.append(bitstring_to_byte(binary_str + '0'*(8 - len(binary_str))))

  t3 = time.time() * 1000
  header = create_header(codes, bits_length)
  t4 = time.time() * 1000
  c_ratio = (len(bytes_data) + len(header)) / len(data)
  print("Compression ratio = %.2f" %(c_ratio * 100) + "%")
  with open(filename + ".compressed", "wb") as file:
    file.write(header)
    file.write(bytearray(bytes_data))
    file.close()
  t5 = time.time() * 1000

  print("Time to read file and generate huffman codes: %d" %(t2 - t1) + " ms")
  print("Time to generate compressed binary data: %d" %(t3 - t2) + " ms")
  print("Time to generate header: %d" %((t4 - t3) * 1000) + " ns")
  print("Time to write compressed file to disk: %d" %((t5 - t4) * 1000) + " ns")
  print("Total time elapsed for compression: %.3f" %(t5 - t1) + " ms\n")
    
def compress_folder(foldername):
  return 0;