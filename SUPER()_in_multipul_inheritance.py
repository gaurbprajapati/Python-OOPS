
class JOB1:
    def __init__(self,sal1,**k):
        
        super().__init__(**k)
        self.sal1=sal1
        # print(self.sal1)
        # print(f"Salary of Job webdev.{self.sal1}")
    def jobone_detail(s):
        print("1. First Job name:-WEB DEVELOPER")
        # print("\n")
        print(f"1. Salary of Job webdev:--{s.sal1}")

class JOB2:
    def __init__(self,sal2,**k):
        
        super().__init__(**k)
        self.sal2=sal2
        # print(self.sal2)
        # print("Second Job name:-Data Scientist")
        # print(f"Salary of Job Data scientist{self.sal2}")
    def jobTwoDetail(s):
        print("2. Second Job name:--Data Scientist")
        # print("\n")
        print(f"2. Salary of Job Data Scientist:--{s.sal2}")

class combine(JOB1,JOB2):

    def __init__(self,a,b,name):
        self.name=name
        print(f"Name of worker who do two job simultaniously:-{self.name}")
        # print("job:-",name)
        super().__init__(sal1=a,sal2=b)
        # print(self.sal1+self.sal2)
        
    def total_salary(s):
        print(f"The total salary of {s.name} is {s.sal1+s.sal1}")

print("-------------------------------------------------------")  
c=combine(40000,50000,"Gaurv")
print("-------------------------------------------------------")
c.jobone_detail()
print("\n")
c.jobTwoDetail()
print("\n")
c.total_salary()
print("________________________________________________________")