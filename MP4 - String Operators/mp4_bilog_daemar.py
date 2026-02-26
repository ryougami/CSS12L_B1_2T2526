# Full name

first = input("Enter your first name:\n").strip().capitalize()
middle = input("Enter your middle name:\n").strip().capitalize()
last = input("Enter your last name:\n").strip().capitalize()

formatted_name = f"{last}, {first} {middle[0]}."

print("Formatted Name:", formatted_name)

# 2nd

sentence = input("Enter a sentence:\n")

characters = len(sentence)
words = len(sentence.split())

vowels = 0
for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1

print("Characters:", characters)
print("Words:", words)
print("Vowels:", vowels)

# 3rd

word = input("Enter a word:\n")

if word == word[::-1]:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")

# 4th

phrase = input("Enter a phrase:\n")

result = phrase.upper()[::-1]

print("Output:", result)

#5th

email = input("Enter your email address:\n")

if email.find("@") != -1 and email.find(".") != -1:
    at_position = email.find("@")
    username = email[:at_position]

    username = username.lower()
    username = username.replace(".", " ")
    username = username.replace("_", " ")

    print("Valid email address!")
    print("Formatted username:", username)
else:
    print("Invalid email address. Please enter a valid email.")
