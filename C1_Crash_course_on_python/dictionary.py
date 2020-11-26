# Dictionary stores values as a pair of keys and values. they are defined by second bracket. They are mutable
# In dictionary each key can be present once

file_count = {"jpg": 10, "txt": 14, "csv": 25, "py": 23}
print(file_count["jpg"])

file_count["gif"] = 33
print(file_count)

# If we try to add a key that already exists in the dictionary, the new value associated with the key will replace the old value of that key.

file_count["csv"] = 21
print(file_count)  # CSV value has been changed from 25 to 21

# we can remove a key value pair of a dictionary by sing the del keyword

del file_count["gif"]
print(file_count)

# # Example: The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 1) Add an entry for Epilogue on page 39.
# # 2) Change the page number for Chapter 3 to 24. 3) Display the new dictionary contents. 4) Display True if there is Chapter 5, False if there isn't.
#
# toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# toc["Epilogue"] = 39 # Epilogue starts on page 39
# toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
# print(toc) # What are the current contents of the dictionary?
# print("Chapter 5" in toc) # Is there a Chapter 5?


# Items method returns a tuple for each elemets in the dictionary. The tuple's first element is the key and second element is the value.

for ext, amount in file_count.items():
    print("There are {} files with the .{} extension".format(amount, ext))

# Accessing the keys or values of the dictionary

print(file_count.keys())
print(file_count.values())


# Example of a dictionary containing number of times a letter appears in a string

def get_count(string):
    count = {}
    for letter in string:
        if letter not in count:
            count[letter] = 0
        count[letter] += 1
    return count


print(get_count("This is a string"))
