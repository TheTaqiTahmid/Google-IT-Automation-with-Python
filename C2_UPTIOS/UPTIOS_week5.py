# Testing in Python
# Software testing: The process of evaluating computer code to determine whether or not it does what you except it to do
# Test can help make good code great
# Types of testing: Automated and Manual tests, Unit and Integration tests, etc.

""" def summation(x, y):
    return x + y


assert summation(2, 3) == 5, 'Should be 5' """

# Unit Test: Used to verify that small, isolated parts of a program are correct. 
import re
def rearrange_name(name):
    result = re.search(r'^([\w.]*), ([\w. ]*)$', name)
    """ Edge cases are inputs to our code that produce unexpected results, 
    and are found at the extreme ends of the ranges of input we imagine 
    our programs will typically work with.    """ 
    if result is None:
        result = re.search(r'^([\w.]*)$', name)
        if result is None:
            return ''
        return result[1]
    return '{} {}'.format(result[2], result[1])

print(rearrange_name('Taqi'))

# White-Box and Black-Box testing:
# White_Box testing: Relies on test creators knowledg of the software being tested to construct the test cases 
# Black-Box testing: Written with an awareness of what the program is supposed to do- its requirements or specifications
# but not how it does it. It is less likely to be biased by the code. 

# Integration Test: Used to verify that the interactions between the different pieces of code in integrated environments 
# are working the way we expect them to. It usually tests all the modules that are verified by unit test and combine them into group to test 

# Regression Test: A variant of unit tests that are usually written as part of a debugging and troubleshooting process 
# that is written after a bug has been identified in order to ensure the bug doesn't show up again. 

# Smoke Test/ Buid verification Test: Smoke test serve as a kind of sanity check to find major bugs in a program. 
# Smoke test answer basic questions like, does the program run?

# Load Test: These tests verify that the system behaves well when it's under significant load.
# Test Suite: A group of tests of one or different kinds is commonly referred to as test suite. 

# Test driven development: TDD calls for creating the test before writing the code.
# But creating some tests first make sure that you've thought about the problem that you're trying to solve and some different 
# approaches that you might use to accomplish it.

# Try Except statement
# The code in the except block is only executed if one of the instructions in try block raises an error of the matching type. 
# Raising error: raise is used to raise an error. 

def validate_user(name, minlen):
    assert type(name) == str, 'name must be a string'  # Assert raises assertion error 
    if minlen < 1:
        raise ValueError("minlen must be atleast 1")
    if len(name) < minlen:
        return False
    if not name.isalnum():
        return False
    else:
        return True

print(validate_user('name', 4))


