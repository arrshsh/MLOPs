class chatbook:

    __user_id = 0 # we can keep it as normal var too
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook. __user_id +=1 
        self.__username = "" # this makes the said attribute hidden we cannot access it directly 
        self.password = ""
        self.loggedin = False
        # self.menu()

    @staticmethod # we dont give self to static methods 
    def get_id(): # getter function
        return chatbook.__user_id
    @staticmethod
    def set_id(value): # setter function
        chatbook.__user_id = value
        return chatbook.__user_id


user1 = chatbook()
print(user1.id)

chatbook.set_id(10) # uwing the static method directly, instead of using an object 
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)