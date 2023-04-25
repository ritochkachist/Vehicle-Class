
class Vehicle():
  def __init__(self, make, model, type, gastanksize):
    self.make = make
    self.model = model
    self.type = type
    self.gastanksize = gastanksize
    self.fuel_level = 0
    
    
  def __repr__(self):
    return "The car's make is " + self.make +"\nThe car's model is " + self.model + "\nThe car's type is " + self.type + "\nThe tank size of the car is " + self.gastanksize + " gallons" + "\nThe current fuel level is " + str(self.fuel_level)

  def fill_up(self):
   self.fuel_level = self.gastanksize
   return "Your fuel tank now contains " + str(self.fuel_level) + " gallons of gas."  
    
  def getgas(self, fuel_amount):
    free_space = int(self.gastanksize) - int(self.fuel_level)
    if int(fuel_amount) > free_space:
       self.fuel_level = self.gastanksize
       
       leftover = int(fuel_amount) - free_space
      
       return "There was too much fuel for the tank to hold. You tried to add " + str(fuel_amount) + "gallons. However, there was only enough space for " + str(free_space) + "." + " That means you have " + str(leftover) + " gallons of gas leftover ."
     
    else:
      self.fuel_level == self.fuel_level + int(fuel_amount)
      added_fuel = int(self.fuel_level) + int(fuel_amount)
      return "The fuel was added to the tank. You now have " + str(added_fuel) + " gallons in the tank."

  def drive(self):
    if self.fuel_level == 0:
      return "No fuel left, cannot drive this Vehicle"
    self.fuel_level = int(self.fuel_level) - 1
    return "The " + self.make + " is now driving!\nYour current fuel level is " + str(self.fuel_level) + " gallons."

  