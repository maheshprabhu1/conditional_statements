#WAP to check whether a character is in the uppercase or not. If the uppercase, storethe value inside the dict(key as a character and value as an ascii value).
ch = input("Enter a character: ")
if len(ch) == 1:
    if ch>='A' and ch<='B':
        my_dict = {ch: ord(ch)}
print(my_dict)