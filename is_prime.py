
# chack if a number is sonly divisble by itself and one then output the bolean value
def is_prime(num):
    list = []  # this lst stores he factors of the num
    for item in range(1, 5000):  # Only checks the first 5000
        if num % item == 0:
            list.append(item)

    if list == [1, num]:
        return True
    else:
        return False

# Main program


while True:
    user = input("ENTER A NUM :")
# create quit command
    if user.lower() == 'quit':
        break
# catch input error
    try:
        a = is_prime(int(user))

        if a is True:
            print(f'{int(user)} is a Prime Number ')
        else:
            print(f'{int(user)} is NOT Prime Number ')
    except ValueError:

        print("INVALID INPUT")


