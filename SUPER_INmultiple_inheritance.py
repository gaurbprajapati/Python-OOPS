# class P1_class:
#     def __init__(self,a,**k):
#         super().__init__(**k)
#         self.a=a
#         # self.b=b
#     def show1(s):
#         print(f"The value of 'a' and 'b' is {s.a} and {s.b} ")

# class P2_class:
#     def __init__(self,c,**k2):
#         super().__init__(**k2)
#         self.c=c
#         # self.d=d
#     def show2(s):
#         print(f"THe value of c and d is {s.c} and {s.d}")

# class P3_class(P1_class,P2_class):
#     def __init__(self,a2,c2,e):
#         self.e=e
#     print("heloo")
#     super().__init__(a2=a)
#     def show(self):
#         print(self.a2+self.b2+self.c2+self.d2+self.e)

# o = P3_class(1,2,3,4,5)
# o.show2()
# o.show()



# from os import O_NDELAY


class P_class:
    def __init__(self,sal1,sal2,**k):
        
        super().__init__(**k)
        self.sal1=sal1
        self.sal2=sal2
        print(k)
        
    def show(s):
        print(f"1. Value of A:--{s.sal1}")

class p2_class:
    def __init__(self,sal3,sal4):
        
        # super().__init__()
        self.sal3=sal3
        self.sal4=sal4
    def sahow2(s):
        print(f"2. Value of B:--{s.sal2}")

class combine(P_class,p2_class):

    def __init__(self,a,b,c,d,e):
        self.e=e
        super().__init__(sal1=a,sal2=b,sal3=c,sal4=d)
  
        
    def total(s):
        print(f"Total value :-- {s.sal1+s.sal1+s.sal3+s.sal4+s.e}")
        
o=combine(1,2,3,4,5)

o.show()
o.sahow2()
o.total()


print("____________________________________________________________________________________________-")

# class a(object):
#     def __init__(self,value):
#         # super().__init__()
#         print(value)
        
# class b(object):
#     def __init__(self,v):
#         print(v)
#         # super().__init__()

# class log(a,b):
#     def __init__(self,a,b):
#         a.__init__(self,a)
#         b.__init__(self,b)
    
# x = log(1,2)

