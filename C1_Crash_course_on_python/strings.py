# def first_and_last(message):
#     if message[-1] == message[0]:
#         return True
#     return False
#
#
# print(first_and_last("else"))

# String index
# x = "goal.com"
# y = x.index(".")
# print(y)

# # use of .join method
# x = "Hello ".join(["Join ", "will ", "Add ", "string before the join method to each string inside join"])
# print(x)
#
# # Use of split method. It splits a long string by the white space"
# x = "This is another string method".split()
# print(x)

# Use of strip method. Strip method removes any white space at the beginning and at the end of any string
# There is also lstrip and rstrip which removes left and right whitespace of a string 

# string = "  Hello everyone  "
# y = string.split()
# print()
#
# # Convert to upper or lower case
#
# s = "Hello world"
# print(s.upper())
# print(s.lower())

# Format string example
# Format takes care of the data type automatically so that user does not have to

# name = "Taqi"
# number = len(name) * 3
# print("Hello {}, your lucky number is {}".format(name, number))
#
# # Another example of format
# print("Hello {name}, your lucky number is {number}".format(name=name, number=len(name) * 3))


# Another example of format
# price = 7.5
# with_tax = price * 1.09
#
# print("Base price: ${:.2f}, with tax: ${:.2f}".format(price, with_tax))
# # Colon separates the field name from the formatting expression in format method

# Another example of format and alignment

def to_celsius(x):
    return (x - 32) * 5 / 9


for i in range(1, 102, 10):
    print("{:>3} F | {:>6.2f} C".format(i, to_celsius(i)))
