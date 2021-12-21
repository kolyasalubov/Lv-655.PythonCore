# Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, 
# площу кола pi*r**2 і цей скрипт використати в іншому модулі, 
# в якому ми запитуємо користувача площу якої фігури він хоче обчислити. 

# (для виконання завдання необхідно імпортувати  модуль math, 
# а з нього функцію pow() та значення змінної пі, 
# модуль1, який містить три функції для знаходження площ, 
# модуль2, в якому імпортований модуль1 і виконується основна логіка програми).



import my_module

while True:
    print("Make your choice ?","1.Triangle ","2.Rectangle","3.Circle","4.Exit", sep="\n")
    try:
        case = int(input("Enter number 1, 2, 3, 4: "))
        if case == 1:
            print("Triangle")
            a,b,c = [float(x) for x in input("Enter tree sides of triangle here as a b c: ").split()]
            print("Square_rectangle is ",  my_module.square_triangle(a,b,c))
            continue
        elif case == 2:
            print("Rectangle")
            a,b = [float(x) for x in input("Enter tree sides of rectangle here as a b : ").split()]
            print("Square of rectangle is: ", my_module.squeare_rectangle(a,b)) 
            continue
        elif case == 3:
            print("Circle")
            radius = float(input("Enter radius: "))
            print("Square of circle is: ", my_module.square_circle(radius))
            continue
        elif case==4:
            break
        else:
            print("Wrong choise try again\n")    
    except ValueError:
        print("Try again bro\n")