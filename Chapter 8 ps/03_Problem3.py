"""How do you prevent Python's print() function from printing a newline at the end?"""

print ("a")
print("b")
print("c", end= "")
print("d", end= "")   #to avoid new line after the result, add comma then end = "  i.e blank)"