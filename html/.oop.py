class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")


student1 = Student("Ali", 123, "AI")
student2 = Student("Sara", 456, "Computer")

print("Student 1:")
student1.introduce()

print("\nStudent 2:")
student2.introduce()
