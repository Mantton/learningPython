
def amplify(num):
    list1 = []
    for item in range(1,num):
        if item % 4 == 0 :
            item  = item * 10
            list1.append(item)
        else:
            list1.append(item)
    return list1
    # NOTE WIL RERUN NONE IF RETURN FUNCTION NOT STATED




print(amplify(100))
