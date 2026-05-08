# Starter Code for Python Classes Assignment

# Task 1: Define a Simple Class
# Fill in the class definition below

class Car:
    def __init__(self, make, model, year, mileage=0):
        # Initialize attributes
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def display_info(self):
        # Print car details
        print(f"Car Details: {self.year} {self.make} {self.model}")
        
    def update_mileage(self, new_mileage):
        # Prevent accidental rollback of odometer readings
        if new_mileage < self.mileage:
            print("Error: New mileage cannot be less than current mileage.")
        self.mileage = new_mileage
        print(f"Mileage updated to {self.mileage} miles.")

    def display_mileage(self):
        print(f"Current mileage: {self.mileage} miles.")


# Task 2: Add Methods and Interactions
# Add mileage attribute and methods as described in the assignment

# Example usage (uncomment and complete):
# my_car = Car('Toyota', 'Corolla', 2020)
# my_car.display_info()
# my_car.update_mileage(15000)
# my_car.display_mileage()

my_car = Car("Toyota", "Camry", 2022)
my_car.display_info()
my_car.display_mileage()
my_car.update_mileage(15000)
my_car.display_mileage()
