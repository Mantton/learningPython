



wrd=input("Please enter a word")

wrd=str(wrd)
rvs=wrd[::-1] # from first in dex to last index read backwards
print(rvs)

if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
