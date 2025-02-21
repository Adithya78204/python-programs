#5.Implement a function to check if a given year is a leap year or not.
def check_leap_year(year):
    return year % 4 == 0 and year %  100 != 0 or year % 400 == 0

year = int(input("enter the year:"))
print(check_leap_year(year))

#A year is a leap year if it satisfies the following conditions:
# Divisible by 400 → It is a leap year.
# ✅ Example: 2000, 2400
#
# Divisible by 100 but not by 400 → It is not a leap year.
# ❌ Example: 1700, 1800, 1900, 2100
#
# Divisible by 4 but not by 100 → It is a leap year.
# ✅ Example: 2024, 2028, 2032
#
# Not divisible by 4 → It is not a leap year.
# ❌ Example: 2023, 2025, 2026
