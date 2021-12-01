# python philosophy const
PYTHON_PHILOSOPHY = """
1.  Beautiful is better than ugly.
2.  Explicit is better than implicit.
3.  Simple is better than complex.
4.  Complex is better than complicated.
5.  Flat is better than nested.
6.  Sparse is better than dense.
7.  Readability counts.
8.  Special cases aren't special enough to break the rules.
9.  Although practicality beats purity.
10. Errors should never pass silently.
11. Unless explicitly silenced.
12. In the face of ambiguity, refuse the temptation to guess.
13. There should be one-- and preferably only one --obvious way to do it.
14. Although that way may not be obvious at first unless you're Dutch.
15. Now is better than never.
16. Although never is often better than *right* now.
17. If the implementation is hard to explain, it's a bad idea.
18. If the implementation is easy to explain, it may be a good idea.
19. Namespaces are one honking great idea -- let's do more of those!
    """
# print(PYTHON_PHILOSOPHY)

# words for option to find given words
first_word_to_find = "better"
second_word_to_find = "never"
third_word_to_find = "is"

# symbols for option replace the symbols
symbol_change_old = 'i'
symbol_change_new = '&'

# option for user
option_find_number_of_words = "1. To find number of words '{a}', '{b}' and '{c}' in chosen statemant".format(a = first_word_to_find, b = second_word_to_find, c = third_word_to_find)
option_make_text_uppercase = "2. To print all text uppercase"
option_change_symbols = "3. To replace all '{old_symbol}' to '{new_symbol}'".format(old_symbol = symbol_change_old, new_symbol = symbol_change_new)

# find number of words in given line (naive version)
def find_number_of_words(x):

    print("\nWise choice!")
    start_index = PYTHON_PHILOSOPHY.find(x)
    end_index = PYTHON_PHILOSOPHY.find(str(int(x) + 1))

    user_string = PYTHON_PHILOSOPHY[start_index : end_index]
    print(user_string)

    print("{f1}: {n1}".format(f1 = first_word_to_find, n1 = user_string.count(first_word_to_find.lower())))
    print("{f2}: {n2}".format(f2 = second_word_to_find, n2 = user_string.count(second_word_to_find.lower())))
    print("{f3}: {n3}".format(f3 = third_word_to_find, n3 = user_string.count(third_word_to_find.lower())))

    return True

# print all text uppercase
def print_text_uppercase():

    print(PYTHON_PHILOSOPHY.upper())

    return True
     

# replace given symbols
def replace_symbols():

    print(PYTHON_PHILOSOPHY.replace(symbol_change_old, symbol_change_new))

    return True

# find number of words in given line little bit wisley
def find_number_of_words_wisely(x):

    delimeters = ['.', ',', '-', '*', '!', '\n']

    start_index = PYTHON_PHILOSOPHY.find(x)
    end_index = PYTHON_PHILOSOPHY.find(str(int(x) + 1))

    user_string = PYTHON_PHILOSOPHY[start_index : end_index]
    user_string_lower = user_string.lower()

    clear_string = []

    for symbol in user_string_lower:
        if symbol not in delimeters:
            clear_string.append(symbol)

    words = []
    word = ''
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0

    for symbol in clear_string:
        if symbol != ' ':
            word = word + symbol
        else:
            words.append(word)
            if word == first_word_to_find:
                counter_1 += 1
            if word == second_word_to_find:
                counter_2 += 1
            if word == third_word_to_find:
                counter_3 += 1
            word = ''

    print("{f1}: {n1}".format(f1 = first_word_to_find, n1 = counter_1))
    print("{f2}: {n2}".format(f2 = second_word_to_find, n2 = counter_2))
    print("{f3}: {n3}".format(f3 = third_word_to_find, n3 = counter_3))


    return True


# user choose one option from given 3: find number of words, to make uppercase, to change symbols
while True:
    print("Python philosophy small converter and analyser")
    print(option_find_number_of_words)
    print(option_make_text_uppercase)
    print(option_change_symbols)
    x = input(" What do you want to do? \n Please, choose one option (press 1, 2, or 3 and Enter) ")
    if x == '1':
        while True:
            print(PYTHON_PHILOSOPHY)
            line_to_analyse = input("\nWhich line you want to analyse? Enter number from 1 to 19 ")
            try:
                if int(line_to_analyse) >= 1 and int(line_to_analyse) <= 19:
                    # find_number_of_words(line_to_analyse)
                    find_number_of_words_wisely(line_to_analyse)
                    break
                else:
                    print("It is not an opttion. Please give me number from 1 to 19")
            except ValueError:
                print("It is not an opttion. Please give me number from 1 to 19")
        break
    if x == '2':
        print_text_uppercase()
        break
    if x == '3':
        replace_symbols()
        break
    print("This is not an option. Try again")
