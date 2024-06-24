# Input
user_input = input()

if not user_input:
    print("empty")
else:
    for i in range(0, len(user_input), 2):
        print(user_input[i])
