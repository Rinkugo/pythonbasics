
from admin import admin_main
def login(role):

    rl = None
    if role.lower() == "a":
        rl = "admin"
    elif role.lower() == "m":
        rl = "manger"
    elif role.lower() == "c":
        rl = "chef"
    elif role.lower() == "cu":
        rl = "customer"
    

    try_count = 0
    while try_count < 3:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        try: 
            with open("data/users.txt", "r") as file: 
                users = file.readlines()
            if not users: 
                print("User not found")
                return
        
            for user in users: 
                stored_users = user.split(',')[0]
                stored_password = user.split(',')[1]
                psw = stored_password.replace("\n", "")
                if username == stored_users and password == psw:
                    print("Login successful.")
                    admin_main(username)
                    # return user
                else:
                    print("Login Fail.")

                
            
        except Exception as e: 
            print("Raised error", e)
        try_count += 1
        print("Maximum attempt done.")
        return
    
    




