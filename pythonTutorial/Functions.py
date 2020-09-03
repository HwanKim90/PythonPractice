# help(round)

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a,b and c.

    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7)
)

# help(least_difference)

mystery = print()
print(mystery)

print(1, 2, 3, sep=' < ')
print(1, 2, 3)

def greet(who="Colin"):
    print("Hello,", who)

greet()
greet(who="Kaggle")
greet("Hwan")

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n'
)

def mod_5(x):
    """Return the remainder of X after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 41),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n'
)

# help(max)
# help(round)
def round_to_two_places(num):
    """Return the given number rounded to two decimal places.

    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    pass
    return round(num, 2)

print(round_to_two_places(3.14159))