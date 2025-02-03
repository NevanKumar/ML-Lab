print("NEVAN KUMAR")
print("22053791")
class Vehicle:
    # Constructor to initialize make, model, and year
    def _init_(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display vehicle information
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    # Overloading the + operator to combine make and model
    def _add_(self, other):
        if isinstance(other, Vehicle):
            return f"{self.make} {self.model} + {other.make} {other.model}"
        return NotImplemented

# Define a derived class Car that inherits from Vehicle
class Car(Vehicle):
    def _init_(self, make, model, year, num_doors, fuel_type):
        # Call the constructor of the base class (Vehicle)
        super()._init_(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    # Override the display_info method to include additional attributes
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, {self.num_doors}-door, Fuel type: {self.fuel_type}"

# Create instances of Vehicle
vehicle1 = Vehicle("Toyota", "Corolla", 2020)
vehicle2 = Vehicle("Honda", "Civic", 2019)

# Create instances of Car (which inherits from Vehicle)
car1 = Car("Ford", "Mustang", 2021, 2, "Gasoline")
car2 = Car("Tesla", "Model S", 2023, 4, "Electric")

# Display information of each vehicle
print(vehicle1.display_info())  
print(vehicle2.display_info())  
print(car1.display_info()) 
print(car2.display_info()) 

# Demonstrating operator overloading (+) to combine make and model
print(vehicle1 + vehicle2)  
print(car1 + car2) 