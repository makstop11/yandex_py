# def alphanumeric_restriction(s):
#     if type(s) is int or type(s) is str:
#         return True
#     else:
#         return False

#-----------------------------------------------------------------------------------------

def alphanumeric_restriction(s):
    if s.isdigit() or s.isalpha():
        return True
    else:
        return False