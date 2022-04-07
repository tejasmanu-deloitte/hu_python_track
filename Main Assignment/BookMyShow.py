import Base

print("""
******Welcome to BookMyShow******
1. Login
2. Register new account
3. Exit""")

num = int(input("Enter : "))

if num == 1:
    print("******Welcome to BookMyShow*******")
    user = input("User: ")
    password = input("Password: ")
    admin_user = Base.login_func(user, password)

if num == 2:
    print("****Create new Account***** ")
    Base.register_func()

if num == 3:
    exit(0)

if admin_user == "admin":
    print("1. Admin  Login:")
    print("******Welcome Admin*******")
    print("1. Add new Movie Info \n"
          "2. Edit Movie Info \n"
          "3. Delete Movies \n"
          "4. Logout")

    opt = int(input("Enter your choice :"))

    if opt == 1:
        pass