# Regular Expression (regex or regexp): Allows us to search a text for string matching a specific pattern. We can
# import re module in python to use the regular expression grep is a powerful tool in linux CLI to search for strings
# in a text file and show the lines that contains it. It is case sensitive. Ex: grep <string> <file path>. To search
# for string regardless of case we have to pass -i parameter in the command. Ex: Ex: grep <string> <file path> Grep
# has a list of reserved characters that gives extra meaning to the patterns that we create. For example,
# the dot matches any character. This means that if we include a dot in our expression, that dot is a wildcard that
# can be replaced by any other character in the results. Let's check out an example of this.
# Ex: grep l.rts <file path>, it will return alerts, blirts, flirts etc.
# '^' and '$' returns the lines that start with and ends with our passed string respectively.
# Ex: grep ^fruit <file path> will return the lines that start with fruit.
# Ex: grep end$ <file path> will return the lines that start with end.
# Reference: regex101.com

import re  # re is regular expression module

#
# result = re.search(r"aza", "bazaar")  # r means this is a raw string and it should not interpret to anything
# print(result)
#
# result2 = re.search(r"aza", "maze")
# print(result2)
#
# print(re.search(r"^X", "Xenon"))
#
# print(re.search(r"p.ng", "penguin"))
# print(re.search(r"p.ng", "clapping"))
#
# # If we want our search to be case insensitive:
# print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
#
# # Regular expression character classes
# print(re.search(r'[Pp]ython', "python"))  # We can put both upper case and lower case p inside the square bracket
# print(re.search(r'[a-z]way', "The end of the highway"))
# print(re.search(r'[a-z]way', "What a way"))  # Other examples: [A-Z], [0-9] etc.
# print(re.search(r'cloud[a-zA-Z0_9]', "cloudy"))  # The character classes can also be combined in the square bracket
# print(re.search(r'cloud[a-zA-Z0_9]', "cloud9"))  # The character classes can also be combined in the square bracket
# print(re.search(r'[,.!?;:]', "This sentence contains exclamation point!"))
#
# # Sometimes we may want to match any characters that aren't in a group.
# print(re.search(r'[^a-zA-Z]', "This is a sentence with spaces."))  # It looks for any character that is not a letter
# print(re.search(r'[^a-zA-Z ]', "This is a sentence with spaces."))  # Also added space that we don't want to match
#
# # If we want to match alternative symbols:
# print(re.search(r'cat|dog', "I like cats."))
# print(re.search(r'cat|dog', "I like dogs."))
# print(re.search(r'cat|dog', "I like dogs and cats."))  # Here we have both matches but search only show the first match
#
# # In order to show all the matches use findall method of the re module
# print(re.findall(r'cat|dog', "I like dogs and cats."))
#
# # Repeated Matches (Repetition qualifier)
# print(re.search(r'py.*n', "pygmalion"))  # This means we have expanded the search and expect match for any number of
# # characters between py and n.
# print(re.search(r'py.*n', "python programming"))  # * takes as many characters possible! This behaviour is called greedy
# print(re.search(r'py[a-z]*n', "python programming"))  # If we want to match only letters
#
# # The plus character matches one or more occurrences of the character that comes before it
# print(re.search(r'o+l+', "goldfish"))
# print(re.search(r'o+l+', "woolly"))
# print(re.search(r'o+l+', "boil"))  # This does not match because there is i in between o and l.
#
# # The question mark symbol is yet another multiplier. It means either zero or one occurrence of the character before
# # it. It can be used for adding optional characters.
# print(re.search(r'p?each', "To each their own"))
# print(re.search(r'p?each', "I love peaches"))
#
# # Escaping characters. Matching escaping characters such as . ? $ etc by using \ before them.
# print(re.search(r'\.com', "welcome"))
# print(re.search(r'\.com', "mydomain.com"))
#
# # \w matches any alphanumeric characters
# print(re.search(r'\w*', "And_this_is_another"))
# # \d is used to match digits, \s for matching whitespace characters, and \b for matching word boundaries.
#
# # Regular expression in action.
# print(re.search(r'^A.*a$', "Argentina"))  # The country names starts and ends with a.
# print(re.search(r'^A.*a$', "Azerbaijan"))
#
# # To define a valid variable name: The variable can contain any alphanumeric character but starts with letter
# pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
# print(re.search(pattern, '_this_is_a_valid_variable_name'))
# print(re.search(pattern, 'this is not a valid variable name'))
# print(re.search(pattern, 'my_variable1'))
# print(re.search(pattern, '1my_variable1'))

# Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an
# uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark,
# or exclamation point.
# import re
# def check_sentence(text):
#   result = re.search(r"^[A-Z][a-z ]*[.?!]$", text)
#   return result != None
#
# print(check_sentence("Is this is a sentence?")) # True
# print(check_sentence("is this is a sentence?")) # False
# print(check_sentence("Hello")) # False
# print(check_sentence("1-2-3-GO!")) # False
# print(check_sentence("A star is born.")) # True

# The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it
# contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes,
# and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu",
# etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers,
# beginning and end-of-line characters, and character classes.

# import re
# def check_web_address(text):
#   pattern = r'[a-zA-Z0-9_\-.+]*\.[a-zA-Z]*$'
#   result = re.search(pattern, text)
#   return result != None
#
# print(check_web_address("gmail.com")) # True
# print(check_web_address("www@google")) # False
# print(check_web_address("www.Coursera.org")) # True
# print(check_web_address("web-address.com/homepage")) # False
# print(check_web_address("My_Favorite-Blog.US")) # True


# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12,
# with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or
# PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just
# learned can you use here?

# import re
# def check_time(text):
#   pattern = r'(1[0-2]|[1-9]):[0-5][0-9] ?[aApP][mM]$'
#   result = re.search(pattern, text, re.IGNORECASE)
#   return result != None
#
# print(check_time("12:45pm")) # True
# print(check_time("9:59AM")) # True
# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False


# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by
# parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is
# met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for
# text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular
# expression in this function:

# def contains_acronym(text):
#   pattern = r'[(][A-Z0-9][A-Za-z0-9]*[)]'
#   result = re.search(pattern, text)
#   return result != None
#
# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


# # Capturing groups: Capturing groups are portions of the pattern that are enclosed in parentheses
# result = re.search(r'^(\w*), (\w*)$', "Lovelace, Ada")
# print(result.group())
# print(result[0])  # Entire captured string
# print(result[1])  # First group of the captured string
# print(result[2])  # Second group of captured string
#
# def rearrange_name(name):
#   result = re.search(r'^(\w*), (\w*)$',name)
#   #result = re.search(r'^([\w \.-]*), ([\w \.-]*)$', name)  # This expression is when we use middle name or initials
#   if result is None:
#     return name
#   return '{} {}'.format(result[2], result[1])
#
# print(rearrange_name("Tahmid, Taqi"))

# Numeric repetition qualifiers
# print(re.search(r'[a-zA-Z]{5}', 'a ghost'))  # We have searched for consecutive 5 alphabetic characters
# print(re.findall(r'[a-zA-Z]{5}', 'a scary ghost appeared'))
# print(re.findall(r'\b[a-zA-Z]{5}\b', 'a scary ghost appeared'))  # To search for words with exactly 5 letters
# print(re.findall(r'[a-zA-Z]{5,10}', 'I really like strawberries'))  # If want to match a range of 5 to 10 letter words
# print(re.findall(r'[a-zA-Z]{5,}', 'I really like strawberries'))  # If we want to match at least 5 to max letter words
# print(re.findall(r's\w{,20}', 'I like strawberries'))  # If we want to match up to 20 letter words that starts with 's'
#
#
# # Defining a function to extract process ID from log file
# def extract_pid(log_line):
#     regex = r'\[(\d+)\]'
#     result = re.search(regex, log_line)
#     if result is None:
#         return ""
#     return result[1]
#
#
# print(extract_pid("This is a log file including a process ID [12345]"))


# # Defining a function to extract process ID from log file along with process info
# def extract_pid(log_line):
#     regex = r"\[(\d+)\]: ([A-Z]+) "
#     result = re.search(regex, log_line)
#     if result is None:
#         return None
#     return "{} ({})".format(result[1], result[2])
#
#
# print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
# print(extract_pid("99 elephants in a [cage]"))  # None
# print(extract_pid("A string that also has numbers [34567] but no uppercase message"))  # None
# print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))  # 67890 (RUNNING)
#
# # Other functions in re module
# print(re.split(r'[.?!]]', 'One sentence. Another one! Is this the last sentence?'))  # This function splits the passed
# # string based on the characters in regex
# print(re.split(r'([.?!])', 'One sentence. Another one! Is this the last sentence?'))  # If we want to get both sentence
# # and the notation mark
# sub = re.sub(r"[\w%.+-]+@[\w.-]+", '[REDACTED]', "Received and email for go_nuts95@my.example.com")
# print(sub)  # This sub function substitutes matched string with another given one
#
# # First name last name interchange example using sub function
# print(re.sub(r'^([\w .-]*), ([\w .-]*)$', r'\2 \1', 'Tahmid, Taqi'))  # backslash followed by number means the
# # corresponding capture group



# Question 1 We're working with a CSV file, which contains employee information. Each record has a name field,
# followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers,
# and needs to be modified to the international format, with "+1-" in front of the phone number. Fill in the regular
# expression, using groups, to use the transform_record function to do that.

# def transform_record(record):
#     new_record = re.sub(r',([\d\-]*),', r',+1-\1,', record)
#     return new_record
#
#
# print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# # Sabrina Green,+1-802-867-5309,System Administrator
# print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# # Melody Daniels,+1-846-687-7436,Programmer

# The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the
# regular expression to do that.

import re
def multi_vowel_words(text):
  pattern = r'[a-zA-Z]*[aeiou]{3,}[a-zA-Z]*'
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []