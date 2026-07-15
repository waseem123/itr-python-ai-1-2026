class Student:
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
        
    def getStudent(self):
        print(f'ROLL NO - {self.rollno}')
        print(f'NAME    - {self.name}')
        
class EngineeringStudent(Student):
    def __init__(self,rollno,name,branchName,degree):
        super().__init__(rollno,name)
        self.branchName = branchName
        self.degree = degree
    
    def getStudent(self):
        super().getStudent()
        print(f'BRANCH NAME - {self.branchName}')
        print(f'DEGREE      - {self.degree}')
        
        
e1 = EngineeringStudent(105,'Alisha','Computer Science','B Tech')
e1.getStudent()
e1.getStudent()