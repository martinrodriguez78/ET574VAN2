#Calculates the amount of a server’s tip. Save the code as PE3_2.py.
#a) Prompt and request input the amount of the bill (in float) and the percentage of tip (in integer).
#b) Calculate, set the result to two decimal places and print the result.
#Input text can be any content. Just make sure to precisely match the output format below

billAmount = float(input("Enter the amount of the bill : $ "))
tip_Percentage = int(input("Enter the percentage of tip: "))
tipAmount = billAmount * tip_Percentage / 100
print ("$",round (tipAmount,2))