'''
|--------------------------------------------------------------------|
|Names: Pavel Trninkov, Alex Bachynsky                               |
|Programming Project: Milestone #1                                   |
|--------------------------------------------------------------------|
'''

from stack import Stack

def main() -> None:
    ''''
    Purpose: Main function to call and begin application.
    Parameters: None.
    Returns: None.
    '''
    selection = get_user_input(["Enter 1 to Start a new game and 2 to Resume a saved game: "], [2], [1])
    if selection[0] == 1:
        start_new_game()
    else:
        return None

def get_user_input(user_questions:list, max_limit:list, min_limit:list) -> list:
    ''''
    Purpose: Helper function to gather user inputs.
    Parameters: A list of questions and a limit to the max acceptable int.
    Returns: A list of user inputs.
    '''
    answers = []
    question = 0
    while question < len(user_questions):
        user_input = input(user_questions[question])
        if validate_input(user_input) != True:
            print("Error: Invalid input.")
            continue
        if int(user_input) > max_limit[question]:
            print("Error: Invalid input.")
            continue
        if int(user_input) < min_limit[question]:
            print("Error: Invalid Input")
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
    ''''
    Purpose: Function to begin a new game.
    Parameters: None.
    Returns: None.
    '''
    print("Starting new game.")
    #unpack list of inputs into their respective variables
    n_towers, n_disks, target_tower = get_user_input(["Number of Towers [min=3, max=9]: ", "Number of disks [max=3, min=9]: ", "Target Tower[min=2, max=3]: "], [9, 9, 3], [3, 3, 2])
    towers = initialize_towers(n_towers, n_disks)
    while True:
        display(towers, n_disks)
        
        break
    return None

def initialize_towers(num_tower: int, num_disks: int) -> dict:
    ''''
    Purpose: Helper function to initialize dictionary to hold towers.
    Parameters: number of towers and number of disks
    Returns: a dictionary of towers
    '''
    towers = dict()
    for tower in range(1, num_tower + 1):
        towers[tower] = Stack()
    for disk in range(num_disks, 0, -1):
        towers[1].push(disk)
    return towers
    

def display(towers:dict, size: int) -> None:
    ''''
    Purpose: Helper function to display the towers.
    Parameters: Towers dictionary and number of disks(size).
    Returns: None.
    '''
    for i in range(1, len(towers) + 1):
        print("="*size + str(i) + "=" * size + " ", end=" ")
    print()
    for y in range(1, size + 1):
        for x in range(1, len(towers) + 1):
            if len(towers[x].get_lst()) >= y:
                disk_length = towers[x].get_lst()[y-1]
            else:
                disk_length = 0
            s_left = " " * (size - disk_length) + "*" * (disk_length)
            s_right = "*" * (disk_length) + " " * (size-disk_length)
            print(s_left + "|" + s_right + " ", end=" ")
        print()
    return None

def move(towers:dict):
    return None

def win_check(target, disks):
    return None

def save_game():
    return None

def end():
    return None

main()