# Declare the sentence “The!quick!brown!fox!jumps!over!the!lazy!dog.” as a string
# Use the replace() function to change all '!' to blank spaces and save new sentence string.
# Print new sentence.
# Assign the new variable to become the previous sentence in all capitals by using the upper() function.
# Print new variable.
# Assign the new variable to become the previous sentence in reverse using the extended slice [::-1]
# Print the new variable.

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence)

sentence = sentence.replace("!", " ") # Updating sentence variable with new string.
print(sentence)

sentence = sentence.upper()
print(sentence)

sentence = sentence[::-1]
print(sentence)