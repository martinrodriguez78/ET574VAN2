Mileage = 23352 #miles on the odometer the first time
MileageTwo = 23695 #milds on the odometer the second time 
gallons = 11 

DT = MileageTwo - Mileage
MPG = DT / gallons


print("Distance Traveled:",DT,"miles")
print (" Gallons Used:", MPG, "Gallons")
print ("How many miles per gallon did the car average between two fillings?")
print (MPG,"Miles/Gallon")
