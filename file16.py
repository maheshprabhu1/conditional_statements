# WAP to check whether a character is in the alphabet or not. If the alphabet, store the value inside the dict(key as a character and value as an ascii value).
ch = input("Enter a character: ")

# Check if the input is a single character
if len(ch) == 1:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        my_dict = {ch: ord(ch)}
        print(my_dict)