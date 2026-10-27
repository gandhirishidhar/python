# write a programmfor findinf=g the grates of 4 numbes enterred by the user.

# Here's a simple Python program that finds the greatest of four numbers entered by the user:```python
# Function to find the greatest of four numbers

a1 = int(input("enter number 1: "))
a2 = int(input("enter number 2: "))
a3 = int(input("enter number 3: "))
a4 = int(input("enter number 4: "))

if (a1>a2 and a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)
elif (a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:", a2)
elif (a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:", a3)
else:
    print("Greatest number is a4:", a4)

    