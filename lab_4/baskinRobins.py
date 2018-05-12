import random
guess_number = random.randint(1,1000)
print("Enter a number(1 ~ 1000)")
user_input = int(input())
while(user_input is not guess_number):
    if(user_input > guess_number):
        print("The number is big")
    else:
        print("The number is small")
    print("Enter a number again")
    user_input = int(input())
else: print("You're right.", "The answer is", user_input, ".")
