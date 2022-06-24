'''useful docstring'''
#def f(x) cheese_and_crackers
#cheese_count, boxes_of_crackers are arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #print statements with f string literals to pass through argument data
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
#print statement
print("\nWe can just give the function numbers directly: ")
#pass in different arguemetns to the f(x)
cheese_and_crackers (20, 30)

print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too: ")
cheese_and_crackers(10 + 20, 5 + 6)

print("We can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#aditional f(x)
def cookies_and_milk(cookies, glasses_of_milk):

#STUDY DRILLS
# 1. comment your code
# 2. read it backwards
# 3. write another f(x), run it ten times