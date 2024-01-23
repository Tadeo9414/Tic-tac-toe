def winner(symbols, winning_matrix):
    for conditions in winning_matrix:
        winning_symbol = symbols[conditions[0]]
        if all(symbols[i] == winning_symbol for i in conditions):
            if winning_symbol == 'X' or winning_symbol == 'O':
                return f'{winning_symbol} wins'


def grid(user_input):
    print('---------')
    for i in range(0, 7, 3):
        print(f'| {user_input[i]} {user_input[i + 1]} {user_input[i + 2]} |')
    print('---------')


def make_move(user_input, turn):
    while True:
        try:
            x, y = map(int, input("Make a move: ").split())
            index = ((x - 1) * 3) + (y - 1)
            if not (1 <= x <= 3) or not (1 <= y <= 3):
                print('Coordinates should be from 1 to 3!')
            elif user_input[index] != '_':
                print('This cell is occupied! Choose another one!')
            else:
                user_input[index] = turn
                grid(user_input)
                break
        except ValueError:
            print('You should enter numbers!')


def main():
    winning_conditions = [
        [0, 1, 2],  # row from left to right
        [3, 4, 5],  # 2nd row from left to right
        [6, 7, 8],  # 3rd row from left to right
        [0, 3, 6],  # 1st row from top to bottom
        [1, 4, 7],  # 2nd row from top to bottom
        [2, 5, 8],  # 3rd row from top to bottom
        [0, 4, 8],  # 1st diagonally
        [2, 4, 6],  # 2nd diagonally
    ]
    while True:
        board = list('_________')
        grid(board)
        player = 'X'
        while True:
            print('Player ' + player + ' turn: ')
            make_move(board, player)
            result = winner(board, winning_conditions)
            if result:
                print(result)
                break
            elif '_' not in board:
                print('Draw')
                break
            player = 'O' if player == 'X' else 'X'

        new_game = input('Restart? (y/n): ')
        if new_game != 'y':
            break


main()
