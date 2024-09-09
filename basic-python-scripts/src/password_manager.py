def save_password():
    Username = input("Please give the username: ")
    Password = input("Please give the password associated: ")

    with open("password.txt", "w") as f:
        f.write(Username + " | " + Password + "\n")


def load_password():
    with open("password.txt", "r") as f:
        for line in f.readline():
            data = line.rstrip()
            username, password = data.split("|")
            print("Username: " + username + "| Password: " + password)


while True:
    command = input("What would You like to do?(save/load/quit?) ").lower()

    if command == "save":
        save_password()
    elif command == "load":
        load_password()
    elif command == "quit":
        break
    else:
        print("Incorrect, Please enter a correct command ")
        continue

print("Have a good day!")

quit()
