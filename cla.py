class c:
    
#THIS IS THE PARENT CLASS
    def __init__(self,a):
        print("parent class")
        
        self.a=a

    def func(s):
        pass
#CLASS CHILE IS DEFINED BELOW 
class c2(c):
    def __init__(self):
        print("child class")
        c().__init__()
    def func2(s):
        pass

o=c2()
