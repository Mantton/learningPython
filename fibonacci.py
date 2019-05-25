
# YIKES fibonacci
try:
    a = int(input("How Many Fibonacci Numbers do you want generated: "))

    # write out the starting terms as it is easier to continue from there
    list = [0,1]
    # define the first two fibonacci terms
    first = list[0]
    second = list[1]


    for item in range(a-2):
        # a -2 because the first two fibonacci terms ahe already been defined
        total = first + second
        list.append(total)
        first = second
        second = total

    print(list)
except ValueError:
    print("INVALID INPUT")




# IT ACTUALLY WORKS LMAO
