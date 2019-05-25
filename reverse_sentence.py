# REVERSE ORDER STRING


'''
So gonna break down string into elements f a list then priint that list in
reverse order
'''


# can split string using .split method
# this would be very useful reading .csv files


def reverse_string(string):
    list1 = string.split(" ")
    list2 = list1[::-1]
# gonna use .join instead of for loop
    result = " ".join(list2)  # joins list using " " space
    print(result)

name = input("What is your name?")

sentence = f'My name is {name}'  # formatted variable lol

reverse_string(sentence)

