from compression import compress
from decompression import decompress

# For testing
# compress("Awaken.flac")
# decompress("Awaken.flac.compressed")

while True:
  print("Choose an option:")
  print("1- Compress a file")
  print("2- Decompress a file")
  print("0- Exit")
  choice = input("Choice > ")
  if choice == '1':
    filename = input("Enter filename: ")
    compress(filename)
  elif choice == '2':
    filename = input("Enter filename: ")
    decompress(filename)
  elif choice == '0':
    break
  else:
    print("Invalid choice")
  print("\n\n")