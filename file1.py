# WAP to check whether a given value is divisible by 5 and 7. If the value is divisible,to display the square of the values.
n=int(input())
if n%5==0 and n%7==0:
    print(n**2)
else:
    print("not divisible")