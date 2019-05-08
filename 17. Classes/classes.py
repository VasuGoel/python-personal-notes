# We use Class to define new types. These types can have methods that we define in the body of class and attributes that we can set anywhere in the program

class Point:
    def move(self):
        print('Moving point...')

    def draw(self):
        print('Drawing point...')


p1 = Point()    # Creating an object of class Point
p1.move()
p1.draw()

# Defining atributes that belong to particular object
p1.x = 10
p1.y = 20
print(f'p1(x, y): ({p1.x}, {p1.y})\n')


# Since, each object is a different instance of Point class, atributes of point 1 won't be accessible in point 2
p2 = Point()
p2.move()
p2.draw()
# print(f'p2(x, y): ({p2.x}, {p2.y})')        AttributeError: 'Point' object has no attribute 'x'
