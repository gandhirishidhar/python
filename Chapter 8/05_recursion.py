# one opf the  most direct way to solve the problem ot write the code in a shorter way if you know the mathematoical formula


def factorial(n):
    if(n==1 or n ==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number:"))
print(f"The Factorial of the given number is: {factorial(n)}")28