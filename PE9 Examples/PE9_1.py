import math

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
# part B
if denominator == 0:
    print("Error: Denominator cannot be zero. Try again.")
else:
    remainder = math.fmod(numerator, denominator)
    print("The remainder is :", round(remainder)) 