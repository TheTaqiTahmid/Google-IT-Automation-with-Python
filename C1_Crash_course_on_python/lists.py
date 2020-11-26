# lists are mutable and they are defined by third bracket: That means they can be changed. The immutable lists are called tuples and they are defined by first bracket.


# def get_word(sentence, n):
#     # Only proceed if n is positive
#     if n > 0:
#         words = sentence.split()
#         # Only proceed if n is not more than the number of words
#         if n <= len(words):
#             return words[n - 1]
#     return("")
#
# print(get_word("This is a lesson about lists", 4))

# Items can be added to the end of the list by using append method, or any other place using the insert method
# Items can be removed from the lists using the remove method by inputting the value, or using the pop method by inputting the index

# x = []
# x.append("you")
# x.insert(0,'Hey!')
# print(x)
# x[0] = "Hey" # changing the value from the list at the index 0
# print(x)
# x.remove("you")
# x.pop(0)
# print(x)


# The skip_elements function returns a list containing every other element from an input list, starting with the first element.
# Complete this function to do that, using the for loop to iterate through the input list.

# def skip_elements(elements):
# #    # Initialize variables
# #    new_list = []
# #    i = 0
# #
# #    # Iterate through the list
# #    for e in elements:
# #       # Does this element belong in the resulting list?
# #       if e == elements[i]:
# #          # Add this element to the resulting list
# #          new_list.append(e)
# #       # Increment i
# #          if i < len(elements) - 2:
# #             i+=2
# #          else:
# #             i = i
# #
# # print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# # print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# # print(skip_elements([])) # Should be []


# Tuple example:
# Tuples are immutable: they cannot be changed but they can be unpacked into variables
# Just to clarify lists can also be unpacked into variables

x = ('1', '2', '3')
(first, second, third) = x
print(first, second, third)


# Enumerate function returns both index and the value of a list
# Enumerate function example

def skip_elements(elements):
    new_list = []
    for i, q in enumerate(elements):
        if i % 2 == 0:
            new_list.append(q)
    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

# Tuple inside a list and unpacking it

people = [('Taqi', 'taqi@gmail.com'), ('Tahmid', 'tahmid@gmail.com')]
for name, email in people:
    print('{} <{}>'.format(name, email))

# List comprehension let us create new lists based on sequences or ranges
# List comprehension example

# At first with for loop
multiples = []

for i in range(1, 11):
    multiples.append(i * 7)
print(multiples)

# Now with list comprehension
muultiples = [x * 7 for x in range(1, 11)]
print(muultiples)

# Another example
languages = ['Python', 'java', 'C', 'Go']
lengths = [len(language) for language in languages]
print(lengths)

# Another example: Create a list of numbers from 1 to 100 which are divisible by 3
x = [x for x in range(0, 101) if x % 3 == 0]
print(x)



