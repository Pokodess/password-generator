# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 09:57:14 2024

@author: ewanv
"""

import string
import random

# we store all possible characters in lists
s1 = list(string.ascii_lowercase) # a, b, c, etc...
s2 = list(string.ascii_uppercase) # A, B, C, ETC...
s3 = list(string.digits) # 1, 2, 3, etc...
s4 = list(string.punctuation) # special characters.

# Ask user about the length of his password
user_input = input("How many characthers do you want in your password ? ( It should be at least 15 characters long ) :")

# check if the input is correct.

while True:
    try:
        characters_number = int(user_input)
        
        if characters_number < 15:
            print("Your password should be at least 15 characters.")
            user_input = input("Please, Enter your number again: ")
        
        else:
            break
        
    except:
        print("Please, Enter numbers only.")
        user_input = input("How many characters do you want in your password ? : ")

# shuffle all lists of characters.
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# calculate 30% & 20% of number of characters

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

# Generation of password (60% letters and 40% digits and punctuations)
result = []

for elt in range(part1):
    result.append(s1[elt])
    result.append(s2[elt])

for elt in range(part2):
    result.append(s3[elt])
    result.append(s4[elt])

random.shuffle(result)

# return the password

password = "".join(result)
print("Suggested password : ", password)
