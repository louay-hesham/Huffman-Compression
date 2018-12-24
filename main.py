from compression import compress, compress_folder
from decompression import decompress, decompress_folder

# For testing
foldername = "test/"
compress_folder(foldername)

# Main code

# while True:
#   print("Choose an option:")
#   print("1- Compress a file")
#   print("2- Decompress a file")
#   print("3- Compress a folder")
#   print("4- Decompress a folder")
#   print("0- Exit")
#   choice = input("Choice > ")
#   if choice == '1':
#     filename = input("Enter filename: ")
#     compress(filename)
#   elif choice == '2':
#     filename = input("Enter filename: ")
#     decompress(filename)
#   elif choice == '3':
#     foldername = input("Enter folder name: ")
#     compress_folder(foldername)
#   elif choice == '4':
#     foldername = input("Enter folder name: ")
#     decompress_folder(foldername)
#   elif choice == '0':
#     break
#   else:
#     print("Invalid choice")
#   print("\n\n")