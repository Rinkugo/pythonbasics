from register import register_user
from login import login
def main():
    role = input("Select the role(A,M,C,CU): ")
    Option = input("Register (r) or Login (l): ")
    if Option == "r":
        register_user(role)
    elif Option == "l": 
        login(role)
    
main()

    