# #multipul inh

# class Student:
#   def __init__(self, name):
#     print(name, 'IS from calss 10.')

# class Tenclass(Student):
#   def __init__(self, Rollno):
#     print(Rollno,":the roll no")
#     super().__init__(Rollno)
    
# class Masks_A(Tenclass):
#   def __init__(self, percentage):
#     print(percentage, "he is in A+ gread")
#     super().__init__(percentage)

# class Masks_B(Tenclass):
#   def __init__(self, percentage_1):
#     print(percentage_1, "can't swim.")
#     super().__init__(percentage_1)

# class Raj(Masks_A,Mask_B):
#   def __init__(self):
#     print("he is Good student")
#     super().__init__('Gaurav')
    
# d = Raj()
# print('')
# # bat =Raj('Gaurav Prajapati')

# class father:
#     def __init__(self,m):
#         self.money=m
#         super().__init__()
#         print("Father class Constructor")
#     def show(self):
#         print("Father class Instance method")

# class father2:
#     def __init__(self,m2):
#         self.money2=m2
#         super().__init__()
#         print("Father2 class Constructor")
#     def show2(self):
#         print("Father2 class Instance method")


# class son(father,father2):
#     def __init__(self,m,m2):
#         super().__init__(m,m2)
#         # self.job=j
#         print("Son class Constructer")

#     def dis(self):
#         print("Son class Instance Method",self.money,"JOB",self.money2)

# s = son(1000,50)
# s.dis()

class Parent:
    def ___init__(self,name):
        print("Perent __init__", name)

# class Parent2:
#     def __init__(self,name):
#         print("Parent2 __init__", name)

class Child(Parent):
    def __init__(self):
        print("Child __init__")
        super.__init__('Gaurav')
c = Child()
print(Child.__mro__)