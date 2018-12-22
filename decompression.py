
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
  print(data)
  # Decompress and write to
  compressed_text=""
  n = len(data)
  for t in data:
    if n == 1:
      compressed_text += '{0:b}'.format(t)
      break
    compressed_text += '{0:08b}'.format(t)
    n -= 1
    return compressed_text

def decode(compressed_text,codes):
  sub=[]
  out=[]
  x=0
  for y in range(len(compressed_text)):
      sub=compressed_text[x : y]
      if sub in codes:
          out.append(codes.get(sub))
          x=y
  print(out)

