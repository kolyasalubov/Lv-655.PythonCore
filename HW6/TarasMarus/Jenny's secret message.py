def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    if  name != "Johnny":
        return "Hello, {name}!".format(name=name)

