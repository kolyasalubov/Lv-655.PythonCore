

def zero_fuel(distance_to_pump, mpg, fuel_left) -> bool:
    
    '''
    Function expects positive ints calculates disctance which you can drive
    and returns True if it's bigger or equal to the distance to a pump, 
    otherwise it returns False
    '''

    if distance_to_pump <= mpg * fuel_left:
        return True 
    else:
        return False

