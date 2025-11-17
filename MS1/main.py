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
        towers, target, n_disks = start_new_game()
    else:
        return None
    
    play(towers, n_disks, target)

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

def start_new_game() -> list:
    ''''
    Purpose: Function to begin a new game.
    Parameters: None.
    Returns: None.
    '''
    print("Starting new game.")
    #unpack list of inputs into their respective variables
    n_towers, n_disks = get_user_input([f"Number of Towers [min=3, max=9]: ", "Number of disks [max=3, min=9]: "], [9, 9], [3, 3])
    target_tower = get_user_input([f"Target Tower [min=2, max={n_towers}]: "], [n_towers], [2])[0]
    towers = initialize_towers(n_towers, n_disks)
    return [towers, target_tower, n_disks]

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

def play(towers:dict, n_disks:int, target_tower: int) -> None:
    count = 0
    while True:
        display(towers, n_disks)
        question = "Enter 1 or 2 or 3: "
        print("1 - Move a Disk\n2 - Save and end\n3 - End without saving")
        decision = get_user_input([question], [3], [1])[0]
        if decision == 1:
            count += 1
            move(towers)
            if win_check(towers, target_tower, n_disks):
                print(f"Good job! Transfer achieved in {count} steps.")
                break
        elif decision == 3:
            break

def move(towers:dict) -> None:
    questions = ["Source Tower: ", "Destination Tower: "]
    source, destination = get_user_input(questions, [len(towers), len(towers)], [1, 1])
    if towers[source].is_empty():
        print("Tower is empty. Please try again.")
        return None
    disk = towers[source].pop()
    towers[destination].push(disk)
    return None

def win_check(towers:dict, target:int, n_disks:int) -> bool:
    win_list = []
    for n in range(n_disks, 0, -1):
        win_list.append(n)
    if towers[target].is_empty():
        return False
    if len(towers[target]) < len(win_list):
        return False
    for i in range(0, len(win_list)):
        if towers[target].get_lst()[i] != win_list[i]:
            return False
    return True

def save_game():
    return None

main()