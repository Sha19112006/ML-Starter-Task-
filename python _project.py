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