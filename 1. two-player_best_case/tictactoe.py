# Exploring Tic Tac Toe
# two-player best case scenario.

# this file shows the basic implementation of the tic tac toe game
# this uses dictionary to store the boards accessible 9 points
# turn based rotation for two players.
# checks the winning case for each possible move provided.

# doesn't store input pattern
# doesn't reduce input paradigm
# no wrong input handeling
##

board = {'tl': 'tl', 'tm': 'tm', 'tr': 'tr',
         'ml': 'ml', 'mm': 'mm', 'mr': 'mr',
         'bl': 'bl', 'bm': 'bm', 'br': 'br'}


def printBoard(board):
    print(f"{board['tl']} |{board['tm']} |{board['tr']}")
    print("---+---+---")
    print(f"{board['ml']} |{board['mm']} |{board['mr']}")
    print("---+---+---")
    print(f"{board['bl']} |{board['bm']} |{board['br']}")
    print()

# printBoard(board)


def checker(board, move, turn):
    if board['tl'] == board['mm'] == board['br'] or \
            board['bl'] == board['mm'] == board['tr'] or \
            board['tl'] == board['ml'] == board['bl'] or \
            board['tm'] == board['mm'] == board['bm'] or \
            board['tr'] == board['mr'] == board['br'] or \
            board['tl'] == board['tm'] == board['tr'] or \
            board['ml'] == board['mm'] == board['mr'] or \
            board['bl'] == board['bm'] == board['br']:
        print(f'{turn} wins the game')
        result = 'W'
        return 0


turn = ' X'
result = 'D'
printBoard(board)
for i in range(9):

    print(f'Turn for {turn}. Move on Which Space!?')
    move = input()
    if move == '':
        print('thanks for playing ! bye!')
        break
    board[move] = turn
    printBoard(board)
    if checker(board, move, turn) == 0:
        break

    if turn == ' X':
        turn = ' O'
    else:
        turn = ' X'

if result == 'D':
    print('result is a draw!!')
