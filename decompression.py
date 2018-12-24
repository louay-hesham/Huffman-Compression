import time

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
  return 0;