#WAP to check whether a given value is a negative or odd number and divisible by 4. If satisfied ,to display the cube of the values.
n=int(input())
if(n<0) or (n%2!=0) and (n%4==0):
    print(n**3)