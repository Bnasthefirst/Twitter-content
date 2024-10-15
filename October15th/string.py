s = "Python"
print(s.upper())  # Output: PYTHON
print(s.lower())  # Output: python


s = "  Hello  "
print(s.strip())  # Output: Hello




s = "Hello World"
print(s.replace("World", "Amy"))  # Output: Hello Amy


s = "Python is fun"
print(s.split())  # Output: ['Python', 'is', 'fun']

words = ['Python', 'is', 'fun']
print(" ".join(words))  # Output: Python is fun



s = "Python"
print(s[0:2])  # Output: Py
print(s[-3:])  # Output: hon




s = "Python programming"
print(s.find("pro"))  # Output: 7

s = "banana"
print(s.count("a"))  # Output: 3


name = "Amy"
age = 30
print(f"My name is {name} and I am {age} years old.")




name = "Amy"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
