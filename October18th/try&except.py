try:
  # Code that might raise an exception
  risky_code()
except SomeException as e:
  # Code that runs if an exception occurs
  print(f"An error occurred: {e}")

try:
  result = 10 / 0
except ZeroDivisionError as e:
  print(f"Error: {e}")


try:
  num = int(input("Enter a number: "))
  result = 10 / num
except (ValueError, ZeroDivisionError) as e:
  print(f"Error: {e}")



try:
  num = int(input("Enter a number: "))
  result = 10 / num
except ZeroDivisionError:
  print("You can't divide by zero!")
except ValueError:
  print("You must enter a valid number!")
else:
  print(f"Result: {result}")
finally:
  print("This runs no matter what.")
