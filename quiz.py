print("====================")
print("       CS QUIZ    ")
print("====================")

score = 0

answer = input("What is 2 + 2? ")

if answer == "4":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What is 5 x 6? ")

if answer == "30":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("Which symbol is used to start a comment in Python? ")

if answer == "#":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What language are we learning? ")

if answer == "Python" or answer == "python":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What is the correct file extension for Python code? ")

if answer == ".py":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What is the correct way to declare a variable in Python? ")

if answer == "variable_name = value":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What is the output of print(2 ** 3)? ")

if answer == "8":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What is the output of print(len('Hello'))? ")

if answer == "5":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What is the output of print(10 // 3)? ")

if answer == "3":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("What is the output of print(10 % 3)? ")

if answer == "1":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print(f"Your score is: {score}. ")
percentage = (score / 10) * 100
print(f"Your percentage is: {percentage:.2f}%. ")

if percentage == 100:
    print("Grade: A+")
elif percentage >= 70-65:
    print("Grade: B")
else:
    print("Grade: F and keep practicing!")