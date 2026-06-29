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
if temperature <= 40:
    print("It's too hot!")
else:
    print("The temperature is normal.")

for i in range(5):
    print("hurrah!")



