from collections import Counter

# Example with a list
data = ['a', 'b', 'a', 'c', 'b', 'a']
counter = Counter(data)
print(counter)


Counter({'a': 3, 'b': 2, 'c': 1})



print(counter['a'])  # Output: 3
print(counter['d'])  # Output: 0 (Returns 0 for elements not in the Counter)


print(counter.most_common(2))  # Output: [('a', 3), ('b', 2)]


counter1 = Counter(a=3, b=1)
counter2 = Counter(a=1, b=2)

# Adding two Counters
print(counter1 + counter2)  # Output: Counter({'a': 4, 'b': 3})

# Subtracting two Counters
print(counter1 - counter2)  # Output: Counter({'a': 2})

# Intersection (minimum of counts)
print(counter1 & counter2)  # Output: Counter({'a': 1, 'b': 1})

# Union (maximum of counts)
print(counter1 | counter2)  # Output: Counter({'a': 3, 'b': 2})
