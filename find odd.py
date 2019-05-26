

# find odd

a = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]





def find_odd(a):
    for item in a:
        b = a.count(item)

        if b % 2 != 0:
            print(item)



find_odd(a)
