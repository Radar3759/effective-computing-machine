'''useful docstring'''
# #start counting at zero
# i = 0
# #empty array called numbers
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1

#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
#     print(num)

# STUDY DRILLS
# 1 convert it to a f(x)
# replace 6 c a var

#n is the input when the f(x) is called
def num_6(n, b):
    i = 0
    numbers_2 = []

    while i < n:
        print(f"At the top i is {i}")
        numbers_2.append(i)
        i = i + b

        print("Numbers now: ", numbers_2)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers_2:
        print(num)


num_6(13, 3)

