import math

# 2.1 Objects

class Shape:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("perimeter")

    def area(self):
        raise NotImplementedError("area")

class Square(Shape):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def perimeter(self):
        return 4 * self.size

    def area(self):
        return self.size ** 2

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return math.pi * 2 * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

examples = [Square("sq", 3), Circle("circle", 3)]
# for thing in examples:
#     name = thing.name
#     perimeter = thing.perimeter()
#     area = thing.area()
#     print(f"{name} has perimeter {perimeter:.2f} and area {area:.2f}")

def square_perimeter(thing):
    return 4 * thing["size"]

def square_area(thing):
    return thing["size"] ** 2

def square_new(name, size):
    return {
        "name": name,
        "size": size,
        "perimeter": square_perimeter,
        "area": square_area
    }

examples = [square_new("sq", 3)]

# to use the methods like square_perimeter or square_area
def call(thing, method_name):
    return thing[method_name](thing)

# for ex in examples:
#     name = ex["name"]
#     perimeter = call(ex, "perimeter")
#     area = call(ex, "area")
#     print(f"{name} has perimeter {perimeter:.2f} and area {area:.2f}")

# 2.2 Classes
def square_perimeter(thing):
    return 4 * thing["size"]

def square_area(thing):
    return thing["size"] ** 2

Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "_className": "square"
}

def square_new(name, size):
    return {
        "name": name,
        "size": size,
        "_class": Square
    }

def call(thing, method_name):
    return thing["_class"][method_name](thing)

examples = [square_new("sq", 3)]

for ex in examples:
    name = ex["name"]
    perimeter = call(ex, "perimeter")
    area = call(ex, "area")
    className = ex["_class"]["_className"]
    print(f"{name} is in {className} class, has perimeter {perimeter:.2f}, and area {area:.2f}")