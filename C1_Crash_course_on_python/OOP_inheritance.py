class Fruit:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
    origin = "Asia"  # This is called attribute and function within a class is called method


class Apple(Fruit):
    pass


class Grape(Fruit):
    pass

# Here both the apple and the grape classes inherit from the fruit class. Because of this, they automatically have
# the same constructor, which sets the color and flavor attributes. This is called inheritance.


granny_smith = Apple('green', 'tart')
carnelian = Grape('purple', 'sweet')

print(granny_smith.origin)
print(carnelian.flavor)


# Another example of inheritance

class Animal:
    def __init__(self,name):
        self.name = name
    sound = ""
    def speak(self):
        print("{sound} I am {name}! {sound}".format(sound=self.sound,name=self.name))

class piglet(Animal):
    sound = "oink"

hamlet = piglet("Hamlet")
hamlet.speak()

class cow(Animal):
    sound = "Mooooo"

milky = cow("Milky white")
milky.speak()
