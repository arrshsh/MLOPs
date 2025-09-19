class chatbook:
    def __init__(self): # this is called self/constructor/dunder method
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""
    Welcome the chatbook! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit




""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_message()
        else:
            exit()

    def signup(self):
        email  = input("Enter your email here: ")
        pwd = input("Enter your password here: ")
        self.username = email
        self.password  = pwd
        print("You have signed up successfully! \n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup first by pressing 1 in the main menu")
        else:
            email  = input("Enter your email here: ")
            pwd = input("Enter your password here: ")
            if self.username == email and self.password == pwd:
                print("You have signed in successfully!\n")
                self.loggedin = True
            else:
                print("Please input the correct credentials\n")
                 
        self.menu()
    
    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here: ")
            print(f"Following content has been posted: \n {txt}\n")
        else:
            print("You need to sign in first to post something\n")
        self.menu()

    def send_message(self):
        if self.loggedin == True:
            txt = input("Enter your message here: ")
            frnd = input("Enter your friend's name: ")
            print(f"Your message {txt} has been sent to {frnd}")
        else:
            print("You need to sign in first ")
        print("\n")
        self.menu()




# user = chatbook()
