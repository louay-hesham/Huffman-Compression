from compression import compress

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
    print("Not implemented yet")
    # filename = input("Enter filename: ")
    # decompress(filename)
  elif choice == '0':
    break
  else:
    print("Invalid choice")
  print("\n\n")