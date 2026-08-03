class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")

dog = Dog()

dog.sound()
dog.bark()