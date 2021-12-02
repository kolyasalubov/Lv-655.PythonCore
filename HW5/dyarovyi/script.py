while True:
    login = input("Enter login: ")

    if login == "First":
        print("Hello, {}!".format(login))
        break

    print("Error. Try again.")