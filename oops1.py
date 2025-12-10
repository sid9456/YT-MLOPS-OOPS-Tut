 # initiate a class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("started exceuting attributes/data")
        self.id =123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been intiated")

    def travel(self,destination) :
        print("This travel function was caleed manually")
        print(f"Employee is now travelling to {destination}")


# create an object/instance of the class
sam = employee()
#print(sam.salary)
sam.travel("kerela")