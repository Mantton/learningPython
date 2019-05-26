

def median(array):

    array = sorted(array)
    n = len(array)
    print(array)

    if n % 2 != 0:
        a = int((n - 1) / 2)
        print(array[a])
# Works
    else:
        a = int(n/2)
        print((array[a-1] + array[a])/2)
# Works


test = [ 18,24,  20,  35,  19,  23,  26,  23,  19,  20]
test2 = [21.4323, 432.54, 432.3, 542.4567]
test3 = [-23, -43, -29, -53, -67]

median(test2)
