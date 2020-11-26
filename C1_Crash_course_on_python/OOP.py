#
# Dot notation allows you access any of the abilities the object might have (called methods) or information it might store (called attributes)
class Apple:
    color = ""
    flavor = ""


jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.color.upper())

golden = Apple()
golden.color = "yellow"
