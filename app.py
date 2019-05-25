# cows and bulls usinh if
import random

print("Welcome to the Cows and Bulls game")

val = random.randint(1000, 9999)
#print(val)  DEV CHECK
while True :

    user = input("Enter a 4 digit number :")

    if user.lower() == 'quit':  # EXIT CODE
        print("EXITING")
        break
    if user.lower() == "unhide":  # CHEAT CODE
        print(val)
        break

    try:
        val_list = [int(x) for x in str(val)] # Convert int to list using for loop
        user_list = [int(x) for x in str(user)]

        cow = 0
        bull = 0

       # print(val_list)
       # print(user_list)
        # IN DEV CHECK ABOVE

        for item in range(0,4):
            if val_list[item] == user_list[item]:
                cow += 1
            elif val_list[item] in user_list:
                bull += 1


        print(f'{cow} cow(s) , {bull} bull(s)')  # OUTPUT RESULTS
        if cow == 4:
            print("YOU FINALLY GOT IT ")
            break

    except ValueError:  # ERROR CODE
        print("Invalid Input")

    except IndexError :  # ERROR CODE
        print("INVALID INPUT")
