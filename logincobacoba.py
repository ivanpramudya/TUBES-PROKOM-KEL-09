import csv
import random

#menu awal
def menu():
    print("========================================================================================")
    print("=                        SELAMAT DATANG DI PROGRAM PENCARIAN KOST!                     =")
    print("========================================================================================")
    print("")
menu()

def load_user_data():
    # Load user data from the CSV file
    with open('datauser.csv', 'r') as file:
        reader = csv.reader(file)
        user_data = list(reader)
    return user_data

def save_user_data(user_data):
    # Save updated user data to the CSV file
    with open('datauser.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(user_data)

def signin():
    print("==========================================")
    print("")
    print("Sign In")
    username = input("Enter your email or username  : ")
    #username = input("Enter your username      : ")
    password = input("Enter your password           : ")

    user_data = load_user_data()

    for user in user_data:
        if user[0] == username or user[1] == username and user[2] == password:
            print("")
            print("========================================================================================")
            print("                                  INFORMASI PENGGUNA                                    ")
            print("Selamat datang,", user[1])
            return True
    return False


def signup():
    print("==========================================")
    print("")
    print("Sign Up")
    email = input("Enter your email              : ")
    username = input("Enter a username              : ")
    password = input("Enter a password              : ")

    user_data = load_user_data()

    for user in user_data:
        if user[0] == username:
            print("Username already exists. Please try again.")
            return

    user_data.append([email,username, password])
    save_user_data(user_data)
    print("Account created successfully. Please sign in.")
    print("")
    signin()

def akun():
    print("Pilih Sign Up jika belum memiliki akun atau pilih Sign In jika sudah memiliki akun.")
    print("1. Sign In")
    print("2. Sign Up")
    choice = input("Choose an option (1/2)        : ")
    print("")
    if choice == "1":
        if signin():
            print("Login successful!")
            # Call other functions or display menu after successful login
        else:
            print("Invalid username or password.")
            # Call login function again or display error message
    elif choice == "2":
        signup()
    else:
        print("Invalid option.")
        akun()
akun()
    