"""A collection of all my functions for doing my Mad Libs project."""


# This imports string module that contains useful string constants 
import string


# Global variable that can be accessed inside or outside of the function
# Variable 'key' increments the encoding by the value stored in 'key', which is 150
key = 150


def password_encryption(password):
    """The password_encryption function encrypts any given string-based password and generates an encrypted
    version of the password (input from user).
    
    Parameters
    ----------
    password : string
        Input received from user
 
    Returns
    -------
    encrypted : string 
        An encrypted version of the password based on user input 
    """
    
    
    # Initialize a variable called 'encrypted' as an empty string 
    encrypted = ""
    
    # Encrypting each character by changing the unicode code point, converting the new int
    # back to a character, and adding this converted character to the string 'encrypted' 
    # This encryption concept was adapated from Assignment 2: Ciphers 
    for char in password:
        new_number = ord(char) + key
        encrypted = encrypted + chr(new_number)
        
    # Returning the final encrypted version of password 
    return encrypted


def end_game(user_input):
    """The end_game function allows the user to end the game of Mad Libs. The function will end the game if
    the word 'quit' appears. 
    
    Parameters
    ----------
    user_input : string
        Input received from user
 
    Returns
    -------
    output : boolean 
        The end_game function should return True if the string 'quit' is in user_input, and return False otherwise 
    """
    
    
    # If statement used to return True if user_input is the string 'quit', and return False otherwise.
    # This end game concept was adapted from Assignment 3: Chatbots 
    if user_input == "quit":
        return True
    else:
        return False

    
def mad_libs():
    """The mad_libs function plays the game of Mad Libs with the user. The function asks the user to input a string of
    adjectives, nouns, colors, verb, number, and stores the strings as lists to create a Mad Libs story based on user input. The
    function checks for the length of user input and checks that the provided input is the correct type by using .isdigit()
    function. An error message is provided if user input is not recognized to provide help for the user so that a Mad Libs story
    can be properly generated.  
    """
    
    
    print("Welcome to the game of Mad Libs!")
    
    # Using while True loop to ask users to provide 3 adjectives that describe themselves   
    while True:
        adjective_input = input("How would you describe yourself using 3 words? Separate each word by a comma. \n \t")
        
        # Check if user input is the string 'quit' to end the game 
        if end_game(adjective_input):
            print("Thank you for playing the game! See you next time!")
            return None
        
        # Prepare the user input for processing by calling prepare_word function, which splits the string into words
        # This preparing word concept was adapated from Assignment 3: Chatbots 
        adjective_input = prepare_word(adjective_input) 
        
        # Check if the length of user input list is 3. If True, break out from while loop. If False, error message provided.
        if len(adjective_input) == 3:
            break
        else:
            print("Input not recognized. Try again.")
    
    # Using while True loop to ask users to provide 3 favorite colors   
    while True:
        color_input = input("What are your top 3 favorite colors? Separate each word by a comma. \n \t")
        
        # Check if user input is the string 'quit' to end the game 
        if end_game(color_input):
            print("Thank you for playing the game! See you next time!")
            return None
        
        # Prepare the user input for processing by calling prepare_word function, which splits the string into words
        color_input = prepare_word(color_input)
        
        # Check if the length of user input list is 3. If True, break out from while loop. If False, error message provided.
        if len(color_input) == 3:
            break
        else:
            print("Input not recognized. Try again.")
    
    # Using while True loop to ask users to provide 1 body part    
    while True:
        body_input = input("Name a body part. \n \t")

        # Check if user input is the string 'quit' to end the game 
        if end_game(body_input):
            print("Thank you for playing the game! See you next time!")
            return None 
        
        # Prepare the user input for processing by calling prepare_word function, which splits the string into words  
        body_input = prepare_word(body_input)
    
        # Check if the length of user input list is 1. If True, break out from while loop. If False, error message provided.
        if len(body_input) == 1:
            break
        else:
            print("Input not recognized. Try again.")
    
    # Using while True loop to ask users to provide 4 items on what they want for Christmas (nouns)     
    while True: 
        noun_input = input("What do you want for Christmas this year? List out 4 items. Separate each word by a comma. \n \t")
        
        # Check if user input is the string 'quit' to end the game 
        if end_game(noun_input):
            print("Thank you for playing the game! See you next time!")
            return None
        
        # Prepare the user input for processing by calling prepare_word function, which splits the string into words  
        noun_input = prepare_word(noun_input)
        
        # Check if the length of user input list is 4. If True, break out from while loop. If False, error message provided.
        if len(noun_input) == 4:
            break
        else:
            print("Input not recognized. Try again.")
  
    # Using while True loop to ask users to provide 1 favorite number     
    while True:
        number_input = input("What is your favorite number? \n \t") 
        
        # Check if user input is the string 'quit' to end the game 
        if end_game(number_input):
            print("Thank you for playing the game! See you next time!")
            return None
        
        # Prepare the user input for processing by calling prepare_word function, which splits the string into words  
        number_input = prepare_word(number_input)
        
        # Check if the length of user input list is 1 and check if user input only consists of digits. If True, break out from  
        # while loop. If False, error message provided.
        if len(number_input) == 1 and number_input[0].isdigit():
            break
        else:
            print("Input not recognized. Try again.") 
            
    # Using while True loop to ask users to provide 1 favorite animal          
    while True:
        animal_input = input("What is your favorite animal? \n \t")
        
        # Check if user input is the string 'quit' to end the game 
        if end_game(animal_input):
            print("Thank you for playing the game! See you next time!")
            return None
        
        # Prepare the user input for processing by calling prepare_word function, which splits the string into words  
        animal_input = prepare_word(animal_input)
        
        # Check if the length of user input list is 1. If True, break out from while loop. If False, error message provided.
        if len(animal_input) == 1:
            break
        else:
            print("Input not recognized. Try again.")
            
    # Using while True loop to ask users to provide 1 favorite hobby (verb)           
    while True: 
        verb_input = input("What is your favorite hobby? \n \t")
        
        # Check if user input is the string 'quit' to end the game 
        if end_game(verb_input):
            print("Thank you for playing the game! See you next time!")
            return None
        
        # Prepare the user input for processing by calling prepare_word function, which splits the string into words  
        verb_input = prepare_word(verb_input)
        
        # Check if the length of user input list is 1. If True, break out from while loop. If False, error message provided.
        if len(verb_input) == 1:
            break
        else:
            print("Input not recognized. Try again.")

    # Generates a Mad Libs story based on user input 
    print("Santa Claus is a " + adjective_input[0] +
          " man who wears a " + color_input[0] + " suit with a " +
          color_input[1] + " belt and a " + adjective_input[1] +
          " " + color_input[2] + " hat. \n He has a long "+ adjective_input[2] +
          " beard and his " + body_input[0] + " shakes like jelly when he laughs. \n Every Christmas, he rides a " +
          noun_input[0] + " full of presents, pulled by " + number_input[0] + " " + animal_input[0] + "s" +
          " high into the night sky. \n Santa is " + verb_input[0] + " down the chimney of people's homes to leave " +
          noun_input[1] + ", " + noun_input[2] + ", and " + noun_input[3] + " under their Christmas trees.")

     
def chat_generator():
    """The chat_generator is my main function that enables users to input username and password of their choice to begin the game
    of Mad Libs. The function checks if the length of string username is within the boundaries of 5 to 10 character limit, and
    checks if the previosuly encrypted password matches with the copied password based on user's input. The function will finally
    call the mad_libs() function to play the Mad Libs game, and allow the user to replay the game by calling the replay_game()
    function. This function is inside my_script python file.  
    """
    
    
    # Using while True loop to ask users to provide a username of their choice. Checks if username is 5-10 character.           
    while True: 
        username = input("Please provide your username with a 5-10 character limit to unlock the game of Mad Libs. \n \t")
        if len(username) <= 10 and len(username) >= 5:
            break
        else:
            print("Error. Please enter your username that is at least 5-10 characters long. \n \t")

    # Calls password_encryption function that passes in user's password of choice  
    password = input("Next, please enter your password to unlock the game of Mad Libs. \n \t")
    encrypted_password = password_encryption(password)
    print("This is the encrypted version of your password: " + encrypted_password)

    # Checks if encrypted password and copied password are the exact same based on user's input 
    while True:
        copied_password = input("Please copy and paste the provided encrypted password below to proceed with the game. \n \t")
        if copied_password == encrypted_password:
            print("Awesome! Now let's play Mad Libs!")
            break
        else:
            print("Please try again. Passwords do not match. \n")
    
    # Using while True loop to play Mad Libs game by calling mad_libs() function, and replay the game by calling replay_game()
    # function. If False, the game will end. 
    replay = True 
    while replay: 
        play_game = mad_libs()
        replay = replay_game()
    
    print("Thank you for playing my game! See you next time! :)")
    

def remove_punct(user_input):
    """The remove_punct function gets rid of all punctuation from the string.
    
    Parameters
    ----------
    user_input : string
        Input received from user
 
    Returns
    -------
    output_list : string 
        User's input with removed punctuation 
    """
    
    
    # Defining new variable output_list as empty string
    output_list = ""
    
    # Loop through each character in user_input. If character is not in string.punctuation, it appends the current character
    # to output_list. This remove punctuation concept was adapated from Assignment 3: Chatbots 
    for char in user_input:
        if char not in string.punctuation:
            output_list = output_list + char
            
    # Returns user input with removed punctuation 
    return output_list 


def prepare_word(user_input):
    """The prepare_word function prepares the user inputs for processing by splitting the string into words through .split()
    string method and making the string all lower case through .lower() string method. The function calls remove_punct() function
    that passes in a string and appends the new string in a list. The function finally returns a list of string free of
    punctuation and uppercases so that a Mad Libs story can be properly generated.  
    
    Parameters
    ----------
    user_input : string
        Input received from user
 
    Returns
    -------
    output_list : list of string 
        New list of string free of punctuation and uppercases 
    """
    
    
    # Splits the string into words by using string method .split()
    word_list = user_input.split(",")
    
    # Initialize to collect a list of strings 
    output_list = []
    
    # Looping through list of strings to make the string all lower case and remove all punctuation from the string 
    for word in word_list:
        word = word.lower()
        word = remove_punct(word)
        output_list.append(word)
        
    # Returning a list of string free of punctuation and uppercases 
    return output_list


def replay_game():
    """The replay_game function allows the user to replay the Mad Libs game if desired and asks whether the user has
    enjoyed the game. The function will also allow the user to end the game. 
    """
    
    
    final_q = "Congrats! You have finished the game of Mad Libs! Did you enjoy it? Yes or No. \n \t"
    
    # Using while True loop to ask users whether they have enjoyed the game 
    while True:
        final_input = input(final_q)
        
        # Checks if user input is the string 'yes'. If False, the user will end the game. Otherwise, error message provided.
        if final_input.lower() == "yes":
            replay_q = "Awesome! Would you like to play another round of game? Yes or No. \n \t"
            
            # Using while True loop to ask users whether they want to play another round
            while True:
                replay_input = input(replay_q)
                
                # Checks if user input is the string 'yes'. If False, the user exits the game. Otherwise, error message provided
                if replay_input.lower() == "yes":
                    return True 
                elif replay_input.lower() == "no":
                    return False 
                else:
                    print("Input not recognized.")
                    replay_q = "Please try again. Do you want to play another round of game? Yes or No. \n \t"
                    
        elif final_input.lower() == "no": 
            return False 
        else:
            print("Input not recognized. ")
            final_q = "Please try again. Did you enjoy the game? Yes or No. \n \t"

