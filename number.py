'''

class Number:
    even=[]
    odd=[]
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        for i in range (self.num1,self.num2):
            if i%2==0:
                Number.even.append(i)
            else:
                Number.odd.append(i)
   
a=Number(1,10)
print(Number.even)
print(Number.odd)

'''
#best and way 2
class Number:
    
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def fun(s):
        even=[]
        odd=[]
        for i in range (s.num1,s.num2):
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        print(odd,even)
a=Number(int(input("num1=")),int(input("num2=")))
a.fun()

#less best than upper code and way two
'''
class Number:
    even=[]
    odd=[]
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        for i in range (self.num1,self.num2):
            if i%2==0:
                Number.even.append(i)
            else:
                Number.odd.append(i)
   
a=Number(1,10)
print(Number.even)
print(Number.odd)
'''