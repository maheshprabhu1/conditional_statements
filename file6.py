#WAP to check whether a given value is a negative or even number. If satisfied ,to display the last digit of the values.
n=int(input())
if(n<0) or (n%2==0):
    print(n%10)