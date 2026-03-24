#Calculate the BMI. Save the code as PE3_3.py.
#a) Prompt and request the input for height(cm) and weight(kg) from the console.
#b) Compute the body mass index and print it in three decimal places.
#Input text can be any content. Just make sure to precisely match the output format below.
#Hint: 𝐵𝑀𝐼 = 𝑤𝑒𝑖𝑔ℎ𝑡
#ℎ𝑒𝑖𝑔ℎ𝑡2 × 703
#Example Output:
#Please enter the height (in cm): 180
#Please enter the weight (in kg): 90.5
#BMI = 1.964
height = int(input("enter your height (in cm): "))
weight = int(input("enter your weight (in kg): ")) 
BMI = (weight // height**2) * 703
print(BMI)
 
