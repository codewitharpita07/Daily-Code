A = "red"
B = "blue"
temp = "blank"

temp = A  # temp becomes "red"
A = B  # A becomes "blue"
B = temp  # B becomes "red"

print(A)
print(B)

age = 10

if age <= 12:
    print("You are 12 years old or older. Congratulations!")
else:
    print("you are not 12 years old. So you have to pay 500")

marks = 74
if marks >= 35:
    print("You have passed the exam. Congratulations!")
else:
    print("You have failed the exam. Better Luck next time!")

correct_password = "secret123"
user_input = input("Enter the password:")
if user_input == correct_password:
    print("Access granted. Welcome!")
else:
    print("Access denied. Please try again.")

bill_amount = int(input("Enter the bill amount:"))

if bill_amount >= 1000:
    print("Wow! You got 10% discount.")
else:
    print("Sorry! No discount. ")

temperature = 30
if temperature <= 25:
    print("It's too hot!")
else:
    print("The temperature is normal.")

for i in range(5):
    print("hurrah!")

user_age = int(input("Enter your age: "))
if user_age < 5:
    print("Your ticket is free.")
elif user_age >= 5 and user_age <= 18:
    print("Your ticket costs $15.")
else:
    print("Your ticket costs $30.")

user_movie = input("Enter the movie name:")
if user_movie == "sci-fi":
    print("You get a 20% discount code: SPACE20") 
elif user_movie == "comedy":
    print("You get a 15% discount code: COMEDY15")  
else:
    print("You will get 5% discount code: MOVIE5")

user_score = int(input("Enter your score: "))
if user_score < 100:
    print("Keep playing! You are still on level 1.")
elif user_score >= 100 and user_score <= 199:
    print("Great job! You have reached level 2. ")
else:
    print("Super player! You skipped to level 3 and got a golden badge!")


user_ages = [12,19,25,15,30,17]
for user_age in user_ages:
    if user_age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")

passwords = ["abc","mypasser123","hello","secret99","123"]
for password in passwords :
    if len (password) >= 6:
        print("strong password")
    else:
        print("too short!")





