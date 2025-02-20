def print_hello():
    """Prints Hello!"""
    print("Hello!")


def print_goodbye():
    """Prints Bye!"""
    print("Bye!")


def print_number(my_number):
    """Prints my_number"""
    print(my_number)


def add_numbers(a, b):
    sum = a + b
    return(sum)


def main():
    """ This is my main program function """
    print_hello()
    print_goodbye()
    print_number(55)
    print_number(25)
    print_number(8)
    add_numbers(11, 7)
    print(add_numbers)

# Call (run) the main function
main()
