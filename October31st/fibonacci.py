def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example usage:
n = 10
print(fibonacci(n))



#0
#1 
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
