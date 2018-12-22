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
    return str(self.byte) + "\t\t" + str(self.freq) + "\t\t" + format(self.byte,'08b') + "\t" + self.code
