"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when the input for numerator is not an integer.
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when the input for denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Add error checking to make sure the input for denominator is not 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero! Please enter a valid number.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")