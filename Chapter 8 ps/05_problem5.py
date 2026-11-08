'''
# write now I am writting codes for use case of recurrsion for call of function for again and again. 
# so what gonna happen now is i am going to def a function to print star.
after def the function as print ("*" * n) then call the function n-1 times and if  the value of n is n is equals to the zero then the function shoukld return the value  nothing

we gonn ado this by putting rturn (" ")
'''


def print_star(n):
    if n == 0:
        return ""
    else:
      return "*" * n + "\n" + print_star(n - 1)


print(print_star(9))
    