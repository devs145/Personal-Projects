import random 

# The range is determined by the user first prompt user for the starting value and ending value
starting_val = int(input("Enter the value you would like to start the range from: "))
ending_val = int(input("Enter the end value for the range: "))

# Generate a random int within the given range by the user
random_number = random.randint(starting_val, ending_val)

# print the random number within the range specified by the user
print(f"The random number generated between {starting_val} and {ending_val} is: {random_number}")

# We will prompt the user if they want an even or odd number
while True:
    even_or_odd = input("Do you want an even or odd number? (even/odd): ").lower()
    if even_or_odd in ['even', 'odd']:
        break
    print("Invalid input. Please enter 'even' or 'odd'.")
    
# Generate a random even or odd integer within the specified range
if even_or_odd == 'even':
    num = range(starting_val + (starting_val % 2), ending_val + 1, 2) 
elif even_or_odd == 'odd':
    num = range(starting_val + (starting_val % 2) + 1, ending_val + 1, 2) 
else:
    print("Invalid input.")
    
# Print the even or odd number in the given range
if num:
    random_number = random.choice(list(num))
    print(f"Random {even_or_odd} number between {starting_val} and {ending_val}: {random_number}")
