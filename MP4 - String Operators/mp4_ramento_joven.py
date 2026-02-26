#1
def name()
    x = input("Enter your first name: ")
    y = input("Enter your middle name: ")
    z = input("Enter your last name: ")
  
    first = x.strip().capitalize()
    middle = y.stript().capitalize()
    last = z.stript().capitalize()

print(" Full Name: " + first + " " + middle + " " + last)

name()

#2
def pyramid():
    word = input("Enter a word: ")
    number = int(input("Enter a number: "))

    for w in range(1, number + 1):
        print(word * w)

pyramid()

#3
def validate_name():
  name = input("Enter your full name: ")
  
  if len(name) < 3:
    print("Error: Name is too short.")
  else:
    print("Hello, " + name.title())
    print("Your name length is: " + str(len(name)))

validate_name()

#4
def palindrome():
    word = input("Enter a word: ").lower()
    
    reversed_word = word[::-1]
    
    if word == reversed_word:
        print("Yes! It is a palindrome.")
    else:
        print("No! It is not a palindrome.")
      
palindrome()

#5 
def shout():
    
    msg = input("Type something to shout: ")
    
    loud_msg = msg.upper()
    
    print(loud_msg + "!!!")

shout()

#6
def check_email():
    address = input("Enter your email address: ")

    if "@" in address and "." in address:
        print("This looks like a valid email!")
    else:
        print("Invalid email format. Missing @ or dot.")

check_email()

#7
def gmail():

    email = input("Enter your email address: ").lower()

    if "@gmail.com" in email:

        username = email.split("@")[0]
        print("Hello, " + username + "! You are using a Google account.")
    else:
        print("This is not a Gmail address.")

gmail()



