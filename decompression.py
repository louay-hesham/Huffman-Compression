
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


def decompress(filename):
  codes, data = decode_file(filename)
  print(codes)
  # Decompress and write to new file here