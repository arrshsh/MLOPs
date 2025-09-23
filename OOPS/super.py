# base class 
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound")

# derived class 
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    
    def speak(self):
        super().speak() # call the base method
        print(f"{self.name} barks, it is a {self.breed}")


# create and instance of dog 
dog = Dog("Golden Retriever")
dog.speak()