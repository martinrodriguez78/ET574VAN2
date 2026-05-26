# Open the file 'email.txt' in write mode and assign it to the variable 'file'
with open("email.txt", "w") as file:  

    #Ask the user to type their email in the console and store it
    email = input("Enter your email address: ") 

    #Write the email to the file email.txt
    file.write(email)

    # Print the email to the console with the QCC EMAIL prefix
print(f"QCC EMAIL: " + email)  