
# incorrect
# def correct_tail(body, tail):
#     sub = body.substr(len(body)-len(tail.length))
#     if sub == tai: 
#         return True
#     else:
#         return False




#correct
def correct_tail(body, tail):
    sub = body[len(body)-len(tail)]
    if sub == tail:
        return True
    else:
        return False