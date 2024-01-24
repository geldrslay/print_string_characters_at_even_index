# Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# Accept string input from the user.
string_input = input ("Please enter a word: ")
print ("The original string is",string_input)

# Determine length of the string
string_length = len (string_input)

# Display string characters in even index
print ("Only printing the characters in even index of the string...")

# Iterate each string character. 
# To start with the first character of the string, start = 0
# To stop at the last character of the string, stop = length of the string
# To get the characters at the even index, step = 2

for i in range (0, len(string_input), 2):
    # Print the characters at even index
    print (string_input[i])


