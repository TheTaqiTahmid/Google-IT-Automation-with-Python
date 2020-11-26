# Always initialize mutable attributes in the constructor. Otherwise they will be applicable to all the instances of
# the class

class Repository:
    def __init__(self):  # Constructor
        self.packages = {}

    def add_package(self, package):
        self.packages[package.name] = package

    def remove_package(self, package):
        del self.packages[package.name]

    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result

# Example

class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
