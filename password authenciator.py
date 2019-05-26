
import random


code = random.randint(1000, 9999)


def is_valid_pin(pin):
    try:
        if int(pin) == code:
            return True

    except ValueError:
        print("INTERNAL ERROR : INVALID INPUT")


while True:
    user = input("ENTER PIN")

    if user.lower() == 'exit' :
        print("EXITING")
        break
    elif user.lower() == 'showpin':
        print(code)
        break

    try:
        if is_valid_pin(int(user)) is True:
            print("WELCOME")
        else:
            print("INVALID CODE")
    except ValueError:
        print("INVALID INPUT")
