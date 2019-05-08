# Constructor is a special method which is used to initialize the attributes of a particular instance of class
# Methods in a class expect the first argument to be self. This self parameter is passed internally by python as it always sends a reference to itself when calling a method, even if it's unused within the method

class Point:
    def __init__(self, x, y):         # Constructor. Note __init__ contains double unserscore
        self.x = x
        self.y = y

    def move(self):
        print(f'Moving point...({self.x}, {self.y})')

    def draw(self):
        print(f'Drawing point...({self.x}, {self.y})')


p1 = Point(10, 20)
print(f'p1(x, y): ({p1.x}, {p1.y})')
p1.move()
p1.draw()

# Updating the attribute of particular instance of class
p1.x = 30
print(f'After updating, p1(x, y): ({p1.x}, {p1.y})')
p1.move()
p1.draw()
