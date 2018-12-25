import time
import os

def decode_header_folder_data(header):
  header_str = header.decode()
  folder_name = header_str.split('?')[0]
  bits_lengths_str = header_str.split('?')[1]
  bits_lengths = {}
  for data_item in bits_lengths_str.split('|')[:-1]:
    bits_lengths[data_item.split(':')[0]] = data_item.split(':')[1]
  
  header_data = header_str.split('?')[2].split('#')
  huffman_codes = {}
  for data_item in header_data:
    data = data_item.split(':')
    if (len(data) == 2):
      huffman_codes[data[1]] = data[0]
  
  return huffman_codes, bits_lengths

def decode_header_data(header):
  header_str = header.decode()
  bits_length = int(header_str.split(';')[0])
  header_data = header_str.split(';')[1].split('#')
  huffman_codes = {}
  for data_item in header_data:
    data = data_item.split(':')
    if (len(data) == 2):
      huffman_codes[data[1]] = data[0]
  return huffman_codes, bits_length

def decode_folder(folder):
  with open(folder, "rb") as file:
    data = file.read()
    file.close()
  header_end = data.index(bytes('~'.encode()))
  header = data[0:header_end]
  actual_data = data[header_end + 1:]
  codes, bits_lengths = decode_header_folder_data(header)
  return codes, actual_data, bits_lengths

def decode_file(filename):
  with open(filename, "rb") as file:
    data = file.read()
    header_end = data.index(bytes('~'.encode()))
    header = data[0:header_end]
    actual_data = data[header_end + 1:]
    codes, bits_length = decode_header_data(header)
    return codes, actual_data, bits_length

def byte_to_binary(byte):
  return format(byte,'08b')

def get_binary_string(codes, data):
  binary_str = ''
  for byte in data:
    binary_str += byte_to_binary(byte)
  return binary_str

def decode_binary_str(codes, binary_str, bits_length):
  i = 0
  j = 1
  decoded_data = []
  while j <= bits_length:
    temp_str = binary_str[i:j]
    if temp_str in codes:
      decoded_data.append(int(codes[temp_str]))
      i = j
    j += 1

  return bytearray(decoded_data)

def decompress(filename):
  t1 = time.time() * 1000
  codes, data, bits_length = decode_file(filename)
  binary_str = get_binary_string(codes, data)
  binary_str = binary_str[0:bits_length]
  decoded_data = decode_binary_str(codes, binary_str, bits_length)

  if filename.split('.')[-1] == 'compressed':
    filename = (filename.split('.')[:-1])
    filename.append('decompressed')
    filename = '.'.join(filename)
  else:
    filename += '.decompressed'

  with open(filename, 'wb') as file:
    file.write(decoded_data)
    file.close()
  t2 = time.time() * 1000
  print("Time elapsed: " + str(t2 - t1) + " ms")

def decompress_folder(foldername):
  t = time.time() * 1000
  t1 = t
  codes, total_data, bits_lengths = decode_folder(foldername)
  total_binary_str = get_binary_string(codes, total_data)
  old_i = 0
  foldername = foldername.split('.')[0]
  foldername += '_decompressed'
  if not os.path.isdir(foldername):
    os.mkdir(foldername)
  for filename, bits_length in bits_lengths.items():
    bits_length = int(bits_length)
    binary_str = total_binary_str[old_i: old_i + bits_length]
    old_i += bits_length
    decoded_data = decode_binary_str(codes, binary_str, bits_length)

    filename += '.decompressed'

    with open(foldername + '/' + filename, 'wb') as file:
      file.write(decoded_data)
      file.close()
    print("Time elapsed to decompress " + filename + ": %.3f" %(time.time() * 1000 - t1) + " ms")
    t1 = time.time() * 1000
  print("Total time to decompress folder: %.3f" %(time.time() * 1000 - t) + " ms")