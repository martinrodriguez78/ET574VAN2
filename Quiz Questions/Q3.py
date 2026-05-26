#lines 2-8 satisfy q1
class ETStudent:

    # __init__ sets up the student's data when the object is created
    def __init__(self, name, student_id):
        self.name = name.title()      # .title() capitalizes the First Letter Of Each Word
        self.student_id = student_id  # Store the student ID
#lines 9-12 satisfy q2
    # student_display() is a method that prints the student's info
    def student_display(self):
        print(f"Name: QCC-ET-{self.name}")          # Prints name with prefix
        print(f"ID:   QCC-ET-{self.student_id}")    # Prints ID with prefix

#lines 15-19 satisfy q3
# --- Create a student object using the provided info ---
student1 = ETStudent("MARTIN RODRIGUEZ", "208016766")

# --- Call student_display() to print the student's info ---
student1.student_display()