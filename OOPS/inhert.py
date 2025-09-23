# simple inheritance 
# base class 
class Animal:
    def __init__(self, name):
        self.name = name 

    def speak(self):
        print(f"{self.name} makes a sound. ")


# derived class 
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# create an instance of animal 
animal = Animal("Generic Animal")
animal.speak()

# creating an instance of dog 
dog = Dog("Buddy")
dog.speak()