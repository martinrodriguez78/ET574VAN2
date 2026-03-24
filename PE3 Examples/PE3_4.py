#Sort three input numbers. Save the code as PE3_4.py.
#a) Prompt and request three integer numbers one by one from the console.
#b) Sort these numbers and print them from smallest to largest.
#Input text can be any content. Just make sure to precisely match the output format below.
#Hint: You can use the built in functions max() and min()
#Example Output:
#Please enter the first integer: 7
#Please enter the second integer: 8
#Please enter the third integer: 1
#Before sorting: 7 8 1
#After sorting: 1 7 8

#A
intOne = int(input("enter your first number: "))
intTwo = int(input("enter your second number: "))
intThree = int(input("enter your third number: "))

print(intOne, intTwo, intThree)
print(max(intOne,intTwo,intThree),intOne, min(intOne, intTwo, intThree) )
