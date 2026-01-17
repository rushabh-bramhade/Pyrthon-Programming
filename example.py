#print function example 
"""
print ->
Displays output
Does NOT send data back

"""

def addition(a,b):
    c = a + b
    print(c)

output = addition(5,4)
new_output = output * 3 
print(new_output)


#return keyword example 
"""
Immediately stops the execution of the current function, and

Sends a value back to the caller.
"""
def print_add(a,b):
    c = a + b
    return c

output = print_add(3,2)
new_output = output * 3 
print(new_output)





"""
Early Return (Guard Clauses)

Used to exit early when conditions are not met.

def first_element(arr):
    if not arr:
        return None
    return arr[0]


This prevents runtime errors
"""