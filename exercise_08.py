# removes docstring error
'''useful docstring'''

# https://www.delftstack.com/howto/python/python-log-formatter/
#formatter sets up how it looks, format tells what info goes in the formatter
formatter = " {} {} {} {}"
#print statement passes in four arguments
print(formatter.format(1, 2, 3, 4))
#print statement passes in four arguments
print(formatter.format("one", "two", "three", "four"))
#print statment  passes in four arguments
print(formatter.format(True, False, False, True))
#print statment passes in formatter, results in empty curly braces
print(formatter.format(formatter, formatter, formatter, formatter))
#print statment  passes in four arguments
print(formatter.format(
    "Try your",
    "Own Text here",
    "Maybe a poem",
    "Or a song about fear"
))

# STUDY DRILLS - same as Ex 7
# 1 Comment your code
# 2 read backwards or outloud
# 3 write down your mistakes from now on
# 4 try to not make the same mistakes
# 5 REM everyone makes mistakes