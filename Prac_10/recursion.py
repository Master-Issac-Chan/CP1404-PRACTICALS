"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))
# 5 % 2 = 1    2 + 1 = 3 (FA)
# 4 % 2 = 0    2 + 0 = 2
# 3 % 2 = 1    1 + 1 = 2
# 2 % 2 = 0    1 + 0 = 1
# 1 % 2 = 1    1 + 0 = 1
# 0 % 2 (STOP) -> ^

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be,
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)
# TODO: 5. fix do_something() so that it works according to the docstring
# 4 * 4 = 16
# 3 * 3 = 9
# 2 * 2  = 4
# 1 * 1 = 1
# 0 * 0 = 0
# (STOP)

def block_pyramid_2D(n):
    if n <= 0:
        return 0
    return n + block_pyramid_2D(n - 1)

block_pyramid_2D(6)
print(block_pyramid_2D(6))
