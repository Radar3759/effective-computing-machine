# removes docstring error
'''useful docstring'''
# declare var types_of_people, assign value of 10
types_of_people = 10
# delcare var x, value of an f string between " "
#  pulling in value of var {types_of_people}
x = f"There are {types_of_people} types of people."
# declare var binary, value string
binary = "binary"
# declare var do_not, value string
do_not = "don't"
# declare var y, value f string
y = f"Those who know {binary} and those who {do_not}."

# prints the value of var x
print(x)
# prints the value of var y
print(y)

# prints f string, pulls in value of var x
print(f"I said: {x}")
# prints f string, pulls in value of var y
print(f"I also said: '{y}' ")

# sets var hilarious to false
hilarious = False
# declare var joke_evaluation, value string empty here to pull in the value of hilarious later
joke_evaluation = "Isn't that joke so funny?! {}"
# print joke_evaluation, put the value of hilarious between the {}
print(joke_evaluation.format(hilarious))
# declare var w, value string
w = "This is the left side of..."
# declare var e, value string
e = "a string with a right side."
# print the concatenated value strings of vars w and e
print(w + e)

# STUDY Drills
# 1. comment each line
# 2. Find strings within strings. At least 4
# 3. Maybe more than 4
# 4. Why does adding w and e make a longer string.
# ANSWER: the two shorter strings are concatenated making one longer string
