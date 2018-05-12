int_input = 1
while int_input < 10 and int_input > 0:
    print("Which dan do you want to play?")
    user_input = input()
    int_input = int(user_input)
    if int_input >= 10 or int_input <= 0:
        break
    else:
        for i in range(1, 10):
          result = int_input * i
          print(user_input, "X", i, "=", result)
