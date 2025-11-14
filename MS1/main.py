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
        selection = gather_user_input(["Enter 1 to Start a new game and 2 to Resume a saved game: "], 2)
        if selection[0] == 1:
            start_new_game()
        else:
            break
    return None

def gather_user_input(user_questions:list, max_limit:int) -> list:
    ''''
    Purpose: Helper function to gather user inputs.
    Parameters: A list of questions and a limit to the max acceptable int.
    Returns: A list of user inputs.
    '''
    answers = []
    question = 0
    while True:
        if question > len(user_questions) - 1:
            break
        user_input = input(user_questions[question])
        if validate_input(user_input) != True:
            print("Error: Invalid input.")
            continue
        if int(user_input) > max_limit:
            print("Error: Invalid input.")
            continue
        answers.append(int(user_input))
        question+=1
    return answers

def validate_input(user_input:str) -> bool:
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

    return True

def start_new_game() -> None:
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