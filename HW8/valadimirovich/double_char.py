# There is mistace in the task discription, in the last work it says "once" and should say "twice"

def double_char(s:str) -> str:
    '''
    Expects str, return a string in which each character (case-sensitive) is repeated twice.
    '''
    string=''
    return string.join([item + item for item in s])

