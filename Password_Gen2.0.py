import random

final_password = ''
password_with_specialchar = None
special_char = False
error_message = "You have entered an invalid response."
charset1 = 'abcdefghijklmnopqrstuvwxyz123456789'
charset2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
charset3 = '!@#$*-_.'

def print_password():
    print('\n******************\n')
    print("Here is your super random secret password: " + final_password)
    print('\n******************\n')
password_length = input("\n\nHow long would you like your password to be?\nChoose between 1 & 50 characters long:\n")
if int(password_length) > 50:
    print(error_message)
if int(password_length) < 1:
    print(error_message)
final_length = password_length

password_specialchar = input("Would you like to add special characters for more randomness? Y/N\n")
if password_specialchar is 'Y':
    special_char = True
elif password_specialchar is 'N':
    special_char = False
else:
    print(error_message, "You need to respond using Y or N.")
    quit()
if special_char == False:
    for _ in range(int(password_length)):
        final_password += random.choice(charset1 + charset2)
        if password_length == str(len(final_password)):
            print_password()
    quit()

if special_char == True:
     for _ in range(int(password_length)):
            final_password += random.choice(charset1 + charset2 + charset3)
            if password_length == str(len(final_password)):
                print_password()
                
quit()      

