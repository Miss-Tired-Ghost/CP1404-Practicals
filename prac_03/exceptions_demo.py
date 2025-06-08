"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When either input is unable to be converted to an integer.
    eg. apples, $200, 200.10, None
2. When will a ZeroDivisionError occur?
    When the divisor is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    You can avoid the ZeroDivisionError call by using the LBYL framework.
    This still won't avoid the fact a 0 divisor is uncomputable.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # LBYL Version
    # if denominator != 0:
    #     fraction = numerator / denominator
    #     print(fraction)
    # else:
    #     print("Cannot divide by zero!")

    fraction = numerator / denominator      # remove if LBYL
    print(fraction)                         # remove if LBYL
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
