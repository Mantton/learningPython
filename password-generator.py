# Password generator
import random
import string
'''
 two types of passwords : strong and weak
 strong wll be generated randomly
 weak will be a combinbation of words from a list
'''


def gen_weak():
    names = ['jaconks', 'Mary', 'Jogn', 'Dioub', 'Lilith', "Jackson"]
    numbers = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
         67, 71, 73, 79, 83, 89, 97,
         101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
         151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    password = names[random.randint(0, len(names)-1)] + str(numbers[random.randint(0 ,len(numbers)-1)])
    # tested and works
    return password



def gen_strong():
    symbols = '!@#$%&*'
    letters = string.ascii_letters
    s = ''.join(random.choice(letters) for i in range(random.randint(1,10)))
    # the line above means join the random letters formed to one string
    password = s + symbols[random.randint(0,len(symbols)-1)] + str(random.randint(0,5000))
    return password

# both functions work


# UI

while True :
    user = input("Would you like a Strong [S] or Weak [W] password : [S/W]")
    if user.lower() == 'quit':
        print("EXITING")
        break
    if user.lower()=='s' or user.lower()=='w':
        if user.lower() == 's':
            print(gen_strong())
        elif user.lower() == 'w':
            print(gen_weak())
    else:
        print("INVALID INPUT")
