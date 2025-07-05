#WAP to check whether a given value is present in between 25 to 100 and the numbershould be divisible by 4 and 5. If satisfied, to display multiplication of given value with 5.
n=int(input())
if (n>=25 and n<=100) and (n%2==0 and n%5==0):
    print(n*5)