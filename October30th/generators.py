def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
for number in counter:
    print(number)


# the above code will print the following 

# 1
# 2
# 3
# 4
# 5



squares = (x * x for x in range(10))
for square in squares:
    print(square) 
