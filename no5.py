# def check(ls):
#     if ls[0] == ls[-1]:
#         return "True"
#     else:
#         return "False"
# lst = eval(input())
# print(check(lst))

# import ast

# def check(ls):
#     if not isinstance(ls, list):
#         return "Error: Input is not a list"
#     if len(ls) == 0:
#         return "Error: List is empty"
#     if ls[0] == ls[-1]:
#         return "True"
#     else:
#         return "False"

# try:
#     lst = ast.literal_eval(input())
#     print(check(lst))
# except (SyntaxError, ValueError):
#     print("Error: Invalid input")

import ast

def check(ls):
    if not isinstance(ls, list):
        return "False"
    if len(ls) == 0:
        return "False"
    if ls[0] == ls[-1]:
        return "True"
    else:
        return "False"

try:
    user_input = input()
    lst = ast.literal_eval(user_input)
    print(check(lst))
except (SyntaxError, ValueError):
    print("False")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
