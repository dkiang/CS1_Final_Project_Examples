#include <stdio.h>
#include <stdbool.h>

#define ROWS 6
#define COLS 7
#define RED "\x1B[31m"
#define YELLOW "\x1B[33m"
#define RESET "\x1B[0m"

void print_board(char board[ROWS][COLS]);
void initialize_board(char board[ROWS][COLS]);
bool check_winner(char board[ROWS][COLS], char player);
bool make_move(char board[ROWS][COLS], int col, char player);

int main() {
    char board[ROWS][COLS];
    initialize_board(board);
    int current_player = 1;
    int col;

    while (true) {
        print_board(board);
        printf("Player %d (%s%c" RESET "), enter column (1-%d): ", current_player, current_player == 1 ? RED : YELLOW, current_player == 1 ? 'R' : 'Y', COLS);
        scanf("%d", &col);
        col--;

        if (col < 0 || col >= COLS || !make_move(board, col, current_player == 1 ? 'R' : 'Y')) {
            printf("Invalid move. Try again.\n");
            continue;
        }

        if (check_winner(board, current_player == 1 ? 'R' : 'Y')) {
            print_board(board);
            printf("Player %d (%s%c" RESET ") wins!\n", current_player, current_player == 1 ? RED : YELLOW, current_player == 1 ? 'R' : 'Y');
            break;
        }

        current_player = 3 - current_player;
    }

    return 0;
}

void print_board(char board[ROWS][COLS]) {
    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
            if (board[row][col] == 'R') {
                printf(RED "O " RESET);
            } else if (board[row][col] == 'Y') {
                printf(YELLOW "O " RESET);
            } else {
                printf(". ");
            }
        }
        printf("\n");
    }
}

// Returns true if a successful move was made on the game board
bool make_move(char board[ROWS][COLS], int col, char player) {
    // Iterate through rows in reverse order (starting from the bottom)
    for (int row = ROWS - 1; row >= 0; row--) {
        // If the current cell is empty (0)
        if (board[row][col] == 0) {
            // Place the player's symbol in the cell
            board[row][col] = player;
            // Return true to indicate that the move was made successfully
            return true;
        }
    }
    // If there's no empty cell in the chosen column, return false
    return false;
}


// Function to check if the current player has won the game
bool check_winner(char board[ROWS][COLS], char player) {
    // Iterate through all rows
    for (int row = 0; row < ROWS; row++) {
        // Iterate through all columns
        for (int col = 0; col < COLS; col++) {
            // Skip if the current cell doesn't have the player's symbol
            if (board[row][col] != player) {
                continue;
            }

            // Iterate through all directions (dx, dy) horizontally, vertically, and diagonally
            for (int dx = -1; dx <= 1; dx++) {
                for (int dy = -1; dy <= 1; dy++) {
                    // Skip when both dx and dy are zero (no direction)
                    if (dx == 0 && dy == 0) {
                        continue;
                    }

                    // Initialize a counter for consecutive symbols
                    int count = 0;

                    // Iterate through four consecutive cells in the current direction
                    for (int i = 0; i < 4; i++) {
                        // Calculate the row and column of the current cell in the sequence
                        int r = row + dy * i;
                        int c = col + dx * i;

                        // Check if the calculated row and column are within the board's boundaries
                        if (r < 0 || r >= ROWS || c < 0 || c >= COLS) {
                            break;
                        }

                        // Increment the counter if the cell has the current player's symbol
                        if (board[r][c] == player) {
                            count++;
                        } else {
                            break;
                        }
                    }

                    // If the counter is 4, the player has won
                    if (count == 4) {
                        return true;
                    }
                }
            }
        }
    }
    // If no winning sequence is found, return false
    return false;
}

void initialize_board(char board[ROWS][COLS])
{
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            board[i][j] = 0;
        }
    }
}
