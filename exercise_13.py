'''helpful docstring'''
from sys import argv
# argv = script, first, second, third
#use argv to call in the command line
#python filename.py var1 var2 var3
# script, first, second, third = argv
# print("The first script is called: " , script)
# print("Your first variable is: ", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

#STUDY DRILLS
#1 more/less arguements results in ValueError: too many/few values to unpack
#2 write a script with more/less values

##Shorter script
# script, orange, apple = argv
# print("The script is called: ", script)
# print("The first var is: ", orange)
# print("The second var is: ", apple)

##longer script
# script, red, orange, yellow, green, blue, indigo, violet = argv
# print("The script is called: ", script)
# print("First color: ", red)
# print("Second color: ", orange)
# print("Third color: ", yellow)
# print("Fourth color", green)
# print("Fifth color ", blue)
# print("Sixth color: ", indigo)
# print("Seventh color ", violet)

##combine input with argv
#this is all about line placement and how you call it in the command
#https://stackoverflow.com/questions/25675223/how-to-use-raw-input-with-argv

script, sandwich = argv

my_num = input("Enter a number between 1 and 10: ")
print(f"Your number is: {my_num}")

print("Script name: ", script)
print("Spam Musubi is my favorite:", sandwich)
