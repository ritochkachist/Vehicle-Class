# Margarita Chistiakova
# 2/20/2023
# Vehicle class (class creation and use of function)

from Vehicle import Vehicle

print("Welcome to the program!")

inventory = []
myVehicle = None
choice = 0
while choice !=7:
 
  print("""\nPlease enter the option from the menu below:\n
  1. Add a vehicle
  2. Drive the vehicle
  3. Fill up the fuel tank in the vehicle
  4. Add fuel to the tank
  5. Print the details of the vehicle
  6. Print the details of a vehicle in the inventory
  7. Quit the program\n""")
  
  choice = int(input("Please enter a number you chose: \n"))
  
  if choice == 1:
    print("Please enter the make of the vehicle: ")
    make = input()
    print("Please enter the model of the vehicle: ")
    model = input()
    print("Please enter the type of the vehicle: ")
    type = input()
    print("Please enter the gas tank size of the vehicle: ")
    gastanksize = input()
  
    myVehicle = Vehicle(make, model, type, gastanksize)
    inventory.append(myVehicle)
    
  elif choice == 2:
    if inventory == []:
      print("You cannot drive a vehicle that has not been yet created.")
    else:
      if len(inventory) == 1:
        #print("There is currently 1 vehicle in the inventory")
        print(myVehicle.drive())
      else:
        print(f"There are currently {len(inventory)} vehicles in the inventory")
        print("Please choose which you would like to drive: ")
        choice = int(input())
        print(inventory[choice-1].drive())
    
  elif choice == 3:
    if len(inventory) == 1:
      #print("There is currently 1 vehicle in the inventory\n")
      print(myVehicle.fill_up())
    else:
      print(f"There are currently {len(inventory)} vehicles in the inventory")
      print("Please choose which you would like to fill up: ")
      choice = int(input())
      print(inventory[choice - 1].fill_up())
      print("The tank in now full!\n")
   
  
  elif choice == 4:
    if len(inventory) == 1:
      #print("There is currently 1 vehicle in the inventory")
      print(myVehicle.getgas())
    else:
      print(f"There are currently {len(inventory)} vehicles in the inventory")
      print("Please choose which you would like to add gas in: \n")
      choice = int(input())
      fuel_amount = int(input("Please enter the amount of fuel you want to put in the Vehicle: "))
      print(inventory[choice -1].getgas())
  
  elif choice == 5:
    if len(inventory) == 1:
      #print("There is currently 1 vehicle in the inventory")
      print(myVehicle)
    else:
      print(f"There are currently {len(inventory)} vehicles in the inventory")
      print("Please choose the one you want to know the details of: ")
      choice = int(input())
      print(inventory[choice - 1].__repr__())
  elif choice == 6:
    print(inventory)

  else:
    print("Thank you for taking part in my Vehicle Class program! Have a good day!")
    
     
      
      