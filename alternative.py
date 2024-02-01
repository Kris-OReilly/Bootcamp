# create a variable to take in a string
# iterate through the string
# create a variable to create an empty string that will store the converted letters
# create a for loop to iterate through each index and letter in the string(sentence) using enumerate()
# using an if-else condition check the index of the string is an even number
# if it is even, change the letter to uppercase and save it in the string(new_sentence)
# if it is odd, copy the letter directly into the string(new_sentence)

sentence = "the quick brown fox jumped over the lazy dog"

new_sentence = ''


for index, letter in enumerate(sentence): 
   
    if index % 2 == 0:
        new_sentence += letter.upper()
    else:
        new_sentence += letter
print(new_sentence)        




# using the split() function, split each word in the string to form a list of each word
# run a for loop to iterate through the range of the length of the list with a step count of 2
# change these words to uppercase in the list
# using .join(), change the list to a new string with a space between each word

split_sentence = sentence.split(' ') 

for word in range(0, len(split_sentence), 2): # iterate through the list of words with a step of 2
    split_sentence[word] = split_sentence[word].upper()
# the loop starts from the first word and loops through every other word and changes them to uppercase
    
alt_sentence = ' '.join(split_sentence) # the new variable alt_sentence saves the joined words as
# a string with a space in between each word

print(alt_sentence)

  

