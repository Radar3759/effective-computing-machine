'''useful docstring'''
from sys import argv

##First Section
##Complete
# print("How old are you?", end=' ')
# age = input()
# print("How tall are you?", end=' ')
# height = input()
# print("How much do you weigh?", end=' ')
# weight = input()

# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

##Second Section
##Complete
# script, filename = argv

# txt = open(filename)

# print(f"Here's your file {filename}:")
# print(txt.read())

# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())

##Third Section
print('Let\'s practice everything.')
print("""You\'d need to know \'bout escapes
      with \\ that do \n newlines and \t tabs.""")

POEM = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(POEM)
print("--------------")


# FIVE = 10 - 2 + 3 - 6
# print(f"This should be five: {FIVE}")

# def secret_formula(START_POINT):
#     jelly_beans = START_POINT * 500
#     jars = jelly_beans / 1000
#     crates = jars + 100
#     return jelly_beans, jars, crates


# START_POINT = 10000
# beans, jars, crates = secret_formula(START_POINT)

# # remember that this is another way to format a string
# print("With a starting point of: {}".format(START_POINT))
# # it's just like with an f"" string
# print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# START_POINT = START_POINT / 10

# print("We can also do that this way:")
# formula = secret_formula(START_POINT)
# # this is an easy way to apply a list to a format string
# print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

# PEOPLE = 20
# CATS = 30
# DOGS = 15

# if PEOPLE < CATS:
#     print( "Too many CATS! The world is doomed!")

# if PEOPLE < CATS:
#     print("Not many CATS! The world is saved!")

# if PEOPLE < DOGS:
#     print("The world is drooled on!")

# if PEOPLE > DOGS:
#     print("The world is dry!")

# DOGS += 5

# if PEOPLE >= DOGS:
#     print("People are greater than or equal to DOGS.")

# if PEOPLE <= DOGS:
#     print("People are less than or equal to DOGS.")


# if PEOPLE == DOGS:
#     print("People are DOGS.")
