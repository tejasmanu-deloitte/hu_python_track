# import Base
#
#
# def add_edit_new_movie():
#     df1 = pd.DataFrame()
#
#     df1["title"] = input("Title")
#     df1["genre"] = input("Genre")
#     df1["duration"] = input("Length :")
#     df1["cast"] = input("Cast :")
#     df1["director"] = input("Director :")
#     df1["admin_rating"] = input("Admin Rating :")
#     df1["lang"] = input("Language :")
#     df1["timing"] = input("Timing :")
#     df1["no_of_shows"] = input("Length :")
#     df1["first_show"] = input("First Show :")
#     df1["interval_time"] = input("Interval Time :")
#     df1["gap_btw_show"] = input("Gap Between Shows :")
#     df1["capacity"] = input("Capacity :")
#
#     print(df1)
#
#     # with open('movies.csv', 'w') as f:
#     #     for key in dict1.keys():
#     #         f.write("%s, %s, " % (key, dict1[key]))
#     #
#     # with open('movies.csv', 'r') as csv_file:
#     #     reader = csv.reader(csv_file)
#     #     mydict1 = dict(reader)
#
#
#


x = 10
Booked_seat = 0
prize_of_ticket = 0
Total_Income = 0
Row = int(input('Enter number of Row - \n'))
Seats = int(input('Enter number of seats in a Row - \n'))
Total_seat = Row * Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]


class chart:

    @staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j + 1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

    @staticmethod
    def find_percentage():
        percentage = (Booked_seat / Total_seat) * 100
        return percentage


class_call = chart
table_of_chart = class_call.chart_maker()

while x != 0:
    print('1 for Show the seats \n2 Select Timings \n3 for Buy a Ticket ',
          '\n4 for Show booked Tickets User Info \n0 for Exit')
    x = int(input('Select Option - '))
    if x == 1:
        if Seats < 10:
            for seat in range(Seats):
                print(seat, end='  ')
            print(Seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, Seats):
                print(seat, end=' ')
            print(Seats)
        if Seats < 10:
            for num in table_of_chart.keys():
                print(int(num) + 1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num) + 1, end='  ')
                else:
                    print(int(num) + 1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant Seats = ', Total_seat - Booked_seat)
        print()

    elif x == 2:
        time = {
            "1": "8.00 - 12.00",
            "2": "1.00 - 300"
        }
        print('Select the Timing')
        print(time)
        t = input("Select your time:")
        x = time[t]
        print("Successful! , enjoy movie at" + x)


    elif x == 3:
        Row_number = int(input('Enter Row Number - \n'))
        Column_number = int(input('Enter Column Number - \n'))
        if Row_number in range(1, Row + 1) and Column_number in range(1, Seats + 1):
            if table_of_chart[str(Row_number - 1)][str(Column_number)] == 'S':
                conform = input('yes for booking and no for Stop booking - ')
                person_detail = {}
                if conform == 'yes':
                    person_detail['Name'] = input('Enter Name - ')
                    person_detail['Gender'] = input('Enter Gender - ')
                    person_detail['Age'] = input('Enter Age - ')
                    person_detail['Phone_No'] = input('Enter Phone number - ')
                    table_of_chart[str(Row_number - 1)][str(Column_number)] = 'B'
                    Booked_seat += 1
                    # Total_Income += prize_of_ticket
                else:
                    continue
                Booked_ticket_Person[Row_number - 1][Column_number - 1] = person_detail
                print('Booked Successfully')
            else:
                print('This seat already booked by some one')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    elif x == 4:
        Enter_row = int(input('Enter Row number - \n'))
        Enter_column = int(input('Enter Column number - \n'))
        if Enter_row in range(1, Row + 1) and Enter_column in range(1, Seats + 1):
            if table_of_chart[str(Enter_row - 1)][str(Enter_column)] == 'B':
                person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Phone number - ', person['Phone_No'])

            else:
                print()
                print('---**---  Vacant seat  ---**---')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    else:
        print()
        print('***  Invalid Input  ***')
        print()

import pandas as pd

df = pd.read_csv("movies.csv")

print(df)