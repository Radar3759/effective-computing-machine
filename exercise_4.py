#removes docstring error
'''useful docstring'''

#declare var cars, set the value to 100
cars = 100
#declare var space_in_a_card, set the value to 4.0
space_in_a_car = 4.0
#declare var drivers, set the value to 30
drivers = 30
#declare var passengers, set value to 90
passengers = 90
#declare var cars_not_driven, set value to cars - drivers
cars_not_driven = cars - drivers
#declare var cars_driven, set the value to the value of drivers
cars_driven = drivers
#declare var carpool_capacity, set the value of cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#declare var average_passengers_per_car, set the value to passengers / cars_driven
average_passengers_per_car = passengers / cars_driven

#print statements with f-string literal
#using f before the "" and {var} pulls in the var value to the print statment
#each line below prints the words between the ""
#\n for new line
print(f"\nThere are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passengers_per_car} in each car.")

#Study drills

#What's up with NameError: name "car_pool_capacity"?
# # It doesn't match the declared var "carpool_capacity"

#1. is 4.0 necessary? Can use just 4?
#  4.0 makes it useable as a floating point number if that is assigned
#2. REM 4.0 is floating point num
#3 Comment your code
#4 -6 no notes