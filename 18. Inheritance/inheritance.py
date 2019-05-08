class Mammal:
    def walk(self):
        print('Walking...')

# Below Dog and Cat class inherit the Mammal class i.e. all methods and attributes of Mammals are accessible in Dog and Cat class

class Dog(Mammal):
    pass        # Use a 'pass' statement to tell Python that you wanna keep a class empty otherwise it'll generate an error


class Cat(Mammal):
    def meow(self, n):
        print('meow ' * n)


dog = Dog()
dog.walk()      # Prints Walking...

cat = Cat()
cat.walk()      # Prints Walking...
cat.meow(3)     # Prints meow meow meow
