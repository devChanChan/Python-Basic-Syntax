birthYear = int(input("Enter your birth year: "))
age = 2017 - birthYear + 1
if age <= 26 and age >= 20:
    print("College")
elif age < 20 and age >= 17:
    print("High School")
elif age < 17 and age >= 14:
    print("Middle School")
elif age < 14 and age >= 8:
    print("Elementary School")
else:
    print("Not student")
