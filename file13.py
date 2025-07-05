#WAP to check whether a given value is less than 125 and greater than 60 or not. If the condition is satisfied, take the name and extract the middle character and display it.
n=int(input())
if (n>=60 and n<=125):
    name=input("enter the name")
    val=int(len(name)/2)
    print(name[val])