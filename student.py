class Student:
    student_count = 0
    all_students = []

    def __init__(
            self,first_name,last_name,age,gender,student_id,course,instructor
    ):
        
        self.first_name = first_name
        self.last_name =last_name
        self.age=age
        self.gender=gender
        self.student_id=student_id
        self.course=course
        self.instructor=instructor

        Student.all_students.append(self)
        Student.student_count += 1
        

    def __repr__(self):
            return f"Student: {self.first_name} {self.last_name}"
        
s1 = Student("Alice", "Smith", 20, "Female", "A001", "Computer Science", "Dr. Jones")
s2 = Student("Bob", "Johnson", 22, "Male", "B002", "Mechanical Engineering", "Prof. Lee")
s3 = Student("Charlie", "Brown", 19, "Male", "C003", "History", "Ms. Davis")

print("All Students:")
print(Student.all_students) 

        
        


    