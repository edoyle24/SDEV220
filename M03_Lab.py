class Vechile:
    def __init__(self, vechile_type):
        self.vechile_type = vechile_type 

class Car(Vechile):
    def __init__ (self, year, make, model, number_of_doors, type_of_roof):
        super().__init__("Car")
        self.year = year
        self.make = make
        self.model = model
        self.number_of_doors = number_of_doors
        self.type_of_roof = type_of_roof

# Prompt user for car details
print("Enter the details of the car:")

year = input("Please enter the Year: ")
make = input("PLease enter the Make: ")
model = input("Please enter the Model: ")

number_of_doors = input("Does the car have 2 or 4 doors (Please enter 2 or 4): ")
while number_of_doors not in ['2', '4']:
    print("Invalid input. Please enter 2 or 4.")
    number_of_doors = input("Does the car have 2 or 4 doors (Please enter 2 or 4): ")

type_of_roof = input("What type of roof does the car have (Please enter solid or sun roof): ")
while type_of_roof not in ['solid', 'sun roof']:
    print("Invalid input. Please enter 'solid' or 'sun roof'.")
    type_of_roof = input("What type of roof does the car have (Please enter solid or sun roof): ")

# Create an vechile object 
car1 = Car(year, make, model, number_of_doors, type_of_roof)

print("The Vechile details are: ")
print("Vechile Type: Car")
print("Year: " + year)
print("Make: " + make)
print("Model: " + model)
print("Number of doors: " + number_of_doors)
print("Type of roof: " + type_of_roof)