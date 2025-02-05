"""
Abduljabbar Said
July 2023
"""
# Print the playing board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def winCheck(board, player):

    #Check the rows to see if a player won
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    #Check the columns to see if a player won
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    #Check diagonals to see if a player won
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    #Check if the board is full with no empty spaces left on the board
    return all(cell in ('X', 'O') for row in board for cell in row)

def main():
    #Start off the board with empty spaces
    board = [[' ' for _ in range(3)] for _ in range(3)]
    #2 players & keeping track of turns
    players = ['X', 'O']
    turn = 0 
    
    while True:
        print_board(board)
        player = players[turn % 2]
        
        try:
            # Get input from the player
            row, col = map(int, input(f"Player {player}, enter row and column (0-2, space-separated): ").split())
            if board[row][col] != ' ':
                print("Cell already occupied! Try again.")
                continue
        except (ValueError, IndexError):
            # Handle invalid input
            print("Invalid input! Enter two numbers between 0 and 2.")
            continue
        
        board[row][col] = player  # Place the player's mark on the board
        
        if winCheck(board, player):  # Check for a winner
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if is_full(board):  # Check if the game is a tie
            print_board(board)
            print("It's a tie!")
            break
        
        turn += 1  # Switch turns

if __name__ == "__main__":
    main()  # Start the game
