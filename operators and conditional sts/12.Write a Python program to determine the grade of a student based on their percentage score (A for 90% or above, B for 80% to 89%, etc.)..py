#12.Write a Python program to determine the grade of a student based on their percentage score (A for 90% or above, B for 80% to 89%, etc.).
def determine_grade(percentage):
    if not isinstance(percentage, (int, float)): #Check if it is a number
        return "Invalid input. Percentage must be a number."

    if percentage < 0 or percentage > 100:
        return "Invalid percentage. It must be between 0 and 100."

    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


# Get percentage input from the user
try:
    percentage = float(input("Enter your percentage score: "))
    grade = determine_grade(percentage)
    print("Your grade is:", grade)

except ValueError:
    print("Invalid input. Please enter a number for the percentage.")