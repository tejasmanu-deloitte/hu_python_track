import pandas as pd

movie_file = pd.read_csv("movies.csv")
admin_detail = pd.read_csv("admin.csv")
user_detail = pd.read_csv("user.csv")


def register_func():
    name = input("Name :")
    email = input("Email :")
    phone = input("Phone :")
    age = input("Age :")
    password = input("Password :")

    lis = [email, phone, age, password]
    return name, lis


def add_edit_new_movie():
    title = input("Title :")
    genre = input("Genre :")
    duration = input("Length :")
    cast = input("Cast :")
    director = input("Director :")
    admin_rating = input("Admin Rating :")
    lang = input("Language :")
    timing = input("Timing :")
    no_of_shows = input("Length :")
    first_show = input("First Show :")
    interval_time = input("Interval Time :")
    gap_btw_show = input("Gap Between Shows :")
    capacity = input("Capacity :")

    lis = [genre, duration, cast, director, admin_rating, lang, timing, no_of_shows, first_show, interval_time,
           gap_btw_show, capacity]

    return title, lis


def login_func(user, password):
    dictionary = dict()
    dictionary["admin"] = "password"
    dictionary["user"] = "pass"

    if dictionary[user] == password:
        return "admin"
    elif (user in dictionary) and (dictionary[user] == password):
        return "user"
    else:
        return "invalid"

def user_display(title):
    lis = list(movie_file[title])

    print("Title :", title , "\n"
          "Genre :", lis[0], "\n"
          "Length", lis[1], "\n"
          "Cast :", lis[2], "\n"
          "Director :", lis[3], "\n"
          "Admin :", lis[4], "\n"
          "Timings :", lis[5], "\n"
          "User Rating :", lis[6])

def book_ticket(title):
    lis = list(movie_file[title])

