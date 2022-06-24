'''useful docstring'''

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_too(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}.")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("No args here.")

#calls the f(x) print_two, "dog" and "food" are the two arguments passed through
print_two("Dog", "Food")
#calls the f(x) print_two_too
print_two_too("Butter", "Toast")
print_one("One!")
print_none()
