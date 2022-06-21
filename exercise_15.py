'''helpful docstring'''
#importing argv from sys module
from sys import argv
#assign values to argv
script, filename = argv
#declare var txt set it to open(filename)
#open(filename) opens a file
txt = open(filename)
#print an f-string-literal prints the string in " ", prints the filename from argv
print(f"Here's your file {filename}:")
#prints the text inside ex15_sample.txt
print(txt.read())
txt.close()
# #prompts the user to input the filename where the text is stored
# print("Type the filename again: ")
# #assigns the filename from line 13 to a var file_again
# file_again = input("> ")

#comment out line 15-17, try using just input
file_again = input("Type the filename again: ")
#reopens the text file
txt_again = open(file_again)
#prints the text file
print(txt_again.read())
#close the file that was opened
txt_again.close()

#STUDY DRILLS
#1. comment your code
#2. ask for help. Try "search term THING" to see what a thing does
#3. commands are aka f(x), methods
#4. comment out lines 10-15, run again
#5. Try just input
#6 open and run files in the command line
#7. close the files that were opened