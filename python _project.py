from abc import ABC, abstractmethod
class Student(ABC):
    def __init__(self, name, roll_no):
        
        self.__name = name
        self.__roll_no = roll_no

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no
    
    @abstractmethod
    def display_info(self):
        pass

class SchoolStudent(Student):
    def __init__(self, name, roll_no, school_class):
        super().__init__(name, roll_no)
        self.school_class = school_class

    def display_info(self):
        print(f"[School Student] Name: {self.get_name()}, Roll No: {self.get_roll_no()}, Class: {self.school_class}")    

class CollegeStudent(Student):
    def __init__(self, name, roll_no, branch):
        # Call parent constructor
        super().__init__(name, roll_no)
        self.branch = branch

    def display_info(self):
        print(f"[College Student] Name: {self.get_name()}, Roll No: {self.get_roll_no()}, Branch: {self.branch}")





s_student1 = SchoolStudent("Rahul Sharma", 20, "10th Standard")
s_student2 = SchoolStudent("Shaurya Verma", 10, "11th Standard")
c_student1 = CollegeStudent("Aman Gupta", 30, "CSE")
c_student2 = CollegeStudent("Neha Singh", 40, "CSIT")


students_list = [s_student1, s_student2, c_student1, c_student2]
print("--- Student Details System ---")
for student in students_list:
    student.display_info()