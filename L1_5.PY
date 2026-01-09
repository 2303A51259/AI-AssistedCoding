#TASK1
#write a python program for string reversal without functions
string=input("Enter a string: ")
reversed_string=""
for char in string:
    reversed_string=char+reversed_string
print("Reversed string:",reversed_string)
#TASK2
#simplify this code and improve readability
string = input("Enter a string: ")
reversed_string = ""
for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]
print("Reversed string:", reversed_string)
#TASK3
#Generate a function-based Python program that:
# Uses a user-defined function to reverse a string
#Returns the reversed string
#Includes meaningful comments (AI-assisted)
def reverse_string(input_string):
    reversed_string = ""
    # Iterate through the input string in reverse order
    for char in input_string[::-1]:
        reversed_string += char
    return reversed_string
# Get user input
user_input = input("Enter a string to reverse: ")
# Call the function and display the result
result = reverse_string(user_input)
print("Reversed string:", result)
#TASK5
# Generate two different methods to reverse a string in Python:
# A loop-based string reversal approach
# A built-in / slicing-based string reversal approach
def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
def reverse_string_slicing(s):
    return s[::-1]
s=input("Enter a string to reverse: ")
print("Reversed string using loop method:", reverse_string_loop(s))
print("Reversed string using slicing method:", reverse_string_slicing(s))
