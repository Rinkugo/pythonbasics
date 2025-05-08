
# -Manage staff - Manager, Chef (Add, Edit, Delete)
# - View sales report based on month, chef etc.
# - View feedback sent by customers.
# - Update own profile
def select_staff():
    staff = input("select M for Manager/ C for Chef: ")
    if staff.lower() == "m":
        staff = "Manager"
    elif staff.lower() == "c":
        staff = "Chef"
    return staff
def add_staff():
    staff = select_staff()
    username = input("Enter the username: ")
    password = input("ENter the password: ")

    try: 
        with open("data/users.txt", "r") as f:
            users = f.readlines()

        for user in users:
            if username in user.split(','):
                print("User already exists.")
                return
        with open("data/users.txt", "a") as a:
            a.write(f"{username},{password},{staff}\n")
            print(f"{staff} registered successful.")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Invalid", e)

def view_staff():
    try: 
        with open("data/users.txt", "r") as r:
            users = r.readlines()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Invalid", e)

def edit_staff():
    # staff = select_staff()
    username1 = input("Enter the name of the user: ")
    
    try: 
        data = []
        is_updated = False
        with open("data/users.txt", "r") as r:
            users = r.readlines()
            for user in users:
                username, password, role = user.split(',')
                if username == username1:
                    password = input("Enter the new password: ")
                    is_updated = True
                data.append(f"{username},{password},{role}")
            
        with open("data/users.txt", "w") as w:
            w.writelines(data)

        if is_updated:
                print("Password updated successfully.")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Invalid", e)
    
def delete_staff():
    staff = select_staff()
    username2 = input("Enter the username to delete: ")

    try: 
        data = []
        is_deleted = False
        with open("data/users.txt", "r") as r:
            users = r.readlines()
        
            for user in users:
                username,_,_ = user.split(',')
                if username2 != username:
                    data.append(user)
                else:
                    is_deleted = True
        with open("data/users.txt", "w") as w:
            w.writelines(data)
    
        if is_deleted:
            print("User deleted successfully.")
        
        manage_staff()

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Invalid, e")


def manage_staff():
    print("1. Add staff")
    print("2. View staff")
    print("3. Edit staff")
    print("4. Delete staff")
    option = input("Enter the option chosen: ")
    if option == "1":
        add_staff()
    if option == "2":
        view_staff()
    if option == "3":
        edit_staff()
    if option == "4":
        delete_staff()
    pass
def view_sales_report():
    pass
def view_feedback():
    pass
def update_profile():
    pass
def admin_main(username):   
    print ("1. Manage staff")
    print("2. View Sales report")
    print("3. View feedback sent by customers")
    print("4. Update own profile")
    choice = input("Enter choice: ")
    if choice == "1":
        manage_staff()
    elif choice == "2":
        view_sales_report()
    elif choice == "3":
        view_feedback()
    elif choice == "4":
        update_profile()
    

    # can be used in VS code Terminal, Git bash, Command
    # to push in GIT -
# git init (to initialise GIT) (only to be used once in the initial phase)
# git add . (to add entire files), git add specific folder/ files (example - git add admin.py)
# git commit -m "Message" (specify the task in the message)
# git remote add origin url (the url of github repository) (to be used only in the intital phase)
# git push origin branchname
# git clone url (paste the url of repo copied from github)