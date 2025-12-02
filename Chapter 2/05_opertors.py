

("""Truth tables for boolean operators

A      B      A or B  A and B  not A  not B
False  False  False   False    True   True
False  True   True    False    True   False
True   False  True    False    False  True
True   True   True    True     False  False
""")

print ("True and False is", True and False)
print ("True or False is", True or False)
print ("not True is", not True)
print ("not False is", not False)
print ("True and True is", True and True)
print ("False or False is", False or False)
print ("True or True is", True or True)
print ("False and False is", False and False)
print ("not (True and False) is", not (True and False))
print ("not (True or False) is", not (True or False))
print ("(True and False) or True is", (True and False) or True)
print ("(True or False) and False is", (True or False) and False)
print ("(not True) or (not False) is", (not True) or (
not False))