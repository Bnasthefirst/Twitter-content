import random
print(random.random())  # e.g., 0.678945


print(random.randint(1, 10)) 
# e.g., 7 


print(random.uniform(1, 10)) 
# e.g., 4.5678


fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))
# e.g., "banana"


print(random.choices(fruits, k=2)) 
# e.g., ["apple", "cherry"]



deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)  # e.g., [3, 1, 5, 2, 4]



print(random.sample(fruits, 2)) 
# e.g., ["banana", "cherry"]



print(random.gauss(0, 1)) 
# e.g., 0.56789
