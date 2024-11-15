"""
Week 4: Numpy
"""

import os
import sys
import hashlib
import binascii
import random
import string
import re
import numpy as np
MAIN_MENU_QUESTION = "null"
phone_regex = re.compile(r"(\d{3}-\d{3}-\d{4})")
zip_code_regex = re.compile(r"\d{5}-\d{4}")

def my_quit():
    """This will Quit"""
    print("Thank you for utilizing the Python Matrix application!")
    sys.exit()

def validator(x_x):
    """Prompts user to validate their input"""
    valid_input = False
    while valid_input is not True:
        print("Is the following input correct:" , x_x.upper() , "\tYes or No?")
        validator_correctness = input()
        if validator_correctness.upper() == "YES":
            print("Thank you for confirming")
            return True
        if validator_correctness.upper() == "NO":
            print("Understood, reprompting...")
            return False
        if validator_correctness.upper() == "QUIT":
            print("Are you sure you'd like to Quit?")
            quit_check = input()
            if quit_check.upper() == "YES":
                print("Goodbye")
                sys.exit()
            elif quit_check.upper() == "NO":
                print("Returning Back")
                break
            else:
                print("Please Enter 'Yes' or 'No'")
        else:
            print("Please Enter 'Yes' or 'No'")

def get_numeric_row(prompt):
    """Creating our array"""
    row = []
    while all(entry.isnumeric() for entry in row) is not True or len(row) != 3:
        print(prompt)
        row_input = input()
        row = row_input.split()
    return np.array(row).astype(float)

def display_results(matrix_things):
    """Displaying the results"""
    print("Your Result Matrix is:\n", matrix_things)
    print("The transpose is:\n" , matrix_things.transpose())
    print("The mean of each row is:" , np.mean(matrix_things[0]), "," ,
    np.mean(matrix_things[1]), "," , np.mean(matrix_things[2]))
    print("The mean of each column is:" , np.mean(matrix_things[:,0]) , "," ,
    np.mean(matrix_things[:,1]) , "," , np.mean(matrix_things[:,2]))

def original_matricies(matricie_one, matricie_two):
    """Reprinting original matrixes"""
    print("Your first 3x3 matrix is:\n", matricie_one)
    print("Your second 3x3 matris is:\n", matricie_two)

def matrix_game():
    """Used to validate zipcode and phone number"""
    continue_option = False
    user_phone_number = ""
    user_zip_code = ""
    user_matrix_one = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    user_matrix_two = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    while re.match(phone_regex, user_phone_number) is None:
        print("Enter your phone number (XXX-XXX-XXXX):")
        user_phone_number = input()
        validator(user_phone_number)
    print("Your Phone Number is:" , user_phone_number)
    while re.match(zip_code_regex, user_zip_code) is None:
        print("Enter your Zip Code and Postal Code (XXXXX-XXXX):")
        user_zip_code = input()
        validator(user_zip_code)
    print("Your Zip Code and Postal Code is:" , user_zip_code)
    first_first_row = get_numeric_row(
        "Enter the first row of your first 3x3 matrix, separating each number with a space:")
    first_second_row = get_numeric_row(
        "Enter the second row of your first 3x3 matrix, separating each number with a space:")
    first_third_row = get_numeric_row(
        "Enter the third row of your first 3x3 matrix, separating each number with a space:")
    user_matrix_one = np.array([first_first_row, first_second_row,
    first_third_row])
    print("Your first 3x3 matrix is:")
    print(user_matrix_one)
    second_first_row = get_numeric_row(
        "Enter the first row of your second 3x3 matrix, separating each number with a space:")
    second_second_row = get_numeric_row(
        "Enter the second row of your second 3x3 matrix, separating each number with a space:")
    second_third_row = get_numeric_row(
        "Enter the third row of your second 3x3 matrix, separating each number with a space:")
    user_matrix_two = np.array([second_first_row,
    second_second_row, second_third_row])
    print("Your second 3x3 matrix is:")
    print(user_matrix_two)
    while continue_option is not True:
        print("Select a Matrix Operation from the list below:")
        print("a. Addition")
        print("b. Subtraction")
        print("c. Matrix Multiplication")
        print("d. Element by element multiplication")
        menu_option = input()
        if menu_option.upper() == 'A':
            validator(menu_option)
            print("You have selected Addition")
            matrix_addition = user_matrix_one + user_matrix_two
            original_matricies(user_matrix_one, user_matrix_two)
            display_results(matrix_addition)
        elif menu_option.upper() == 'B':
            validator(menu_option)
            print("You have selected Subtraction")
            matrix_subtraction = user_matrix_one - user_matrix_two
            original_matricies(user_matrix_one, user_matrix_two)
            display_results(matrix_subtraction)
        elif menu_option.upper() == 'C':
            validator(menu_option)
            print("You have selected Multiplication")
            matrix_multiplication = np.matmul(user_matrix_one,
            user_matrix_two)
            original_matricies(user_matrix_one, user_matrix_two)
            display_results(matrix_multiplication)
        elif menu_option.upper() == 'D':
            validator(menu_option)
            print("You have selected Element Multiplication")
            matrix_element_multiplication = np.multiply(user_matrix_one,
            user_matrix_two)
            original_matricies(user_matrix_one, user_matrix_two)
            display_results(matrix_element_multiplication)
        elif menu_option.upper() == 'QUIT':
            validator(menu_option)
            continue_option = True
        else:
            print("Invalid Input, Please select 'A' 'B' 'C' 'D' or 'QUIT'")

def password_hasher():
    """Used to give a password hash"""
    print("Go again?")
    go_again = input()
    while go_again.upper() != "NO":
        print("Go again?")
        go_again = input()
        if go_again.upper() == "YES":
            print("Enter a password to encode:")
            password = input()
            salt = os.urandom(32)
            print("Enter a salt to use:")
            user_salt = input()
            random_password_length = random.randint(32, 64)
            characters_chosen = [string.ascii_uppercase, string.ascii_lowercase,
            string.digits, string.punctuation]
            temp_password = ""
            for random_password_length in range(0, int(random_password_length)):
                temp_password += random.choice(random.choice(characters_chosen))
            final_password =  "".join(temp_password)
            hashed_password = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
            user_hashed_password = hashlib.pbkdf2_hmac('sha256', b'password', b'user_salt', 100000)
            true_random_password = hashlib.pbkdf2_hmac('sha256', b'final_password', b'salt', 100000)
            password = password.encode('utf-8')
            print("MD5 Hash of:" , password , "is:" , hashlib.md5(password).hexdigest())
            print("SHA256 Hash of:" , password , "is:", hashlib.sha256(password).hexdigest())
            print("SHA512 Hash of:" , password, "is:" , hashlib.sha512(password).hexdigest())
            print("Random Salted SHA256 Hash of:" , password, "with a random salt of:" ,
            binascii.hexlify(salt) , "is:" , binascii.hexlify(hashed_password))
            print("User Salted SHA256 Hash of:" , password, "with a given salt of:" ,
            user_salt , "is:" , binascii.hexlify(user_hashed_password))
            print("True Random Salted SHA256 Hash of:" , final_password, "with a random salt of:" ,
            binascii.hexlify(salt) , "is:" , binascii.hexlify(true_random_password))
        elif go_again.upper() == "NO":
            print("okay")
            break
        else:
            print("Bad input yo")

print("******************************")
print("Welcome to the Python Matrix Application!")

while MAIN_MENU_QUESTION.upper() != "N":
    print("Would you like to play the Matrix Game?")
    print("Enter Y for Yes or N for No:")
    MAIN_MENU_QUESTION = input()
    if MAIN_MENU_QUESTION.upper() == "Y":
        validator(MAIN_MENU_QUESTION)
        matrix_game()
    elif MAIN_MENU_QUESTION.upper() == "N":
        validator(MAIN_MENU_QUESTION)
        my_quit()
    elif MAIN_MENU_QUESTION.upper() == "PASSWORD":
        validator(MAIN_MENU_QUESTION)
        password_hasher()
    else:
        print("***Invalid Input***")
        print("Please Enter 'Y', or 'N'\t")
