'''useful docstring'''

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs: 
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")


#try other booleans
if people == dogs and cats == 30:
    print("Yay! People are dogs and cats are 30.")

#STUDY DRILLS
#1. What do you think the if does to the code under it?
#the if statement evaluates the code under it
#if the statement code is true, then it goes to the next line

#2 why does the code under the if statement need to be indented four spaces
#to show that this code occurs as part of the previous line. 

#3 what happens if no indent?
#error: 'expected an indented block

#4 Can you put other boolean expressions from Ex 27 here? try it.
# yes. 

#5 What happens if you change the initial values for people, cats, dogs
#different things print or don't print
