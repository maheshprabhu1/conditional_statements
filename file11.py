#WAP to check whether a given number is an integer and odd number. If the condition is satisfied, the integer is divisible by 5 and displays the result.
n=int(input())
if(n%2!=0):
    print(n%5==0)