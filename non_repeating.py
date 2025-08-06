#Given a string, find the first character that does not repeat 
# anywhere in the string. Return None if all characters repeat.
#Input: "Hello"
#Output: "H"
#Input: "Swiss"
#Output: "w"



def nonrepeating_char(word):
    char_count = {}
    
    for char in word:
    # a loop to go through
    # each character in the string of word put
        if char in char_count:
            char_count[char] += 1
    #this if statement checks if a character
    #in the put word exists in the dictionary
    #if it does, it increments or add the countby 1
        else:
            char_count[char] = 1
    #if it does not exist, it adds the character
    #to the dictionary with a count of 1

    for char in word:
        if char_count[char] == 1:
            return char
    #another loop
    #an if statement that checks if the count of the character is not equal to 1
    #return the character
    #showing that it does not repeat
    #hence first non-repeating character

    return None
  #if a word is given and all characters repeat
  #the return none shows there
  #is no unique char and all are repeated


print(nonrepeating_char("Hello"))  
print(nonrepeating_char("swiss"))  


