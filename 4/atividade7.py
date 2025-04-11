# Ask for the user's name and age
name = input('What is your name? ').capitalize().strip()
age = input('What is your age? ')

# Check if both name and age are filled in
if name and age:
    print(f'Your name is {name}')
    print('Your name reversed is:', name[::-1])
    
    # Check if the name contains spaces
    if " " in name:
        print('Your name contains spaces')
    else: 
        print('Your name does not contain spaces')
    
    # Count the number of characters in the name
    name_length = len(name)
    print(f'Your name has {name_length} characters!')
    
    # Display the first and last letter of the name
    print('The first letter of your name is:', name[0])
    print('The last letter of your name is:', name[-1])
else:
    print("Sorry, you left some fields empty.")
