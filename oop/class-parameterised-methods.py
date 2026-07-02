class Student:
    
    def inputdata(self,rollno=100,name='Anushka',marks=81):
        self.rollno = rollno
        self.name = name
        self.marks = marks
        
    def getStudent(self):
        print(f'ROLL NO - {self.rollno}')
        print(f'NAME - {self.name}')
        print(f'MARKS - {self.marks}')
        print('______________________')
        
        
        
s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()

s1.inputdata(101,'Alisha',70)
s2.inputdata(102,'Bhakti',72)
s3.inputdata(103,'Aarya',87)
s4.inputdata()

s1.getStudent()
s2.getStudent()
s3.getStudent()
s4.getStudent()