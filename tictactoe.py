#!/usr/bin/env python3
"""
Tic Tac Toe for two players.
• 2 players should be able to play the game (both sitting at the same computer)
• The board should be printed out every time a player makes a move
• You should be able to accept input of the player position and then place a symbol on the board.
"""
import os

# TODO:
#   * Randomize which user goes first.
#   * Switch turns and prompt for the other user after each user has played.
#   * Once the first X or O is played, it will be associated with that player for the duration of the game.
#   * Add validation so that the players cannot play the other letter.
#   * Add option to replay.

# Initial board
board = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
greyon = "\033[0;90m"
greyoff = "\033[0m"
coloron = "\033[0;33m"
coloroff = "\033[0m"

def main():
    get_input(True)

def print_board():
    # Clear the screen before each turn.
    absolutely_unused_variable = os.system("clear") # This variable gets the output from the clear command, else it would print to screen.
    print ('+---+---+---+')
    print ('| {r1} | {r2} | {r3} |'.format(r1=greyon+board['1']+greyoff,r2=greyon+board['2']+greyoff,r3=greyon+board['3']+greyoff))
    print ('+---+---+---+')
    print ('| {r1} | {r2} | {r3} |'.format(r1=greyon+board['4']+greyoff,r2=greyon+board['5']+greyoff,r3=greyon+board['6']+greyoff))
    print ('+---+---+---+')
    print ('| {r1} | {r2} | {r3} |'.format(r1=greyon+board['7']+greyoff,r2=greyon+board['8']+greyoff,r3=greyon+board['9']+greyoff))
    print ('+---+---+---+')
    print ('\nEnter q to exit')

def help():
    print ('\n')
    msg = 'Please choose which box to fill using X or O.'
    msg += '\nThe boxes are numbered from 1 to 9, so enter the box number and the X or O.'
    msg += '\nSample input: 3X or 7O (capital "o", not zero)'
    print (msg)

def strip_chars(st):
    # Remove the colourizing chars
    stripped_val = st.replace(coloron,'')
    stripped_val = stripped_val.replace(coloroff,'')
    return stripped_val

def check_for_win(loc, x_or_o):
    # Add the colour changes to the character so a simple string comparison succeeds.
    x_or_o = coloron + x_or_o + coloroff
    # Check for winning combination
    if (board['1'] == x_or_o and board['2'] == x_or_o and board['3'] == x_or_o) or \
        (board['4'] == x_or_o and board['5'] == x_or_o and board['6'] == x_or_o) or \
        (board['7'] == x_or_o and board['8'] == x_or_o and board['9'] == x_or_o) or \
        (board['1'] == x_or_o and board['4'] == x_or_o and board['7'] == x_or_o) or \
        (board['2'] == x_or_o and board['5'] == x_or_o and board['8'] == x_or_o) or \
        (board['3'] == x_or_o and board['6'] == x_or_o and board['9'] == x_or_o) or \
        (board['1'] == x_or_o and board['5'] == x_or_o and board['9'] == x_or_o) or \
        (board['3'] == x_or_o and board['5'] == x_or_o and board['7'] == x_or_o):
            print ('You win!')
            exit()

    filled_cells = 0
    for cell in board.values():
        cell = strip_chars(cell);
        if cell in 'XO':
            filled_cells += 1

        if filled_cells == len(board):
            print ('\nIt is a tie!\n')
            exit()
    '''
    Couldn't figure out an easy way to check the combinations of squares dynamically to determine a winner,
    hence the 8 conditional expressions above.
    The solution from by the instructor was nearly identical to mine.
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    '''
def validate_input(st):
    #TOOD: If the input starts with 1-9, check that the second char is x or o
    if st[0] in '123456789':
        if str(st[1]).upper() in 'XO':
            return True

    if st.upper() == 'Q':
        return True
    return False

def get_input(first_time):
    print_board()
    if first_time == True:
        help()

    loc = 0
    x_or_o = ' '
    attempts = 0

    while int(loc) not in list(range(1,10)) or str(x_or_o) not in 'XO':
        # Get the user's selection
        loc_and_x_or_o = input()    # yeah yeah, poor choice of names.

        if validate_input(loc_and_x_or_o) != True:
            print ('Invalid input, please make a valid selection.')
            continue
        if loc_and_x_or_o == 'q':
            print ('\n\tGoodbye!\n')
            exit()

        # Split the input into the loc and x_or_o variables
        loc = str(loc_and_x_or_o[0])
        x_or_o = str(loc_and_x_or_o[1]).upper()
        # Merging dicts (turned out to be unnecessary)
        # http://treyhunner.com/2016/02/how-to-merge-dictionaries-in-python/
        #full_dict = {**row1, **row2, **row3} # Python 3.5 way to merge dicts

        # With the introduction of coloured text, the comparison
        # needs to be against the stripped cell value.
        cur_val = coloron + board[loc] + coloroff
        stripped_val = strip_chars(cur_val)

        if stripped_val in 'XO':
            loc = 0
            print ('That cell is already occupied! Choose again.')
            continue

    update_board(loc,x_or_o)


def update_board(loc, x_or_o):
    # Update the correct dict value
    global board
    board[loc] = coloron + x_or_o + coloroff
    # Print the board with the new values
    print_board()
    check_for_win(loc, x_or_o)
    get_input(False)

# Let's start the game
main()
