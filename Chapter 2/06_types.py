# Function to check the type/class of a variable
def check_variable_type(variable):
    return type(variable)

# Example usage
if __name__ == "__main__":
    # Different types of variables
    int_var = 10
    float_var = 10.5
    str_var = "Hello, World!"
    list_var = [1, 2, 3]
    dict_var = {"key": "value"}

    # Checking and printing the types
    print(f"The type of int_var is: {check_variable_type(int_var)}")
    print(f"The type of float_var is: {check_variable_type(float_var)}")
    print(f"The type of str_var is: {check_variable_type(str_var)}")
    print(f"The type of list_var is: {check_variable_type(list_var)}")
    print(f"The type of dict_var is: {check_variable_type(dict_var)}")