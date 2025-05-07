
def register_user(role):

    rl = None
    if role.lower() == "a":
        rl = "admin"
    elif role.lower() == "m":
        rl = "manager"
    elif role.lower() == "c":
        rl = "chef"
    elif role.lower() == "cu":
        rl = "customer"

    try: 
        username = input("enter new username: ")
        password = input("enter new password: ")
        
        with open("data/users.txt", "r") as f:
            users = f.readlines()

        for user in users: 
            if username in user.split(','):
                print("Username already exists.")
                return

        with open("data/users.txt", "a") as w:
            w.write(f"{username},{password},{rl}\n")
            print("Registration successful.")
        
    except FileNotFoundError:
        print("File not found.")

    except Exception as e: 
        print("Invalid", e)





