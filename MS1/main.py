'''
|--------------------------------------------------------------------|
|Names: Pavel Trninkov, Alex Bachynsky                               |
|Programming Project: Milestone #1                                   |
|--------------------------------------------------------------------|
'''

def main() -> None:
    ''''
    Purpose: Main function to call and begin application.
    Parameters: None.
    Returns: None.
    '''
    while True:
        selection = gather_user_input(["Enter 1 to Start a new game and 2 to Resume a saved game: "])
        decision(selection)
        break
    return None

def gather_user_input(user_questions) -> list:
    ''''
    Purpose: Helper function to gather user inputs.
    Parameters: A list of questions.
    Returns: A list of user inputs.
    '''
    answers = []
    for question in user_questions:
        user_input = input(question)
        if validate_input(user_input, len(user_questions)):
            answers.append(int(user_input))
        else:
            print("Error: Invalid answer.")
    return answers

def validate_input(user_input:str, max_limit:int) -> bool:
    ''''
    Purpose: Helper function to validate user inputs
    Parameters: User input.
    Returns: True if valid, False if not.
    '''
    
    #if user input is invalid, return false and dictate is invalid
    if len(user_input.strip()) < 1:
        return False
    
    if user_input.isdigit() != True:
        return False
    
    if int(user_input) > max_limit:
        return False

    return True

def decision(selection):
    return None

def move(source, target, disks):
    return None

def win_check(target, disks):
    return None

def print_status():
    return None

def save_game():
    return None

def end():
    return None

main()