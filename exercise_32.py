'''useful docstring'''

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#go through mixed lists
for i in change:
    print(f"I got {i}")

#build a list
elements = range(0,6)

#commented out 23-27 to switch elements to a direct range
#use range to do 0 to 5 counts
# for i in range (0,6):
#     print(f"Adding {i} to the list.")
#     #append is a function that lists understand
#     elements.append(i)

for i in elements:
    print(f"Element was: {i}")


