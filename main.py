# Check if a word is an anagrams    
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True



def welcome():
    print('Welcome to the Anagram Match Finder')
def find_anagrams():
    # [assignment] Add your code here
    first_input = input('Enter first choice word:- ')
    second_input = input('Enter second choice word:- ')
    if first_input.isnumeric():
        print(False)
    elif second_input.isnumeric():
        print(False)
    elif sorted(first_input.replace(' ','').lower()) == sorted(second_input.replace(' ','').lower()):
        print(True)
        print(first_input.upper() +' and '+second_input.upper() +' are anagrams!')
    elif sorted(first_input.lower()) == sorted(second_input.lower()):
        print(True)
        print(first_input.upper() +' and '+second_input.upper() +' are anagrams!')
    else:
        print(False)
    again()
def again():
    run_again = input('''
Do you want to run again?
Please type Y for YES or N for NO.
''')

    if run_again.upper() == 'Y':
        find_anagrams()
    elif run_again.upper() == 'N':
        print('See you later.')
    else:
        again()
welcome()
find_anagrams()