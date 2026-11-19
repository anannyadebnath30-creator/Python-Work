# Q4. Scope, lifetime, global keyword and lambda functions

global_value = 10  # Global variable; available throughout the program

def show_local():
    local_value = 5  # Local variable; exists while this function runs
    print("Local variable inside function:", local_value)
    print("Global variable inside function:", global_value)

def update_global():
    global global_value
    global_value = 25
    print("Global value changed inside function:", global_value)

print("Initial global value:", global_value)
show_local()
update_global()
print("Global value after function call:", global_value)
# local_value cannot be accessed here because it belongs to show_local()

square = lambda x: x * x
cube = lambda x: x * x * x
maximum = lambda a, b: a if a > b else b
addition = lambda a, b: a + b

print("Square of 4:", square(4))
print("Cube of 3:", cube(3))
print("Maximum of 8 and 12:", maximum(8, 12))
print("Addition of 5 and 7:", addition(5, 7))
