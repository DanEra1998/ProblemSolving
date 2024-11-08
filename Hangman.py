import random as called_random
# ////////////////////////////////////////////////
#               ASCII ART SECTION
# ////////////////////////////////////////////////
hangman_art = """
 _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ 
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

menu_option = """
type s
"""







# ////////////////////////////////////////////////
#          Main logic section
# ////////////////////////////////////////////////

def starting_hangman():
    hangman_stages = [
        """
         ____
        |    |
        |    
        |    
        |   
        |   
        |
       _|_
        """,
        """
         ____
        |    |
        |    O
        |    
        |   
        |   
        |
       _|_
        """,
        """
         ____
        |    |
        |    O
        |    |
        |    
        |   
        |
       _|_
        """,
        """
         ____
        |    |
        |    O
        |   /|
        |    
        |   
        |
       _|_
        """,
        """
         ____
        |    |
        |    O
        |   /|\\
        |    
        |   
        |
       _|_
        """,
        """
         ____
        |    |
        |    O
        |   /|\\
        |   / 
        |   
        |
       _|_
        """,
        """
         ____
        |    |
        |    O
        |   /|\\
        |   / \\
        |   
        |
       _|_
        """
    ]


    list_of_words = ["switch", "blowjob", "halo", "jackson"]

    selected_word_from_list = called_random.choice(list_of_words).strip().lower()

    max_attempts = len(hangman_stages) - 1
    attempts = 0

    # Initialize a set to track the unique letters in the selected word
    letters_to_guess = set(selected_word_from_list)

    # Create a set to track the correct guesses made by the user
    correct_guesses = set()
    # Initialize underscores string based on the length of the word
    underscores = ["_"] * len(selected_word_from_list)
    while attempts < max_attempts:
        print(" ".join(underscores))
        user_guess = input("Insert your guess: ").strip().lower()

        if user_guess in selected_word_from_list:
            correct_guesses.add(user_guess)
            print("Great guess!")

            # Update the underscores list with the correct guess
            for index, letter in enumerate(selected_word_from_list):
                if letter == user_guess:
                    underscores[index] = user_guess

            # Check if all letters have been guessed
            if letters_to_guess == correct_guesses:
                print(f"Congratulations! You've guessed the word: {selected_word_from_list}")
                break
        else:
            attempts += 1
            print(hangman_stages[attempts])

        if attempts == max_attempts:
            print(f"Game over! The word was: {selected_word_from_list}")



print(hangman_art)

continue_playing = True

while continue_playing:

    menu_input = input("Do you want to play Hangman? (yes/no)").strip().lower()

    if menu_input == "yes":
        starting_hangman()
        break

    elif menu_input == "no":
        continue_playing = False
        print("Thanks for playing!")
    else:
        print("not a valid option, please enter: yes or no")





# ////////////////////////////////////////////////
#          notes for myself
# ////////////////////////////////////////////////
'''
    .strip():
        remove any leading and trailing whitespace characters (such as spaces, tabs, or newlines) from 
        a string. This means that it will remove any extra spaces before or after the actual text in
        the string.

    .lower() just changes all characters in the string to lower case
'''