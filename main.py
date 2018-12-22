from compression import compress
from decompression import decompress

# For testing
# compress("bee_movie_script.txt")
# decompress("bee_movie_script.txt.compressed")

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