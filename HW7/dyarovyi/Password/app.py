from module import check_validity

password = input("Enter password: ")
print("The password is {}".format("valid" if check_validity(password) else "invalid"))