'''
To write a program for star pattern in the python 

For n = 3
  *
 ***
******


'''

n =int(input("Enter the number: "))
for b in range (1, 1+n):
    print(" "* (n-b), end="")
    print("*"* (3*b-1), end="")
    print("")


