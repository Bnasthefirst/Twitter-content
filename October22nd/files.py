# Opening a file in read mode (default mode)
file = open('Bnas.txt', 'r')

# Open a file in write mode (overwrites if file exists)
file = open('Bnas.txt', 'w')

# Open a file in append mode (adds to the end of the file)
file = open('Bnas.txt', 'a')

# It's good practice to close the file after opening it
file.close()



with open('Bnas.txt', 'r') as file:
  content = file.read()
  print(content)

with open('Bnas.txt', 'r') as file:
  for line in file:
      print(line)




with open('Bnas.txt', 'r') as file:
  content = file.read(10)  # Read first 10 characters
  print(content)


with open('Bnas.txt', 'w') as file:
  file.write('This will overwrite the file.')


with open('example.txt', 'a') as file:
  file.write('\nThis will append to the file.')
