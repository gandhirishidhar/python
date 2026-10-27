'''
To write a program for star pattern in the python 

For n = 3
***
* *
***


Its a CLASSIC CASE OF IF, OR and ELSE STATEMENT

'''

n = int(input("Enter the Number:"))
for i in range(1, n+1):
    if i== 1 or i==n:
        print("*"* n)
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
        print("")
        
