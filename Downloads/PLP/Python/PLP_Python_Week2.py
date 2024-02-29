'''
Task 1
Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
'''
#num_1 = (int(input("Enter first number you want to add: ", )))
#num_2 = (int(input("Enter second number you want to add: ", )))
#num_3 = (int(input("Enter third number you want to add: ", )))

#sum_num = int((num_1 + num_2 + num_3))
#print(sum_num)


'''
Task 2
Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
'''
#fav_books = ('5 AM Club - Robin Sharma', 'Start With Why - Simon Sinek', 'Tough Times Never Last, Tough People Do - Robert H. Schuller', 'The Monk Who Sold His Ferrari - Robin Sharma', 'The Alchemist - Paulo Coelho')
#for books in fav_books:
    #print(books)

'''
Task 3
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
'''

#name = input('What is your name: ', )
#age = input('How old are you: ', )
#colour = input('What is your favourite colour: ', )
#job = input('What is your job: ', )

#personal_info = {'name': name, 'age': age, 'colour': colour, 'job':job}
#print(personal_info)

#print(personal_info['colour'])
#print(personal_info['age'])
#print(personal_info['name'])
#print(personal_info['job'])


'''
Task 4
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
'''
set_1 = set()
set_2 = set()

runs = int(input("How many numbers would you like to add?: "))
for i in range(runs):
    user_input = int(input("Add a number: "))
    # Randomly assign the number to set_1 or set_2
    if i % 2 == 0:
        set_1.add(user_input)
    else:
        set_2.add(user_input)

print("Set 1:", set_1)
print("Set 2:", set_2)

# Find common elements between the two sets using membership testing
common_elements = {elem for elem in set_1 if elem in set_2}

print("Common elements:", common_elements)

'''
Task 5
Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
'''

# Initiate with an empty list to store words
#word_list = []

# Prompt the user to input words
#num_words = int(input("How many words do you want to add? "))
#for _ in range(num_words):
    #word = input("Enter a word: ")
    #word_list.append(word)

# Use list comprehension to filter words with odd number of characters
#odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Print the list of words with odd number of characters
#print("Word list with words containing an odd number of characters:", odd_length_words)


'''
The range() function in Python generates a sequence of numbers. It's commonly used in conjunction with loops to iterate over a specific range of numbers. Here's how it works:

Syntax: The range() function can take one, two, or three arguments.

With one argument: range(stop): Generates numbers from 0 up to (but not including) the stop value.
With two arguments: range(start, stop): Generates numbers from start up to (but not including) the stop value.
With three arguments: range(start, stop, step): Generates numbers from start up to (but not including) the stop value, incrementing by step.
Usage in loops: You can use range() to specify the number of iterations for a loop.

# Example 1: range(stop)
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Example 2: range(start, stop)
for i in range(2, 6):
    print(i)
# Output: 2, 3, 4, 5

# Example 3: range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
# Output: 1, 3, 5, 7, 9

'''