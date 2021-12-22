import script_with_functions


def input_from_user(name_or_requested_value:str) -> float:
    '''
    function requests value from user trys to converts it into float
    catches value error ant interrupts script, or returns float if everything is good
    '''
    try: 
        user_input_value = float(input(f'Please enter {name_or_requested_value} value: '))
    except ValueError as error_msg:
        print('Unfortunately, only numbers inputs are valid for this script, bye', error_msg)
        exit()
    return user_input_value


def printing_result(area:float) -> None:
    '''
    Expects one float argument for area and prints result into console
    returns None
    '''
    print(f'Area of your polygon is: {area}')


def main_loop() -> None:
    '''
    Master loop function promts user to input figure and calls user_input function set amount of times based on user's reply
    Then input from user goes into function which will calculate area, calculations would be printed by printing_result function
    If input from user isn't valid function will interapt script execution
    Returns None
    '''
    user_selection = input('Please enter figure of each you need to calculate area for(rectangle, triangle or circle): ')

    if user_selection == 'rectangle':
        side_a = input_from_user('side a')
        side_b = input_from_user('side b')
        printing_result(script_with_functions.calculating_rectangle_area(side_a, side_b))

    elif user_selection == 'triangle':
        height = input_from_user('height')
        side_a = input_from_user('side a')
        printing_result(script_with_functions.calculate_triangle_are(height, side_a))

    elif user_selection == 'circle':
        radius = input_from_user('radius')
        printing_result(script_with_functions.calculate_circle_area(radius))

    else:
        print('Your input was invelid and program would be terminated')
        exit()

if __name__ == '__main__':
    main_loop()

