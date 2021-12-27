import task_9_part_1 as module_1

figures_list = {1:'Rectangle', 2:'Triangle', 3:'Circle'}
user_input = input('Type Rectangle/Triangle/Circle to calculate it\'s square: ').lower()
if user_input == 'rectangle':
    user_input_1 = int(input('Enter side a: '))
    user_input_2 = int(input('Enter side b: '))
    result = module_1.square_of_rectangle(user_input_1, user_input_2)
    print(f'Square of the rectangle is {result}.')

elif user_input == 'triangle':
    user_input_1 = int(input('Enter height h: '))
    user_input_2 = int(input('Enter side a: '))
    result = module_1.square_of_triangle(user_input_1, user_input_2)
    print(f'Square of the triangle is {result}.')

else:
    user_input_1 = int(input('Enter radius r: '))
    result = module_1.square_of_circle(module_1.pi, user_input_1)
    print(f'Square of the circle is {result}.')
    