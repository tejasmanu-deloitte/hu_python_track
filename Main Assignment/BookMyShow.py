import pandas as pd

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
    name, user_details = Base.register_func()
    Base.user_detail[name] = user_details

if num == 3:
    exit(0)

if admin_user == "invalid":
    print("Invalid username or password")
    # continue

if admin_user == "admin":
    print("1. Admin  Login:")
    print("******Welcome Admin*******")
    print("1. Add new Movie Info \n"
          "2. Edit Movie Info \n"
          "3. Delete Movies \n"
          "4. Logout")

    opt = int(input("Enter your choice :"))

    if opt == 1:
        print("******Welcome Admin*******")
        title, movie_details = Base.add_edit_new_movie()
        Base.movie_file[title] = movie_details
        Base.movie_file.to_csv("movies.csv",index=False)

    elif opt == 2:
        print("******Welcome Admin*******")
        Base.add_edit_new_movie()
        title, movie_details = Base.add_edit_new_movie()
        Base.movie_file[title] = movie_details
        Base.movie_file.to_csv("movies.csv",index=False)

    elif opt == 3:
        print("******Welcome Admin*******")
        title = input("Title of the movie to be deleted: ")

if admin_user == "user":
    print("2. User Login")
    print("******Welcome User1******* ")
    file = pd.read_csv("movies.csv")
    movies = list(file.columns)

    for i in range(1, len(movies), 1):
        print(i, ". ", movies[i])

    print((i + 1), ". ", "Logout")

    movie = input("Enter movie: ")
    func = Base.user_display(movies[movie])
