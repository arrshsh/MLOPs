class chatbook:
    def __init__(self):
        self.__username = "" # this makes the said attribute hidden we cannot access it directly 
        self.password = ""
        self.loggedin = False
        self.menu()

    def get_name(self): # getter function
        return self.__username

    def set_name(self, value): # setter function
        self.__username = value


hello =  chatbook()
hello_name = hello.__username # this is how we access the hidden things 
