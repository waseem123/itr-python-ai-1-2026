class Student:
    def setStudent(self,rollno,name):
        self.rollno = rollno
        self.name = name
        
    def getStudent(self):
        print(f'ROLL NO - {self.rollno}')
        print(f'NAME    - {self.name}')
        
class EngineeringStudent(Student):
    def setEngStudent(self,branchName,degree):
        self.branchName = branchName
        self.degree = degree
    
    def getEngStudent(self):
        print(f'BRANCH NAME - {self.branchName}')
        print(f'DEGREE      - {self.degree}')
        
class MedicalStudent(Student):
    def setMedStudent(self,specialization):
        self.specialization = specialization
    
    def getMedStudent(self):
        print(f'SPECIALIZATION - {self.specialization}')
        
        
        
stud1 = EngineeringStudent()
stud2 = EngineeringStudent()
stud3 = MedicalStudent()

stud1.setStudent(101,'Waseem')
stud1.setEngStudent('Computer Science and Engineering','BTech')

stud2.setStudent(102,'Spider man')
stud2.setEngStudent('Electronics and Telecommunication','MTech')

stud3.setStudent(101,'Iron Man')
stud3.setMedStudent('Cardiology')

stud1.getStudent()
stud1.getEngStudent()

stud2.getStudent()
stud2.getEngStudent()

stud3.getStudent()
stud3.getMedStudent()