import time

def decode_header_data(header):
  header_str = header.decode()
  header_data = header_str.split('#')
  huffman_codes = {}
  for data_item in header_data:
    data = data_item.split(':')
    if (len(data) == 2):
      huffman_codes[data[1]] = data[0]
  return huffman_codes

def decode_file(filename):
  with open(filename, "rb") as file:
    data = file.read()
    header_end = data.index(bytes('~'.encode()))
    header = data[0:header_end]
    actual_data = data[header_end:]
    codes = decode_header_data(header)
    return codes, actual_data

def byte_to_binary(byte):
  return format(byte,'08b')

def get_binary_string(codes, data):
  binary_str = ''
  for byte in data:
    binary_str += byte_to_binary(byte)
  return binary_str

def decode_binary_str(codes, binary_str):
  i = 0
  j = 1
  decoded_data = []
  while j < len(binary_str):
    temp_str = binary_str[i:j]
    if temp_str in codes:
      decoded_data.append(int(codes[temp_str]))
      i = j
      j += 1
    else:
      j += 1

  return bytearray(decoded_data)

def decompress(filename):
  t1 = time.time() * 1000
  codes, data = decode_file(filename)
  binary_str = get_binary_string(codes, data)
  decoded_data = decode_binary_str(codes, binary_str)

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