from datetime import datetime

def enter_data():
    name = input("Enter name: ")
    surname = input("Enter surname: ")

    while True:
        date_of_birth = input("Enter date of birth (dd.mm.yyyy): ")
        try:
            datetime.strptime(date_of_birth, "%d.%m.%Y")
            break
        except ValueError:
            print("Invalid format. Please use dd.mm.yyyy.")

    while True:
        phone_number = input("Enter phone number (9 digits): ")
        if phone_number.isdigit() and len(phone_number) == 9:
            break
        else:
            print("Invalid phone number. It must be 9 digits.")

    while True:
        pesel = input("Enter PESEL (11 digits): ")
        if pesel.isdigit() and len(pesel) == 11:
            break
        else:
            print("Invalid PESEL. It must be 11 digits.")

    return (f" Name: {name} \n Surname: {surname} \n Date of birth: {date_of_birth} \n "
            f"phone number: {phone_number} \n pesel: {pesel} \n \n"
            f"-----------------------")

def add_to_file():
    new_entry = enter_data()
    try:
        with open("data.txt", "r") as file:
            existing_entries = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        existing_entries = []
    if new_entry in existing_entries:
        print("Data exists")
    else:
        with open ("data.txt", "a") as file:
            file.write(new_entry + "\n")
        print("Data added successfully")
add_to_file()
