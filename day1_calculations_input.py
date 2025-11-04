# Day 1 - Part 3: Basic Calculations and User Input

# 1. Ask for user input
name = input("What is your name? ")
age = int(input("How old are you? "))

# 2. Do a simple calculation
current_year = 2025
year_of_birth = current_year - age

# 3. Ask for another numeric input
monthly_salary = float(input("Enter your monthly salary in dollars: "))
annual_salary = monthly_salary * 12

# 4. Show the results
print("\n--- Summary ---")
print("Hello,", name + "!")
print("You were born in", year_of_birth)
print("Your estimated annual salary is $", annual_salary)
