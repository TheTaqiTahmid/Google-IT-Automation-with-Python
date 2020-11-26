# Recursion is a programm where the function call itself until the value reaches the base value

# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(4))


def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base and number != 1:
        # If number is equal to 1, it's a power (base**0).
        return False
    elif number == base or number == 1:
        return True

    # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False
