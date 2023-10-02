actual_word = input("Enter the actual word that user wants to guess:")
actual_word = list(actual_word.upper())
while(len(actual_word)!=5):
    actual_word = list(input("Enter the actual word that user wants to guess:"))
print(actual_word)

# keyboard = 

# Create a dictionary with all letters as keys and 'W' as the value
letter_dict = {chr(letter): 'W' for letter in range(ord('A'), ord('Z') + 1)}

# Include uppercase letters as well
# letter_dict.update({chr(letter): 'W' for letter in range(ord('A'), ord('Z') + 1)})

# Print the dictionary
print(letter_dict)

tried_words =[]
color_codes = []
for i in range(6): #Number of tries
    guess_word = input(f"Enter the users guess {i} :")
    guess_word = guess_word.upper()

    while(len(guess_word)!=5):
        guess_word = input(f"Enter the users guess {i} :")

    tried_words.append(guess_word)

    color = ['W' for i in range(5)]    # List that will maintain the color of each guessed word 'Y','B','G' 

    # eliminator = guess_word.copy() #To avoid duplicate letters in 

    # for x in guess_word:
    #     if x in actual_word:
    #         if actual_word[guess_word.index(x)] == x:
    #             color[guess_word.index(x)] = 'G'
    #         else:
    #             color[guess_word.index(x)] = 'Y'

    #     else:
    #         #assign black color to that letter and white in the keyboard
    #         color[guess_word.index(x)] = 'B'
            
    for i in range(5):
        if guess_word[i] in actual_word:
            if guess_word[i] == actual_word[i]:
                color[i] = 'G'
                letter_dict[guess_word[i]] = 'G'
            else:
                color[i] = 'Y'
                if(letter_dict[guess_word[i]] != 'G' ):
                    letter_dict[guess_word[i]] = 'Y'    
        else:
            #assign black color to that letter and white in the keyboard
            color[i] = 'B'
            if(letter_dict[guess_word[i]] != 'G' and letter_dict[guess_word[i]] != 'Y'):
                letter_dict[guess_word[i]] = 'B'


    print(letter_dict)
    # print(color)
            
    
print(tried_words)
