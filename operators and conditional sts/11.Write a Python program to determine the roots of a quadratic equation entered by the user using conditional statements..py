#11.

def check_voting_eligibility(age):
    if age >= 18:
        return True
    else:
        return False
try:
    age = int(input("Enter your age: "))

    if age < 0: #Added to handle negative age input
        print("Age cannot be negative.")
    else:
        is_eligible = check_voting_eligibility(age)

        if is_eligible:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
except ValueError:
    print("Invalid input. Please enter a whole number for age.")
