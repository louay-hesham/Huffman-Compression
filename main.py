from compression import compress, compress_folder
from decompression import decompress, decompress_folder

# For testing
# filename = "HuffmanInput.txt"
# compress(filename)
# decompress(filename + ".compressed")

# from os import listdir
# from os.path import isfile, join
# mypath = 'images/'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# for f in onlyfiles:
#   filename = mypath + f
#   print(filename)
#   compress(filename)
#   decompress(filename + ".compressed")

# Main code

while True:
  print("Choose an option:")
  print("1- Compress a file")
  print("2- Decompress a file")
  print("3- Compress a folder")
  print("4- Decompress a folder")
  print("0- Exit")
  choice = input("Choice > ")
  if choice == '1':
    filename = input("Enter filename: ")
    compress(filename)
  elif choice == '2':
    filename = input("Enter filename: ")
    decompress(filename)
  if choice == '3':
    foldername = input("Enter folder name: ")
    compress_folder(foldername)
  elif choice == '4':
    foldername = input("Enter folder name: ")
    decompress_folder(foldername)
  elif choice == '0':
    break
  else:
    print("Invalid choice")
  print("\n\n")