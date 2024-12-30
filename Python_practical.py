import math

# # 1. WAP to find the roots of a quadratic equation
# def find_roots(a, b, c):
#     if a == 0:
#         print("Coefficient 'a' cannot be zero for a quadratic equation.")
#         return None
    
#     # Calculate the discriminant
#     d = b**2 - 4*a*c

#     if d > 0:
#         # Two distinct real roots
#         root1 = (-b + math.sqrt(d)) / (2 * a)
#         root2 = (-b - math.sqrt(d)) / (2 * a)
#         print(f"The equation has two real roots: {root1} and {root2}")
#     elif d == 0:
#         # One real root
#         root = -b / (2 * a)
#         print(f"The equation has one real root: {root}")

# # Input coefficients
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))

# # Call the function
# find_roots(a, b, c)

# --------------------------------------------------------


# # 2. WAP to accept a number ‘n’ and
# # j. Check if ’n’is prime
# # k. Generate all prime numbers till ‘n’
# # l. Generate first ‘n’ prime numbers This program may be done using functions
# def is_prime(n):
#     # Check if a number is prime
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def primes_up_to_n(n):
#     #Define empty list to store prime numbers
#     primes = []
#     for num in range(2, n + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes

# def first_n_primes(n):
#     #define empty list to store first n prime numbers
#     primes = []
#     num = 2  # Start checking for primes from 2
#     while len(primes) < n:
#         if is_prime(num):
#             primes.append(num)
#         num += 1
#     return primes

# def main():
#     # Accept user input
#     n = int(input("Enter a number 'n': "))
    
#     # Check if 'n' is prime
#     if is_prime(n):
#         print(f"{n} is a prime number.")
#     else:
#         print(f"{n} is not a prime number.")
    
#     # generate all prime numbers up to n
#     all_primes = primes_up_to_n(n)
#     print(f"All prime numbers up to {n}: {all_primes}")
    
#     # generate the first 'n' prime numbers
#     first_n = first_n_primes(n)
#     print(f"The first {n} prime numbers: {first_n}")

# main()


# ------------------------------------------------------

## WAP to create a pyramid of the character ‘*’ and a reverse pyramid
# def print_pyramid(rows):
#     # for lop for printing pyramid 
#     for i in range(rows):
#         print(' ' * (rows - i - 1), end='')
#         print('* ' * (i + 1))

# def print_reverse_pyramid(rows):
#     # printing reverse pyramid 
#     for i in range(rows, 0, -1):
#         print(' ' * (rows - i), end='')
#         print('* ' * i)

# def main():
#     # Accept user input for number of rows
#     rows = int(input("Enter the number of rows for the pyramids: "))
    
#     print_pyramid(rows)
#     print("")
#     print_reverse_pyramid(rows)

# main()

# -------------------------------------------------------

## WAP that accepts a character and performs the following:
## a. print whether the character is a letter or numeric digit or a special character
## b. if the character is a letter, print whether the letter is uppercase or lowercase
## c. if the character is a numeric digit, prints its name in text (e.g., if input is 9,
## output is NINE)
# def character_analysis(ch):
#     #Analyze the character and perform the required tasks
#     if ch.isalpha():
#         print(f"'{ch}' is a letter.")
#         if ch.isupper():
#             print("It is an uppercase letter.")
#         else:
#             print("It is a lowercase letter.")
#     elif ch.isdigit():
#         print(f"'{ch}' is a numeric digit.")
#         digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
#         print(f"Its name in text is {digit_names[int(ch)]}.")
#     else:
#         print(f"'{ch}' is a special character.")


# ch = input("Enter a single character: ")
# if len(ch) == 1:
#     character_analysis(ch)

# --------------------------------------------------------

# WAP to perform the following operations on a string
# a. Find the frequency of a character in a string.
# b. Replace a character by another character in a string.
# c. Remove the first occurrence of a character from a string.
# d. Remove all occurrences of a character from a string.

# def character_frequency(s, char):
#     #find the frequency of a character in a string
#     print(s.count(char))

# def replace_character(s, old_char, new_char):
#     #Replace a character by another character in a string
#     print(s.replace(old_char, new_char))

# def remove_first_occurrence(s, char):
#     #remove the first occurrence of a character from a string
#     print(s.replace(char, '', 1)) 

# def remove_all_occurrences(s, char):
#     #Remove all occurrences of a character from a string
#     print(s.replace(char, ''))

# character_frequency('sushant', "s")
# replace_character('my name is sushant bhagat', 'bhagat', 'kumar')
# remove_first_occurrence('i am 18 years old','18')
# remove_all_occurrences('what is your name, is your name is sushant', 'is')

# -------------------------------------------------------

# WAP to swap the first n characters of two strings.

# def swap_first_n_characters(str1, str2, n):
#     if n > len(str1) or n > len(str2):
#         return "n is larger than the length of one or both strings."
    
#     swapped_str1 = str2[:n] + str1[n:]
#     swapped_str2 = str1[:n] + str2[n:]

#     return swapped_str1, swapped_str2

# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# n = int(input("Enter the number of characters to swap: "))

# result = swap_first_n_characters(string1, string2, n)

# if isinstance(result, str):
#     print(result)
# else:
#     swapped_string1, swapped_string2 = result
#     print(f"after swapping first {n} characters:")
#     print(f"first string: {swapped_string1}")
#     print(f"Second string: {swapped_string2}")


# -------------------------------------------------------

#Write a function that accepts two strings and returns the indices of all the occurrences
# of the second string in the first string as a list. If the second string is not present in the
# first string then it should return -1.

# def myFunc(main_str, sub_str):
#     indices = []
#     start = 0

#     while True:
#         start = main_str.find(sub_str, start)
#         if start == -1:
#             break
#         indices.append(start)
#         start += 1  # Move past the current match to find subsequent ones

#     return indices if indices else -1

# main_string = input("Enter the main string: ")
# substring = input("Enter the substring to search for: ")

# result = myFunc(main_string, substring)

# if result == -1:
#     print("The substring was not found in the main string.")
# else:
#     print(f"The substring was found at indices: {result}")

# ----------------------------------------------------------------------

# WAP to create a list of the cubes of only the even integers appearing in the input list
# (may have elements of other types also) using the following:
# a. 'for' loop
# b. list comprehension

# def cubes_int(l):
#     result = []
#     for element in l:
#         if isinstance(element, int) and element % 2 == 0:
#             result.append(element ** 3)
#     return result

# def cubes_comp(l):
#     return [element ** 3 for element in l if isinstance(element, int) and element % 2 == 0]

# l = [1, 2, 'a', 3.5, 4, 5, 6, 'b']
# print("Cubes of even integers using 'for' loop:", cubes_int(l))
# print("Cubes of even integers using list comprehension:", cubes_comp(l))

# -------------------------------------------------------

# # read the file
# file = open("txt_file.txt", "r")

# # Read all lines from the file
# lines = file.readlines()

# # Count total characters, words, and lines
# num_lines = len(lines)
# num_words = sum(len(line.split()) for line in lines)
# num_characters = sum(len(line) for line in lines)

# # Print the results
# print(f"Total characters: {num_characters}")
# print(f"Total words: {num_words}")
# print(f"Total lines: {num_lines}")
# file.close()

# # read the file
# file = open("txt_file.txt", "r")

# # Read all lines from the file
# lines = file.readlines()

# # Calculate the frequency of each character 
# char_frequency = {}
# for line in lines:
#     for char in line:
#         if char in char_frequency:
#             char_frequency[char] += 1
#         else:
#             char_frequency[char] = 1

# # Print character frequencies
# print("Character frequencies:")
# for char, count in char_frequency.items():
#     print(f"'{char}': {count}")

# # Close the file
# file.close()


# file = open("txt_file.txt", "r") # read the file
# lines = file.readlines()
# # Print words in reverse order
# print("Words in reverse order:")
# for line in lines:
#     words = line.split()
#     reversed_words = " ".join(words[::-1])
#     print(reversed_words)
# # Close the file
# file.close()

# # read the file
# file = open("txt_file.txt", "r")
# # Read all lines from the file
# lines = file.readlines()
# # Copy even and odd lines to separate files
# with open("File1.txt", "w") as file1, open("File2.txt", "w") as file2:
#     for i, line in enumerate(lines):
#         if (i + 1) % 2 == 0:
#             file1.write(line)
#         else:
#             file2.write(line)
# # Close the original file
# file.close()

# ---------------------------------------------------------

# import math
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point(x={self.x}, y={self.y})"

#     def distance(self, other):
#         # calculate distance
#         return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# # Create two points
# point1 = Point(3, 4)
# point2 = Point(7, 1)

# # Print the points
# print("Point 1:", point1)
# print("Point 2:", point2)

# # Calculate and print the distance between the points
# dist = point1.distance(point2)
# print(f"Distance between {point1} and {point2}: {dist:.2f}")


# ----------------------------------------------------------------

# Function to print a dictionary with keys as numbers (1 to 5) and values as their cubes
# def print_cubes_dict():
#     cubes_dict = {x: x ** 3 for x in range(1, 6)}
#     print("Dictionary of cubes:", cubes_dict)
# print_cubes_dict()

# Tuple operations
# def tuple_operations():
#     t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

#     # a. Print half the values of the tuple in one line and the other half in the next line
#     half = len(t1) // 2
#     print("First half:", t1[:half])
#     print("Second half:", t1[half:])

#     # b. Print another tuple whose values are even numbers in the given tuple
#     even_tuple = tuple(x for x in t1 if x % 2 == 0)
#     print("Tuple with even numbers:", even_tuple)

#     # c. Concatenate a tuple t2=(11,13,15) with t1
#     t2 = (11, 13, 15)
#     concatenated_tuple = t1 + t2
#     print("Concatenated tuple:", concatenated_tuple)

#     # d. Return maximum and minimum value from this tuple
#     max_value = max(concatenated_tuple)
#     min_value = min(concatenated_tuple)
#     print(f"Maximum value: {max_value}, Minimum value: {min_value}")
# tuple_operations()

# ------------------------------------------------------------------

# def get_name():
#     name = input("Enter your name: ")

#     # Check if the name contains digits or special characters
#     if not name.isalpha():  # checks for anything other than alphabets
#         raise ValueError("Name should only contain alphabets. No digits or special characters allowed.")
    
#     return name

# # Main program execution
# try:
#     name = get_name()
#     print(f"Hello, {name}!")
# except ValueError as e:
#     print(f"Error: {e}")
