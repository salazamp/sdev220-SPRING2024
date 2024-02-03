# 7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]
things
['mozzarella', 'cinderella', 'salmonella']
# 7.5 Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
things = ["mozzarella", "cinderella", "salmonella"]

# Capitalize the element that refers to a person
things[1] = things[1].capitalize()

# Print the updated list
print(things)
['mozzarella', 'Cinderella', 'salmonella']
# 7.6 Make the cheesy element of things all uppercase and then print the list.
things = ["mozzarella", "cinderella", "salmonella"]

# Make the "cheesy" element all uppercase
things[0] = things[0].upper()

# Print the updated list
print(things)
['MOZZARELLA', 'cinderella', 'salmonella']
# 7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.
things = ["mozzarella", "cinderella", "salmonella"]

# Delete the "disease" element
things.remove("salmonella")

# Print the updated list
print(things)
['mozzarella', 'cinderella']
# 9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
def good():
    return ['Harry', 'Ron', 'Hermione']

# Call the function to get the list
good_list = good()

# Print the list
print(good_list)
['Harry', 'Ron', 'Hermione']
# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
def get_odds():
    for number in range(1, 10, 2):
        yield number

# Create a generator object
odd_generator = get_odds()

# Use a for loop to find and print the third value
count = 0
for odd in odd_generator:
    count += 1
    if count == 3:
        print("The third odd number is:", odd)
        break
The third odd number is: 5