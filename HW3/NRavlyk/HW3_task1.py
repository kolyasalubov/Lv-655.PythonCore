import this
import codecs

zen_of_python = codecs.encode(this.s, 'rot13')

# line_true = False
# while not line_true:
while True:
    number_of_line_str = input("Please input number of string 1-19: ")
    if number_of_line_str.isdecimal():
        number_of_line = int (number_of_line_str)
        if  number_of_line>0 and number_of_line<20:
            break
            # line_true = True
number_of_line += 1
split_zen = zen_of_python.split('\n')
string_zen = split_zen[number_of_line]
print(string_zen)


n_better = string_zen.count('better')
n_never = string_zen.count('never')
n_is = string_zen.count('is')

print(f"better ocupps {n_better} times")
print(f"never ocupps {n_never} times")
print(f"is ocupps {n_is} times")

print ("String in upper case: ", string_zen.upper())

new_string = string_zen.replace('i','&')
print ("String with replased i: ", new_string)

