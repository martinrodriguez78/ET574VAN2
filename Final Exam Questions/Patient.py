class Patient:

    # __init__ sets up the Patients data when the object is created
    def __init__(self, name, Patient_id, Patient_diagnosis):
        self.name = name.title()      # .title() capitalizes the First Letter Of Each Word
        self.Patient_id = Patient_id  # Store the Patients' ID
        self.Patient_diagnosis = Patient_diagnosis  # Store the Patient's diagnosis

    # Patient_display() is a method that prints the Patient's info
    def Patient_display(self):
        print(f"Name: {self.name}")          # Prints name 
        print(f"ID: PT-{self.Patient_id}")    # Prints ID 
        print(f"Diagnosis: {self.Patient_diagnosis}")  # Prints diagnosis


# Create a patient object using the provided info
#patient1 = Patient("paddington bear", "1088")
patient2 = Patient("John Smith", "1025", "flu")

# Call Patient_display() to print the Patient's info
patient2.Patient_display()