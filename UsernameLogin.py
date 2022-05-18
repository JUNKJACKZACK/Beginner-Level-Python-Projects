print('Welcome to the best website in the WWW!')

username = input("Type a good username: ")
password = input("Type a good password: ")

secret = input("What is a secret you want to store in this vault?")

warning = "WARNING ATTEMPT FAILED"

print("Awesome now to access the vault type in your login info: ")


username_attempt = input("Username: ")

if username_attempt == username:
    password_attempt = input("Password: ")
    
elif username_attempt != username:
    print(warning)

if password_attempt == password:
    print(secret)

elif password_attempt != password:
    print(warning)


