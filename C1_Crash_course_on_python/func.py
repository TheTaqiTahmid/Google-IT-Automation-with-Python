def greetings(name, department):
    print("hello " + name, "Welcome to " + department, "department")


greetings("Taqi", "Sensor Hardware")


# Returning values instead of printing
def area_triangle(height, base):
    return (0.5 * height * base)


x = area_triangle(2, 3)
y = area_triangle(5, 7)
sum = x + y
print(sum)


# converting seconds into hours, minutes, and seconds

def conversion(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - minutes * 60 - hours * 3600
    return hours, minutes, remaining_seconds


hours, minutes, seconds = conversion(3665)
print(hours,minutes,seconds)
