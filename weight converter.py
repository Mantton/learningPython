

var = float(input('Weight:'))



unit = input("(L)bs or (K)g: ")

constant = 0.45
to_kg = var * constant
to_lbs = var / constant
if unit.lower() == "l":
    print(f'You are {to_kg} Kg')
elif  unit.lower() == "k":
    print(f'You are {to_lbs} pounds')
else:
    print("Invalid Input")



