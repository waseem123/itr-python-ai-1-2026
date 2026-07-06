class Person:
    def setPerson(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def getPerson(self):
        print(f'NAME   - {self.name}')
        print(f'AGE    - {self.age}')
        print(f'GENDER - {self.gender}')
        
class Student(Person):
    def setStudent(self,rollno,marks,dept):
        self.rollno = rollno
        self.marks = marks
        self.dept = dept
        
    def getStudent(self):
        print(f'ROLLNO   - {self.rollno}')
        print(f'MARKS    - {self.marks}')
        print(f'DEPT - {self.dept}')
        
        


s = Student()
s.setPerson('Anya',5,'F')
s.setStudent(101,25,'LKG')
s.getPerson()
s.getStudent()