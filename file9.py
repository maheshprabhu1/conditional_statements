# WAP to check whether a given value is present in between 45 to 125 and the number should be divisible by 4 and 5 and even value. If satisfied, to display the ascii character.
n=int(input())
if (n>=45 and n<=125) and (n%2==0 and n%5==0):
    print(chr(n))