import mysql.connector as mc
import random

con = mc.connect(host='localhost', user='root', passwd='Riju2001', database='hotel')
c = con.cursor()


def menu():
    print("1.Login as a customer \n2.Login as a staff")
    ans = input("Select an option: ")
    if ans == '1':
        mainmenu()
    elif ans == '2':
        staff_menu()
    else:
        print("This is not a valid option!")
        menu()


def mainmenu():
    print("--Mainmenu-- \n1.Book a room \n2.Book a Banquet hall \n3.Choose a day package \n4.Today's best deals \n5.Cancel a booking \n6.Contact us \n7.I'm a staff (Go back to login menu)")
    ans = input("Select an option from the menu: ")
    if ans == '1':
        book_a_room()
    elif ans == '2':
        book_a_banquet_hall()
    elif ans == '3':
        day_package()
    elif ans == '4':
        best_deals()
    elif ans == '5':
        cancel_book()
    elif ans == '6':
        print("\n\nMail us at \033[1msupport@revenza.in\033[0m or directly call us \nPhone no: 033 9867367582 \n          +91 8578352751 \nOr just fillup the form below and we will contact you shortly")
        ans1 = input("Press 1 to fillup the form \nPress 0 to return to mainmenu \n")
        if ans1 == '1':
            a1 = input("Enter your name: ")
            a2 = input("Enter your email address: ")
            a3 = input("Enter your phone number: ")
            a4 = input("Please tell us the issue you are facing: ")
            a5 = uid()
            print("Your ticket number is: ", a5)
            data1 = (a5, a1, a2, a3, a4)
            sql1 = "insert into need_support values(%s,%s,%s,%s,%s)"
            c.execute(sql1, data1)
            con.commit()
        if ans1 == '0':
            mainmenu()
    elif ans == '7':
        menu()
    else:
        print("This is not a valid option")
        mainmenu()


def book_a_room():
    print("-- Select the room you want to book -- \n1.Guest room                     Tariff: 2,300 INR per night\n2.Deluxe suite                   Tariff: 2,900 INR per night\n3.Premier suite                  Tariff: 3,800 INR per night\n4.Executive suite (Exclusive)    Tariff: 10,000 INR per night\n\nPress 0 to return to mainmenu")
    ans = input("Select an option: ")
    if ans == '1':
        a1 = input("Enter your name: ")
        a2 = input("Enter your age: ")
        a3 = input("Enter your sex: ")
        a4 = input("Enter your phone number: ")
        a5 = input("Enter your residential address: ")
        a6 = input("Enter the number of persons: ")
        if int(a6) > 3:
            print("3 persons can be accomodated in a suite of the selected category \nfor each extra person a charge of \033[1m500 INR per night\033[0m will be added to the total bill")
            a = input("If you want to terminate the process press 0 or press 1 to continue: ")
            if a == '0':
                mainmenu()
        a7 = input("Enter your email address: ")
        a9 = input("Enter your check-in date in YYYY-MM-DD format: ")
        a10 = input("Enter the number of days you want to stay: ")
        s2 = 0
        a8 = ""
        for num in range(101, 120):
            for i in range(int(a10)):
                c.execute(f"select count(no_{str(num)}) from G_avail where no_{str(num)} = date_add(str_to_date('{a9}','%Y-%m-%d'),interval {i} day)")
                s1 = clean(c.fetchall())
                s2 += int(s1)
            if s2 == 0:
                print(f"Your room number is: G{str(num)}")
                a8 += f"G{str(num)}"
                for j in range(int(a10)):
                    c.execute(
                        f"insert into G_avail(no_{str(num)}) values(date_add(str_to_date('{a9}','%Y-%m-%d'),interval {j} day))")
                break
            if num == 120:
                print("Sorry! no guest suite available for the selected dates")
                book_a_room()
        print(f"Congratulations! You have successfully booked a Guest suite from date {a9} for {a10} days")
        print("Your room number number is: ", a8)
        a11 = uid()
        print(f"Your unique id is: {a11}")
        a12 = "0"
        data1 = (a8, a1, a2, a3, a4, a5, a6, a7, a9, a10, a11, a12)
        sql1 = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        con.commit()

    elif ans == '2':
        a1 = input("Enter your name: ")
        a2 = input("Enter your age: ")
        a3 = input("Enter your sex: ")
        a4 = input("Enter your phone number: ")
        a5 = input("Enter your residential address: ")
        a6 = input("Enter the number of persons: ")
        if int(a6) > 3:
            print("3 persons can be accomodated in a suite of the selected category \nfor each extra person a charge of \033[1m500 INR per night\033[0m will be added to the total bill")
            a = input("If you want to terminate the process press 0 or press 1 to continue: ")
            if a == '0':
                mainmenu()
        a7 = input("Enter your email address: ")
        a9 = input("Enter your check-in date in YYYY-MM-DD format: ")
        a10 = input("Enter the number of days you want to stay: ")
        s2 = 0
        a8 = ""
        for num in range(101, 115):
            for i in range(int(a10)):
                c.execute(f"select count(no_{str(num)}) from D_avail where no_{str(num)} = date_add(str_to_date('{a9}','%Y-%m-%d'),interval {i} day)")
                s1 = clean(c.fetchall())
                s2 += int(s1)
            if s2 == 0:
                print(f"Your room number is: D{str(num)}")
                a8 = f"D{str(num)}"
                for j in range(int(a10)):
                    c.execute(
                        f"insert into D_avail(no_{str(num)}) values(date_add(str_to_date('{a9}','%Y-%m-%d'),interval {j} day))")
                    con.commit()
                break
            if num == 115:
                print("Sorry! no Deluxe suites available for the selected dates")
                book_a_room()
        print(f"Congratulations! You have successfully booked a Deluxe suite from date {a9} for {a10} days")
        print("Your room number number is: ", a8)
        a11 = uid()
        print(f"Your unique id is: {a11}")
        a12 = "-"
        data1 = (a8, a1, a2, a3, a4, a5, a6, a7, a9, a10, a11, a12)
        sql1 = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        con.commit()
    elif ans == '3':
        a1 = input("Enter your name: ")
        a2 = input("Enter your age: ")
        a3 = input("Enter your sex: ")
        a4 = input("Enter your phone number: ")
        a5 = input("Enter your residential address: ")
        a6 = input("Enter the number of persons: ")
        if int(a6) > 3:
            print("3 persons can be accomodated in a suite of the selected category \nfor each extra person a charge of \033[1m500 INR per night\033[0m will be added to the total bill")
            a = input("If you want to terminate the process press 0 or press 1 to continue: ")
            if a == '0':
                mainmenu()
        a7 = input("Enter your email address: ")
        a9 = input("Enter your check-in date in YYYY-MM-DD format: ")
        a10 = input("Enter the number of days you want to stay: ")
        s2 = 0
        a8 = ""
        for num in range(101, 115):
            for i in range(int(a10)):
                c.execute(f"select count(no_{str(num)}) from P_avail where no_{str(num)} = date_add(str_to_date('{a9}','%Y-%m-%d'),interval {i} day)")
                s1 = clean(c.fetchall())
                s2 += int(s1)
            if s2 == 0:
                print(f"Your room number is: P{str(num)}")
                a8 = f"P{str(num)}"
                for j in range(int(a10)):
                    c.execute(
                        f"insert into P_avail(no_{str(num)}) values(date_add(str_to_date('{a9}','%Y-%m-%d'),interval {j} day))")
                    con.commit()
                break
            if num == 115:
                print("Sorry! no Premier suites available for the selected dates")
                book_a_room()
        print(f"Congratulations! You have successfully booked a Premier suite from date {a9} for {a10} days")
        print("Your room number number is: ", a8)
        a11 = uid()
        print(f"Your unique id is: {a11}")
        a12 = "-"
        data1 = (a8, a1, a2, a3, a4, a5, a6, a7, a9, a10, a11, a12)
        sql1 = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        con.commit()
    elif ans == '4':
        a1 = input("Enter your name: ")
        a2 = input("Enter your age: ")
        a3 = input("Enter your sex: ")
        a4 = input("Enter your phone number: ")
        a5 = input("Enter your residential address: ")
        a6 = input("Enter the number of persons: ")
        a7 = input("Enter your email address: ")
        a9 = input("Enter your check-in date in YYYY-MM-DD format: ")
        a10 = input("Enter the number of days you want to stay: ")
        s2 = 0
        a8 = ""
        for num in range(101, 105):
            for i in range(int(a10)):
                c.execute(f"select count(no_{str(num)}) from E_avail where no_{str(num)} = date_add(str_to_date('{a9}','%Y-%m-%d'),interval {i} day)")
                s1 = clean(c.fetchall())
                s2 += int(s1)
            if s2 == 0:
                print(f"Your room number is: E{str(num)}")
                a8 = f"E{str(num)}"
                for j in range(int(a10)):
                    c.execute(
                        f"insert into E_avail(no_{str(num)}) values(date_add(str_to_date('{a9}','%Y-%m-%d'),interval {j} day))")
                    con.commit()
                break
            if num == 105:
                print("Sorry! no Executive suites available for the selected dates")
                book_a_room()
        print(f"Congratulations! You have successfully booked a Executive suite from date {a9} for {a10} days")
        print("Your room number number is: ", a8)
        a11 = uid()
        print(f"Your unique id is: {a11}")
        a12 = "-"
        data1 = (a8, a1, a2, a3, a4, a5, a6, a7, a9, a10, a11, a12)
        sql1 = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        con.commit()
    elif ans == '0':
        mainmenu()
    else:
        print("This is not a valid option")
        book_a_room()


def book_a_banquet_hall():
    print("-- Celebrate with us at our luxury banquets --\n \n1.The Sonnet Banquet \n2.Arunodaya Hall  \n3.\033[1mThe Bonvoy\033[0m by Revenza \n\nPress 0 to return to mainmenu")
    ans = input("Please select one option: ")
    if ans == "1":
        print("Excellent choice! \033[1mThe Sonnet Banquet\033[0m is one of the finest and luxurious banquets in the heart of the city \nThe current rate for renting this wonderfull banquet hall is 2,40,000 INR per night \n\033[1mNOTE: Third party catering service is not allowed, one has to go with a catering service \nfrom the restaurant of Revenza!\033[0m")
        ans1 = input("Please select an option: \n1.Book now \n2.View other banquet halls \nYour answer: ")
        if ans1 == '1':
            a1 = input("Enter your name: ")
            a2 = input("Enter your phone number: ")
            a3 = input("Enter your mail id: ")
            a4 = input("Enter your residential address: ")
            a5 = input("Enter the approximate no. of guests: ")
            a6 = input("Enter the event date for which you want to book: ")
            a7 = input("Please tell us for how many nights you want to book: ")
            s3 = 0
            for i in range(int(a7)):
                c.execute(f"select booked from S_avail where booked = date_add(str_to_date('{a6}','%Y-%m-%d'),interval {i} day)")
                s1 = clean(c.fetchall())
                c.execute(f"select count(booked) from S_avail where booked = date_add(str_to_date('{a6}','%Y-%m-%d'),interval {i} day)")
                s2 = clean(c.fetchall())
                s3 += int(s2)
                if s1 != "":
                    print(f"Sorry!the banquet hall is not available for booking on: {s1[-10:]} ")
            if s3 != 0:
                print("You are being redirected to banquet hall booking menu \n")
                book_a_banquet_hall()
            a8 = input("Please tell us about the event in short: ")
            a11 = uid()
            print(f"Your unique id is: {a11}")
            a12 = "SONNET"
            data1 = (a1, a2, a3, a4, a5, a6, a7, a8, a11, a12)
            sql1 = "insert into banquet_book values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            c.execute(sql1, data1)
            for i in range(int(a7)):
                c.execute(f"insert into S_avail(booked) values(date_add(str_to_date('{a6}','%Y-%m-%d'),interval {i} day))")
                con.commit()
            print(f"Congratulations! you have successfully booked the banquet hall from the date {a6} for {a7} days")
            print("Our manager will connect with you shortly!")
        if ans1 == '2':
            book_a_banquet_hall()
    elif ans == '2':
        if ans == "1":
            print("Excellent choice! \033[1mArunodaya Hall\033[0m is a one of a kind hall in the heart of the city \nThe current rate for renting this wonderfull banquet hall is 1,80,000 INR per night \n\033[1mNOTE: Third party catering service is not allowed, one has to go with a catering service \nfrom the restaurant of Revenza!\033[0m")
            ans1 = input("Please select an option: \n1.Book now \n2.View other banquet halls \nYour answer: ")
            if ans1 == '1':
                a1 = input("Enter your name: ")
                a2 = input("Enter your phone number: ")
                a3 = input("Enter your mail id: ")
                a4 = input("Enter your residential address: ")
                a5 = input("Enter the approximate no. of guests: ")
                a6 = input("Enter the event date for which you want to book: ")
                a7 = input("Please tell us for how many days you want to book: ")
                s3 = 0
                for i in range(int(a7)):
                    c.execute(f"select booked from A_avail where booked = date_add(str_to_date('{a6}','%Y-%m-%d'),interval {i} day)")
                    s1 = clean(c.fetchall())
                    c.execute(f"select count(booked) from A_avail where booked = date_add(str_to_date('{a6}','%Y-%m-%d'),interval {i} day)")
                    s2 = clean(c.fetchall())
                    s3 += int(s2)
                    if s1 != "":
                        print(f"Sorry!the banquet hall is not available for booking on: {s1[-10:]} ")
                if s3 != 0:
                    print("You are being redirected to banquet hall booking menu \n")
                    book_a_banquet_hall()
                a8 = input("Please tell us about the event in short: ")
                a11 = uid()
                print(f"Your unique id is: {a11}")
                a12 = "ARUN"
                data1 = (a1, a2, a3, a4, a5, a6, a7, a8,a11,a12)
                sql1 = "insert into banquet_book values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                c.execute(sql1, data1)
                for i in range(int(a7)):
                    c.execute(
                        f"insert into A_avail(booked) values(date_add(str_to_date('{a6}','%Y-%m-%d'),interval {i} day))")
                    con.commit()
                print(
                    f"Congratulations! you have successfully booked the hall from the date {a6} for {a7} days")
                print("Our manager will connect with you shortly!")
            if ans1 == '2':
                book_a_banquet_hall()
    elif ans == '3':
            print("Excellent choice! \033[1mThe Bonvoy by Revenza\033[0m is the most luxurious banquet Revenza has to offer \nThe current rate for renting this wonderfull banquet hall is 5,20,000 INR per night \n\033[1mNOTE: Third party catering service is not allowed, one has to go with a catering service \nfrom the restaurant of Revenza!\033[0m")
            ans1 = input("Please select an option: \n1.Book now \n2.View other banquet halls \nYour answer: ")
            if ans1 == '1':
                a1 = input("Enter your name: ")
                a2 = input("Enter your phone number: ")
                a3 = input("Enter your mail id: ")
                a4 = input("Enter your residential address: ")
                a5 = input("Enter the approximate no. of guests: ")
                a6 = input("Enter the event date for which you want to book: ")
                a7 = input("Please tell us for how many days you want to book: ")
                s3 = 0
                for i in range(int(a7)):
                    c.execute(f"select booked from B_avail where booked = date_add(str_to_date('{a6}','%Y-%m-%d'),interval {i} day)")
                    s1 = clean(c.fetchall())
                    c.execute(f"select count(booked) from B_avail where booked = date_add(str_to_date('{a6}','%Y-%m-%d'),interval {i} day)")
                    s2 = clean(c.fetchall())
                    s3 += int(s2)
                    if s1 != "":
                        print(f"Sorry!the banquet hall is not available for booking on: {s1[-10:]} ")
                if s3 != 0:
                    print("You are being redirected to banquet hall booking menu \n")
                    book_a_banquet_hall()
                a8 = input("Please tell us about the event in short: ")
                a11 = uid()
                print(f"Your unique id is: {a11}")
                a12 = "BONVOY"
                data1 = (a1, a2, a3, a4, a5, a6, a7, a8,a11,a12)
                sql1 = "insert into banquet_book values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                c.execute(sql1, data1)
                for i in range(int(a7)):
                    c.execute(
                        f"insert into B_avail(booked) values(date_add(str_to_date('{a6}','%Y-%m-%d'),interval {i} day))")
                    con.commit()
                print(
                    f"Congratulations! you have successfully booked the hall from the date {a6} for {a7} days")
                print("Our manager will connect with you shortly!")
            if ans1 == '2':
                book_a_banquet_hall()
    elif ans == '0':
        mainmenu()
    else:
        print("This is not a valid option")
        book_a_banquet_hall()


def day_package():
    print("-- Day package menu -- \n1.Picnic package \n2.Day package (Guest suite) \n3.Day package (Premier suite) \n\nPress 0 to return to mainmenu")
    ans = input("Select an option: ")
    if ans == '1':
        print("We have a 2000 sqft. area with a large pond that can be a perfect picnic spot. The rent is: 25,000 INR for one day (Excluding catering services)\n")
        a1 = input("Enter your name: ")
        a2 = input("Enter your phone number: ")
        a3 = input("Enter your mail id: ")
        a4 = input("Enter your residential address: ")
        a5 = input("Enter the approximate no. of guests: ")
        a6 = input("Enter the event date for which you want to book: ")
        c.execute(f"select booked from picnic_avail where booked = str_to_date('{a6}','%Y-%m-%d')")
        s1 = clean(c.fetchall())
        if s1 != "":
            print(f"Sorry!the picnic spot is not available for booking on: {s1[-10:]} ")
            print("You are being redirected to Day package menu")
            day_package()
        c.execute(f"insert into picnic_avail(booked) values(str_to_date('{a6}','%Y-%m-%d'))")
        con.commit()
        a11 = uid()
        print(f"Your unique id is: {a11}")
        data1 = (a1, a2, a3, a4, a5, a6, a11)
        sql1 = "insert into picnic_book values(%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        print(f"Congratulations! you have successfully booked picnic spot for the date {a6}")
        print("Our manager will connect with you shortly!")
    elif ans == '2':
        print("This Day package includes buffet lunch for 2 persons at our restaurant and stay at one of our Guest suites (check out at 6pm) at a rate 3000 INR only")
        a1 = input("Enter your name: ")
        a2 = input("Enter your age: ")
        a3 = input("Enter your sex: ")
        a4 = input("Enter your phone number: ")
        a5 = input("Enter your residential address: ")
        a6 = "2"
        a7 = input("Enter your email address: ")
        a9 = input("Enter your check-in date in YYYY-MM-DD format: ")
        a10 = "1"
        s2 = 0
        for num in range(101, 120):
            for i in range(int(a10)):
                c.execute(
                    f"select count(no_{str(num)}) from G_avail where no_{str(num)} = date_add(str_to_date('{a9}','%Y-%m-%d'),interval {i} day)")
                s1 = clean(c.fetchall())
                s2 += int(s1)
            if s2 == 0:
                print(f"Your room number is: G{str(num)}")
                a8 = f"G{str(num)}"
                for j in range(int(a10)):
                    c.execute(
                        f"insert into G_avail(no_{str(num)}) values(date_add(str_to_date('{a9}','%Y-%m-%d'),interval {j} day))")
                    con.commit()
                quit()
            if num == 120:
                print("Sorry! no guest suite available for the selected dates")
                book_a_room()
        print(f"Congratulations! You have successfully booked a day package for 2 persons for date {a9}")
        print("Your room number number is: ", a8)
        a11 = uid()
        print(f"Your unique id is: {a11}")
        a12 = "DAYGUEST"
        data1 = (a8, a1, a2, a3, a4, a5, a6, a7, a9, a10, a11,a12)
        sql1 = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        con.commit()
    elif ans == '3':
        print("This Day package includes buffet lunch for 2 persons at our restaurant and stay at one of our Premier suites (check out at 6pm) at a rate 3700 INR")
        a1 = input("Enter your name: ")
        a2 = input("Enter your age: ")
        a3 = input("Enter your sex: ")
        a4 = input("Enter your phone number: ")
        a5 = input("Enter your residential address: ")
        a6 = "2"
        a7 = input("Enter your email address: ")
        a9 = input("Enter your check-in date in YYYY-MM-DD format: ")
        a10 = "1"
        s2 = 0
        for num in range(101, 115):
            for i in range(int(a10)):
                c.execute(
                    f"select count(no_{str(num)}) from P_avail where no_{str(num)} = date_add(str_to_date('{a9}','%Y-%m-%d'),interval {i} day)")
                s1 = clean(c.fetchall())
                s2 += int(s1)
            if s2 == 0:
                print(f"Your room number is: P{str(num)}")
                a8 = f"P{str(num)}"
                for j in range(int(a10)):
                    c.execute(
                        f"insert into P_avail(no_{str(num)}) values(date_add(str_to_date('{a9}','%Y-%m-%d'),interval {j} day))")
                    con.commit()
                quit()
            if num == 115:
                print("Sorry! no Premier suites available for the selected dates")
                book_a_room()
        print(f"Congratulations! You have successfully booked a day package (premier suite) for 2 persons for date {a9}")
        print("Your room number number is: ", a8)
        a11 = uid()
        print(f"Your unique id is: {a11}")
        a12 = 'DAYPREMIER'
        data1 = (a8, a1, a2, a3, a4, a5, a6, a7, a9, a10, a11, a12)
        sql1 = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        con.commit()
    elif ans == '0':
        mainmenu()
    else:
        print("This is not a valid option")
        day_package()


def best_deals():
    print("Welcome to the best deals menu -- currently there are 3 offerss going on \n1.Book a Deluxe suite for atleast 4 days and get flat 30% off \n2.Book a Executive suite for 7 days at 40,000 INR only \n3.Book day package (premier suite) at 2,800 INR only \n\nPress 0 to return to mainmenu")
    ans = input("Please select an offer: ")
    if ans == '1':
        a1 = input("Enter your name: ")
        a2 = input("Enter your age: ")
        a3 = input("Enter your sex: ")
        a4 = input("Enter your phone number: ")
        a5 = input("Enter your residential address: ")
        a6 = input("Enter the number of persons: ")
        if int(a6) > 3:
            print(
                "3 persons can be accomodated in a suite of the selected category \nfor each extra person a charge of \033[1m500 INR per night\033[0m will be added to the total bill")
            a = input("If you want to terminate the process press 0 or press 1 to continue: ")
            if a == '0':
                mainmenu()
        a7 = input("Enter your email address: ")
        a9 = input("Enter your check-in date in YYYY-MM-DD format: ")
        a10 = input("Enter the number of days you want to stay: ")
        if int(a10) < 4:
            print("The offer is only valid for for a stay of atleast 4 days, as you are staying {a10} days the offer can't be used!")
            ans1 = input("If you wish to book the suite without an offer press 1 (you will be redirected to the main booking menu) \npress 0 to return to best deals menu")
            if ans1 == '0':
                best_deals()
            if ans1 == '1':
                book_a_room()
        s2 = 0
        for num in range(101, 115):
            for i in range(int(a10)):
                c.execute(
                    f"select count(no_{str(num)}) from D_avail where no_{str(num)} = date_add(str_to_date('{a9}','%Y-%m-%d'),interval {i} day)")
                s1 = clean(c.fetchall())
                s2 += int(s1)
            if s2 == 0:
                print(f"Your room number is: D{str(num)}")
                a8 = f"D{str(num)}"
                for j in range(int(a10)):
                    c.execute(
                        f"insert into D_avail(no_{str(num)}) values(date_add(str_to_date('{a9}','%Y-%m-%d'),interval {j} day))")
                    con.commit()
                quit()
            if num == 115:
                print("Sorry! no Deluxe suites available for the selected dates")
                book_a_room()
        print(f"Congratulations! You have successfully booked a Deluxe suite from date {a9} for {a10} days")
        print("Your room number number is: ", a8)
        a11 = uid()
        print(f"Your unique id is: {a11}")
        a12 = "DELUXE30"
        data1 = (a8, a1, a2, a3, a4, a5, a6, a7, a9, a10, a11, a12)
        sql1 = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        con.commit()
    elif ans == '2':
            a1 = input("Enter your name: ")
            a2 = input("Enter your age: ")
            a3 = input("Enter your sex: ")
            a4 = input("Enter your phone number: ")
            a5 = input("Enter your residential address: ")
            a6 = input("Enter the number of persons: ")
            a7 = input("Enter your email address: ")
            a9 = input("Enter your check-in date in YYYY-MM-DD format: ")
            a10 = "7"
            s2 = 0
            for num in range(101, 105):
                for i in range(int(a10)):
                    c.execute(
                        f"select count(no_{str(num)}) from E_avail where no_{str(num)} = date_add(str_to_date('{a9}','%Y-%m-%d'),interval {i} day)")
                    s1 = clean(c.fetchall())
                    s2 += int(s1)
                if s2 == 0:
                    print(f"Your room number is: E{str(num)}")
                    a8 = f"E{str(num)}"
                    for j in range(int(a10)):
                        c.execute(
                            f"insert into E_avail(no_{str(num)}) values(date_add(str_to_date('{a9}','%Y-%m-%d'),interval {j} day))")
                        con.commit()
                    quit()
                if num == 105:
                    print("Sorry! no Executive suites available for the selected dates")
                    book_a_room()
            print(f"Congratulations! You have successfully booked a Executive suite from date {a9} for {a10} days")
            print("Your room number number is: ", a8)
            a11 = uid()
            print(f"Your unique id is: {a11}")
            a12 = "EXECUTIVE7"
            data1 = (a8, a1, a2, a3, a4, a5, a6, a7, a9, a10, a11, a12)
            sql1 = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            c.execute(sql1, data1)
            con.commit()
    elif ans == '3':
        print(
            "This Day package includes buffet lunch for 2 persons at our restaurant and stay at one of our Premier suites (check out at 6pm)")
        a1 = input("Enter your name: ")
        a2 = input("Enter your age: ")
        a3 = input("Enter your sex: ")
        a4 = input("Enter your phone number: ")
        a5 = input("Enter your residential address: ")
        a6 = "2"
        a7 = input("Enter your email address: ")
        a9 = input("Enter your check-in date in YYYY-MM-DD format: ")
        a10 = "1"
        s2 = 0
        for num in range(101, 115):
            for i in range(int(a10)):
                c.execute(
                    f"select count(no_{str(num)}) from P_avail where no_{str(num)} = date_add(str_to_date('{a9}','%Y-%m-%d'),interval {i} day)")
                s1 = clean(c.fetchall())
                s2 += int(s1)
            if s2 == 0:
                print(f"Your room number is: P{str(num)}")
                a8 = f"P{str(num)}"
                for j in range(int(a10)):
                    c.execute(
                        f"insert into P_avail(no_{str(num)}) values(date_add(str_to_date('{a9}','%Y-%m-%d'),interval {j} day))")
                    con.commit()
                quit()
            if num == 115:
                print("Sorry! no Premier suites available for the selected dates")
                book_a_room()
        print(
            f"Congratulations! You have successfully booked a day package (premier suite) for 2 persons for date {a9}")
        print("Your room number number is: ", a8)
        a11 = uid()
        print(f"Your unique id is: {a11}")
        a12 = 'DPREMIER2800'
        data1 = (a8, a1, a2, a3, a4, a5, a6, a7, a9, a10, a11, a12)
        sql1 = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        con.commit()
    elif ans == '0':
        mainmenu()
    else:
        print("This is not a valid option")
        best_deals()


def staff_menu():
    print("-- Staff menu -- 1.Make the bill for a customer \n2.Book a book room for a customer \n3.Book a banquet for a customer \n4.Book a day package for a customer \n5.Cancel a booking \n6.See customer queries \n7.Not a staff (return to login menu)")
    ans = input("Select an option: ")
    if ans == "1":
        cid = input("Please enter the customer id")
        for i in range(3):
            if i == 0:
                c.execute(f"select booking_date,duration,hall from banquet_book where uid = {cid}")
                s2 = clean(c.fetchall())
                if s2 != []:
                    s3 = list(map(str, s2.split()))
                    if s3[2] == "SONNET":
                        bill1 = 240000*int(s3[0])
                        print(f"The bill is: {bill1} INR")
                        for i in range(int(s3[1])):
                            c.execute(
                                f"delete from S_avail where booked = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                            con.commit()
                    if s3[2] == "ARUN":
                        bill2 = 180000*int(s3[0])
                        print(f"The bill is: {bill2} INR")
                        for i in range(int(s3[1])):
                            c.execute(
                                f"delete from A_avail where booked = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                            con.commit()
                    if s3[2] == "BONVOY":
                        bill3 = 520000*int(s3[0])
                        print(f"The bill is: {bill3} INR")
                        for i in range(int(s3[1])):
                            c.execute(
                                f"delete from A_avail where booked = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                            con.commit()
            if i == 1:
                c.execute(f"select check_in,ID,persons,duration,code from customer where uid = {cid}")
                s2 = dateclean(c.fetchall())
                if s2 != []:
                    person=0
                    s3 = list(map(str, s2.split()))
                    if int(s3[2]) > 3:
                        person += (int(s3[2])-3)*500
                    if s3[1][0] == 'G':
                        if s3[4] == '0':
                            b1 = 2300*int(s3[3]) + person*int(s3[3])
                            print(f"The bill is: {b1} INR")
                        if s3[4] == 'DAYGUEST':
                            print(f"The bill is: 3000 INR")
                        for i in range(int(s3[3])):
                            c.execute(
                                f"delete from G_avail where no_{str(s3[1][1:])} = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                            con.commit()
                    if s3[1][0] == 'D':
                        if s3[4] == '0':
                            b2 = 2900*int(s3[3]) + person*int(s3[3])
                            print(f"The bill is: {b2} INR")
                        if s3[4] == 'DELUXE30':
                            b2 = (2900*int(s3[3]) + person*int(s3[3]))*0.7
                            print(f"The bill is: {b2} INR")
                        for i in range(int(s3[3])):
                            c.execute(
                                f"delete from D_avail where no_{str(s3[1][1:])} = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                            con.commit()
                    if s3[1][0] == 'P':
                        if s3[4] == '0':
                            b3 = 3800*int(s3[3]) + person*int(s3[3])
                            print(f"The bill is: {b3} INR")
                        if s3[4] == 'DAYPREMIER':
                            print("The bill is: 3700 INR")
                        if s3[4] == 'DPREMIER2800':
                            print("The bill is: 2800 INR")
                        for i in range(int(s3[3])):
                            c.execute(
                                f"delete from P_avail where no_{str(s3[1][1:])} = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                            con.commit()
                    if s3[1][0] == 'E':
                        if s3[4] == '0':
                            b4 = 10000*int(s3[3])
                            print(f"The bill is: {b4} INR")
                        if s3[4] == 'EXECUTIVE7':
                            print("The bill is: 40000 INR")
                        for i in range(int(s3[3])):
                            c.execute(
                                f"delete from E_avail where no_{str(s3[1][1:])} = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                            con.commit()
            if i == 2:
                c.execute(f"select book_date from picnic_book where uid = {cid}")
                s2 = dateclean(c.fetchall())
                if s2 != []:
                    s3 = list(map(str, s2.split()))
                    c.execute(f"DELETE from picnic_avail where booked = str_to_date('{s3[0]}','%Y-%m-%d')")
                    con.commit()
                    print("The bill is: 25000 INR")
    elif ans == '2':
        print("\033[1mNOTE: you are redirected to the room booking page. After successfully booking a room please forward the room number and unique id to the customer\033[0m")
        book_a_room()
    elif ans == '3':
        print("\033[1mNOTE: you are redirected to the banquet hall booking page. After successfully reserving a banquet hall please forward the unique id to the customer\033[0m")
        book_a_banquet_hall()
    elif ans == '4':
        print("\033[1mNOTE: you are redirected to the day package page. After successfully completing the booking please forward the room number and unique id to the customer\033[0m")
        day_package()
    elif ans == '5':
        cancel_book()
    elif ans == '6':
        print("Currently active customer queries are: ")
        c.execute("select * from need_support")
        s = c.fetchall()
        for i in range(len(s)):
            s1 = clean(s[i][:4])+"   The issue: "+s[i][4]
            print(s1)
        ans2 = input("\n\n\n Enter the ticket number which is already resolved: ")
        c.execute(f"DELETE from need_support where ticket_no = {ans2}")
        con.commit()
        print("The query list is now updated")
    elif ans == '7':
        menu()
    else:
        print("This is not a valid option")
        staff_menu()


def cancel_book():
    cid = input("Please enter the customer id: ")
    for i in range(3):
        if i == 0:
            c.execute(f"select booking_date,duration,hall from banquet_book where uid = {cid}")
            s2 = dateclean(c.fetchall())
            if s2 != []:
                s3 = list(map(str, s2.split()))
                if s3[2] == "SONNET":
                    for i in range(int(s3[1])):
                        c.execute(
                            f"delete from S_avail where booked = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                        con.commit()
                if s3[2] == "ARRUN":
                    for i in range(int(s3[1])):
                        c.execute(
                            f"delete from A_avail where booked = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                        con.commit()
                if s3[2] == "BONVOY":
                    for i in range(int(s3[1])):
                        c.execute(
                            f"delete from B_avail where booked = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                        con.commit()
        if i == 1:
            c.execute(f"select check_in,duration,ID from customer where uid = {cid}")
            s2 = dateclean(c.fetchall())
            if s2 != []:
                s3 = list(map(str, s2.split()))
                if s3[2][0] == "G":
                    for i in range(int(s3[1])):
                        c.execute(
                            f"delete from G_avail where no_{str(s3[2][1:])} = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                        con.commit()
                if s3[2][0] == "D":
                    for i in range(int(s3[1])):
                        c.execute(
                            f"delete from D_avail where no_{str(s3[2][1:])} = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                        con.commit()
                if s3[2][0] == "P":
                    for i in range(int(s3[1])):
                        c.execute(
                            f"delete from P_avail where no_{str(s3[2][1:])} = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                        con.commit()
                if s3[2][0] == "E":
                    for i in range(int(s3[1])):
                        c.execute(
                            f"delete from E_avail where no_{str(s3[2][1:])} = date_add(str_to_date('{s3[0]}','%Y-%m-%d'),interval {i} day)")
                        con.commit()
        if i == 2:
            c.execute(f"select book_date from picnic_book where uid = {cid}")
            s2 = dateclean(c.fetchall())
            if s2 != []:
                s3 = list(map(str, s2.split()))
                c.execute(f"DELETE from picnic_avail where booked = str_to_date('{s3[0]}','%Y-%m-%d')")
                con.commit()


def uid():
    d = ""
    for i in range(0, 4):
        n = random.randint(0, 9)
        c1 = str(n)
        d += c1
    return d


def clean(str1):
    str1 = str(str1)
    str2 = ""
    for i in range(len(str1)):
        if str1[i] != "'" and str1[i] != "(" and str1[i] != ")" and str1[i] != "," and str1[i] != "]" and str1[i] != "[":
            str2 = str2 + str1[i]
    return str2


def dateclean(s1):
    s1 = str(s1)
    s2 = clean(s1)
    s3 = s2[13:]
    s4 = s3.replace(" ", "-", 2)
    return s4


menu()
