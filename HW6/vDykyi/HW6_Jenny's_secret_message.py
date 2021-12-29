#Jenny's secret message
def greet(name):
    if name != "Johnny":
        return f"Hello, {name}!"
    else:
        return "Hello, my love!"
        
print(greet("Johnny"))
