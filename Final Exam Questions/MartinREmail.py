with open("email.txt", "w") as file:  

    #Ask the user to type their name & email in the console and store it
    name = input("Enter your full name: ")
    email = input("Enter your email address: ") 

    #Write the email to the file email.txt
    file.write(email)

    # Print the email to the console with the QCC EMAIL prefix
print(name.title())
print(f"QCC EMAIL: {email}")  