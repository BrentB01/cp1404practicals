"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")  # ValueError occurs if this exception does not exist (non-integer input)
except ZeroDivisionError:
    print("Cannot divide by zero!")  # ZeroDivisionError occurs if this exception does not exist (0 denominator)
print("Finished.")

#  For this code, Zero division error is impossible. By adding an exception similar to above, 0 value denominator inputs will never return an error.