'''useful docstring'''
#declare variables and assign them a numeric value (int)
people = 30
cars = 40
trucks = 15

#if/elif statement
#if the number assigned to var cars is greater than that assigned to var people, print the string in " "
#CARS
if cars > people:
    print("We should take the cars.")
#if cars > people is False, see if cars < people
# #if cars < people is True, then print the string in " "    
elif cars < people:
    print("We should not take the cars.")
#if no other statement is True, print the string in " "    
else:
    print("We can't decide")  

#try other nums    
trucks = 45

#TRUCKS
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

#PEOPLE
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

#try other nums and other boolean expressions
trucks = 10
cars = 10
if trucks == cars or people == cars:
    print("Something is equal to cars")

#STUDY QUESTIONS     
#1. guess what elif and else are doing
#elif and else are secondary statements
#if the first statment is false, then the elif statment is tried
#if everything is false, then the else code is read

#2 Change the number of cars, people, trucks. See what prints
#3. Try other Boolean expressons
#4. comment your code