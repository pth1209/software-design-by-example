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

# 2.3 Arguments
def show_args(title, *args, **kwargs):
    print(f"{title} args '{args}' and kwargs '{kwargs}'")

show_args("nothing")
show_args("one unnamed argument", 1)
show_args("one named argument", second="2")
show_args("one of each", 3, fourth="4")

def show_spread(left, middle, right):
    print(f"left {left} middle {middle} right {right}")

all_in_lst = [1,2,3]
show_spread(*all_in_lst)
all_in_dict = {"right": 30, "left": 10, "middle": 20}
show_spread(**all_in_dict)

def square_larger(thing, size):
    return call(thing, "area") > size

Square = {
    "permieter": square_perimeter,
    "area": square_area,
    "larger": square_larger,
    "_classname": "Square"
}

examples = [square_new("sq", 3)]

def call(thing, method_name, *args):
    return thing["_class"][method_name](thing, *args)

for ex in examples:
    result = call(ex, "larger", 10)
    print(f"is {ex['name']} larger than 10? {result}")

# Section 2.4: Inheritance
class Shape:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("perimeter")

    def area(self):
        raise NotImplementedError("area")

    def density(self, weight):
        return weight / self.area()

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

examples = [Square("sq", 3), Circle("ci", 2)]
for ex in examples:
    n = ex.name
    d = ex.density(5)
    print(f"{n}: {d:.2f}")