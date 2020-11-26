x = 1
product = 1
while x < 10:
    product = product * x
    x += 1
    print(product)

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()


# Write a function that finds if a value is a power of another value
# def is_power_of(number, base):
#     if number / base == 1 or number == 1:
#         return True
#     elif number / base <= 10 and number != 1:
#         return False
#     return is_power_of(number / base, base)
#
#
# print(is_power_of(1, 2))
