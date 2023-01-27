class employee:
    def __init__(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.id=id
        print(self.name,self.age,self.id,self.salary)

employee1 = employee("gaurav",22,1000,60000)
print(employee1.__dict__)

employee2 = employee("ram",22,3,333030300)
print(employee2.__dict__)