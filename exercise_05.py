#removes docstring error
'''useful docstring'''
my_name = "Zed A. Shaw"
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"\nLet's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

#Study Drills
#1 remove 'my' from all the vars
name = "Zed A. Shaw"
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"\nLet's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#2 create vars that convert from lbs and inches to cms and kgs
convert_to_cms = height * 2.54
print(f"\n{height}in converted to centimeters is {convert_to_cms}cm.")

convert_to_kgs = weight * 0.45359237
#round to 3 sig figs
kgs_sig_figs = round(convert_to_kgs, 3)
print(f"\n{weight}lbs converted to kilograms is {kgs_sig_figs}kg.")
