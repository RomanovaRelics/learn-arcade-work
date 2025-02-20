"""This function calculates the volume of a cylinder."""
def volume_cylinder(height, radius):
    pi = 3.14
    volume = pi * radius ** 2 * height
    return volume

"""Can measurements"""
can_radius = 1.5
can_height = 6

"""Can volume function"""
can_volume = volume_cylinder(can_height, can_radius)
print(can_volume)

"""Two functions that print a sum"""
def sum_print(a, b):
    result = a + b
    print(result)

    """This function returns a sum"""
def sum_return(a, b):
    result = a + b
    return result

"""Assigns sum_return to variable called result. When this is printed, we will get our answer."""
result = sum_return( 4, 3)
print(result)

"""This will print the sum from inside a function I defined."""
sum_print(5, 7)

"""Creates a variable and assigns a value to it and pulls it outside of the function."""
def assigns_x():
    x = 22
    return x

result = assigns_x()
print(result)

"""Increases x by one and prints it"""
def f(x):
    x += 1
    print(x)

x = 44

result = f(x)
print(x)