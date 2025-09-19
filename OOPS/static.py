class chatbook:

    __user_id = 0 # we can keep it as normal var too
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook. __user_id +=1 
        self.__username = "" # this makes the said attribute hidden we cannot access it directly 
        self.password = ""
        self.loggedin = False
        # self.menu()

    def get_name(self): # getter function
        return self.__username

    def set_name(self, value): # setter function
        self.__username = value


user1 = chatbook()
print(user1.id)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)