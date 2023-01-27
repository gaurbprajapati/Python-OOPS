class Car:

    def __init__(self,company,model,color,Fuel_Type,Engine_Displacement,Seating_Capacity,TransmissionType,Body_Type,brakes,doors,cost):
        self.company=company
        self.model=model
        self.color=color
        self.Fuel_Type=Fuel_Type
        self.Engine_Displacement=Engine_Displacement
        self.Seating_Capacity=Seating_Capacity
        self.TransmissionType=TransmissionType
        self.Body_Type=Body_Type
        self.brakes=brakes
        self.doors=doors
        self.cost=cost
        print(f"Name of company :-{self.company} ")
    def design(e):
        print(f"Name of Modal:- {e.model}")
        print(f"Color of car:- {e.color} ")
        print(f"Cost of car:- {e.cost} ")
        print("-------------------------------------")

    def genralFeature(d):
        print("General Feature of car:-")
        print("'Power Steering','Power Windows Front','Anti Lock Braking System','Air Conditioner','Driver Airbag','Passenger Airbag'")
        print("--------------------------------------")

    def engineTransmission(a):
        print("Engine Detail of Car:-")
        print(f"Displacement(cc):- {a.Engine_Displacement}, Brakes and steering:- { a.brakes}, Body Type {a.Body_Type}  ")
        print("--------------------------------------")

    def fuelPerformance(b):
        print("Fuel detail of car:-")
        print(f" Fuel type:-{b.Fuel_Type}")
        print("---------------------------------------")

    def dimensionsCapacity(c):
        print("Capacity of Car")
        print(f"Seating Capacity:- {c.Seating_Capacity} , Number of DOors { c.doors} ")
        print("--------------------------------------------------------------------------------")
    def suggestion(f):
        print("This is the best model for you and I hope you take good dession")

#child class one
class Mahinda(Car):
    def fun(self):
        print("The detail of Car:---")
        print("--------------------------------------")
print("OPTION ONE:-")
print(" ")
o = Mahinda("Mahindra","Mahindra XUV700","blue","petro","1993","7","manual","SUV","Ventilated Disc",4,"500000 Rs.")
o.fun()
o.design()
o.genralFeature()
o.engineTransmission()
o.fuelPerformance()
o.dimensionsCapacity()
o.suggestion()
print(" ")
print("===============================================================================================================")
#child class two
print("OPTION TWO")
print("")

class Hondamoters(Car):
    def fan(self):
        print("The details of car:-")
ob = Hondamoters("Honda","Honda Jazz","Gray","CNG",1999,5,"Manual","Jazz","Ventilated Disc",4,"700000 Rs.")
ob.fan()
ob.design()
ob.genralFeature()
ob.engineTransmission()
ob.fuelPerformance()
ob.dimensionsCapacity()
ob.suggestion()
