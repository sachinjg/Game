#-*-coding: UTF-8-*-
# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1



easy_info = ["The United Nations annual World Happiness Report has named ", "___1___", "as the world's happiest nation jumping up from fourth place last year."
            " the latest World Happiness Report, released Monday by the Sustainable Development Solutions Network for the United Nations. "
            "Other superpowers didn't fare better than Northern Europe either.", "___2___", "came in 14th place, dropping one place from last year.",
            "___3___", "has won the title three of the four times the report has been issued", "___4___",
            "came in 16th place for the second year",
            "___5___", "'moved up four spots to 19th place"]

easy_answers = ["Norway", "USA", "Denmark", "Germany", "UK"]

# The medium empty fill-in-the-blank and its corresponding answers.
medium_info = ["Portuguese footballer who plays as a forward for Spanish La Liga club Real Madrid and who serves as captain of the Portuguese national team.", "___1___", 
            "___2___", " only stands 5’7”, but this small package has definitely yielded some huge things."
            "For His Achievements in Sprinting he Nicknamed as “Lightning ", "___3___",
            "___4___", " free kick magician English footballer.",
            "___5___", " icknamed the “Black Mamba”, is an American professional basketball player, Formerly a high-flying dunker, Bryant is now a prolific jump shooter and phenomenal defender in the National Basketball Association (NBA).."]

medium_answers = ["CristianoRonaldo", "LionelMessi", "UsainBolt", "DavidBeckham", "KobeBryant"]

# The hard empty fill-in-the-blank and its corresponding answers.
hard_info = ["If Brazil owned South American travel last year.", "___1___", 
            "___2___", "became a self-governing dominion within the British Empire – a country, in other words."
            "What an intriguing mix of innovation and tradition ", "___3___",
            "___4___", "Spending a few days drifting around Granada is the most sensual of history lessons.",
            "___5___", " Hark! Is that the sound of hooves? There hasn’t been this much action on Hadrian’s Wall since Roman troops tramped up Ermine Street in the second century to build the 73-mile barrier between Bowness and Wallsend."]

hard_answers = ["Chile", "Canada", "India", "Spain", "England"]


def load_info_difficulty():
    """Asks the user for a difficulty level and loads that level's data.
    Args:
        none.
    Returns:
        (list of str): empty fill-in-the-blank.
        (list of str): answer key.
        (str): difficulty level.
        """
    
    level = raw_input("\nPlease select a difficulty level for general knowledge quiz"
                      "general knowledge  fill-in-the-blank (easy, medium, or hard):")
    if level.lower() == "easy":
        return easy_info, easy_answers, "easy"
    if level.lower() == "medium":
        return medium_info,  medium_answers, "medium"
    if level.lower() == "hard":
        return hard_info, hard_answers, "hard"
    else:
        print "You selected an invalid difficulty level!"
        return load_info_difficulty()


def remove_spaces_before_punc(info_string):
    """Removes spaces before punctuation.

    Removes the spaces after blanks and before punctuation (i.e. ___n___ .)
    that are created by " ".join(info).

    Args:
        info_string (str): the concatenated fill-in-the-blank with the unwanted
        spaces.
    Returns:
        (str): the same string without the unwanted spaces.
    """
    
    info_string = info_string.replace(" .", ".")
    info_string = info_string.replace(" !", "!")
    return info_string


def provide_link(level):
    """Provides a link.
    Args:
        level (str): the chosen difficulty level.
    Returns:
        (str): link.
    """
    if level == "easy":
        return "http://www.cnn.com/2017/03/20/travel/worlds-happiest-countries-united-nations-2017/"
    if level == "medium":
        return "http://sporteology.com/top-10-popular-athletes-in-the-world/"
    if level == "hard":
        return "http://www.telegraph.co.uk/travel/lists/20-best-destinations-for-2017/ "
                

    
def guess_check(blank_number, info, answers, answer):
    """Asks the user for a guess. If correct, moves to the next blank.
    Prompts the user to fill in the first blank. Displays the updated
    fill-in-the-blank when the user inputs the correct answer and prompts them
    to fill in the next blank. Prompts the user to try again when their guess
    is incorrect.
    
    Args:
        blank_number (int): the current blank number.
        info (list of str): the fill-in-the-blank in its current state.
        answers (list of str): the answer key.
        answer (str): the answer to the current blank.
    Returns:
        (int): the next blank number.
    """
    
    blank = "___" + str(blank_number) + "___"
    guess = raw_input("Please fill in blank #" + str(blank_number) +
                      " (case-sensitive): ")
    if guess == answer:
        info[info.index(blank)] = answer
        print remove_spaces_before_punc(" ".join(info)) + "\n"
        blank_number += 1
        return blank_number
    else:
        print "Incorrect. Please try again.\n"
        return guess_check(blank_number,info, answers, answer)


def play_game():
    """Plays a full game of fill-in-the-blanks.
    Displays the chosen empty fill-in-the-blank. Game ends with a printed
    congratulations statement.
    Args:
        none.
    Returns:
        none.
    """
    info, answers, level = load_info_difficulty()
    print ("\nHere is the fill-in-the-blank for the " + level + " difficulty "
           "level:")
    print remove_spaces_before_punc(" ".join(info)) + "\n"

    blank_number = 1
    for answer in answers:
        blank_number = guess_check(blank_number, info, answers, answer)

    print ("Congratulations")
    print provide_link(level) + "\n"
play_game()
