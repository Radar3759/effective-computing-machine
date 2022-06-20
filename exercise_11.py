#this is also exercise 12

age = input("\nHow old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

#alt way to get input
#print("How old are you", end=' ')
#age = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#STUDY DRILLS
#1. find out what Python input does
#input prompts the user to enter a string that inputs is assigned to a var
#2 Other ways to use input?
#int(input()), float(input()) 

#3 write another form like this
#ANOTHER FORM LIKE THIS
flavor = input("\nChoose an ice cream flavor: Chocolate, Vanilla, Strawberry ")
toppings = input("Pick a topping: Caramel, Hot Fudge, Pineapple ")
dish = input("Would you like a plate or a bowl? ")
print(f"You want {flavor} ice cream served in a {dish} with {toppings} on top.")