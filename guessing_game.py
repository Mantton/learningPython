import random

num = random.randint(1, 9)


while True:
    user = input("ENTER A NUM BETWEEN 1 & 9 ")
    if user.lower() == "quit":
        break
    #catch invalid input error
    try:
        if int(user) > num:
            print("TOO HIGH")
        elif int(user) < num:
            print('TOO LOW')
        elif int(user) == num:
            print("YOU ARE CORRECT!")
            break

    except ValueError:
        print("INVALID INPUT")
