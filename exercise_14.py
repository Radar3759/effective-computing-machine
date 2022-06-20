'''helpful docstring'''
from sys import argv
# script, user_name = argv
# prompt = '>'

# print(f"Hi {user_name}, I'm the {script} script.")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes = input(prompt)

# print(f"Where do you live {user_name}?")
# lives = input(prompt)

# print("What kind of computer do you have?")
# computer = input(prompt)

# print(F"""
# Alright, so you said {likes} about liking me.
# You live in {lives}. Not sure where that is.
# And you have a {computer} computer. Nice.
# """)

# STUDY DRILLS
# 1 Zork is an interactive computer game
# https://zork.fandom.com/wiki/Zork_series
# Adventure is an Atari game
# https://en.wikipedia.org/wiki/Adventure_(1980_video_game)
# 2. change prompt to something else
# 3. add another argument (see below)
# 4. Make sure you understand how  """ and {} f literals work.

script, user_name, color = argv
answer = '-'

print(f"Hi {user_name}, I'm the {script} script.")
print(f"My fav color is {color} too!")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(answer)

print(f"Where do you live {user_name}?")
lives = input(answer)

print("What kind of computer do you have?")
computer = input(answer)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
