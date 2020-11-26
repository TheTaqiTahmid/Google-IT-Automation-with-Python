# Classes and Instances
# Classes define the behavior of all instances of a specific class.
# Each variable of a specific class is an instance or object.
# Objects can have attributes, which store information about the object.
# You can make objects do work by calling their methods.
# The first parameter of the methods (self) represents the current instance.
# Methods are just like functions, but they can only be used through a class.

# class cow():
#     #    def speak(self):
#     #       print("moooooooo")
#     def __init__(self, speak, color):
#         self.speak = speak
#         self.color = color
#
# lali = cow("mooooo", "red")
# print(lali.speak)
# print(lali.color)

class piglet():
    name = "piglet"
    color = "brown"
    years = 0
    def pig_years(self):
        return self.years * 18
    def speak(self):
        print("Hello! my name is {}, and my color is {}".format(self.name,self.color))

hamlet = piglet()
hamlet.name = "Hamlet"
hamlet.speak()
hamlet.years = 5
print(hamlet.pig_years())

# constructor method __init__: with this method we can create a new function with all the desired attributes while creating the object
# If we want python to print a friendly defined message instead of default python message when we try to print an object we use special method called _str__

class Apple:
    def __init__(self,flavor,color):
        self.flavor = flavor
        self.color = color
    def __str__(self):
        return "The color of the object is {}".format(self.color)


Jonagold = Apple("sweet","red")
print(Jonagold.color)
print(Jonagold)

# A docstring is a brief text that explains what something does. It can be seen by using hel function
def to_seconds(hours,minutes,seconds):
    """"Returns the amount of seconds from the given hours, minutes and seconds"""
    h_s = hours * 3600
    m_s = minutes * 60
    return h_s + m_s + seconds
help(to_seconds)