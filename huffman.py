
class Frequency:
  def __init__(self, byte, freq):
    self.byte = byte
    self.freq = freq

  def __lt__(self, other):
    return self.freq < other.freq

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
      frequencies.append(Frequency(key, value))
    return frequencies

frequencies = count_characters("bee_movie_script.txt")
print(frequencies)