from unreliable_car import UnreliableCar

car1 = UnreliableCar("Toyota", 50, 70)  # Reliability set to 70%
car2 = UnreliableCar("Ford", 60, 30)    # Reliability set to 30%

print(car1.drive(30))  # Output: Either 30 or 0 (if the drive fails)
print(car2.drive(40))  # Output: Either 0 (if the drive fails) or distance less than 40
