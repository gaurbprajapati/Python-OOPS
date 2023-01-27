#  method overriding

class Emp:
    def message(self):
        
        print("I am from NIET")

class Dept(Emp):
    
    '''
    there is 3 code and diff. output meaning
    
    '''
    # def message(self):
    #     print("GAURav")
    #     return super().message()
    
    
    # def message(self):
    #     super().message()
    #     print("NIET is in Greater noida")
        
    def message(self):
       
        print("NIET is in Greater noida")
        super().message()

d = Dept()
d.message()

# e = Emp()
# e.message()

