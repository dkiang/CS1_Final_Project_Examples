#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <cs50.h>
#include <ctype.h>

// Function to check if the word exists in the grid
bool findWord(char grid[10][10], char *word, int len);
void fillGridWithRandomLetters(char grid[10][10]);
string convert_to_upper(string input);

int main() {
    // Pre-determined 10x10 grid of capital letters
    char grid[10][10];
    fillGridWithRandomLetters(grid);
    string input;
    int points = 0;
    
    printf("Enter words you find in the grid (type 'quit' to exit):\n");

    while (1) {
        input = get_string("Enter words you find in the grid (type 'quit' to exit): ");
        input = convert_to_upper(input);
        if (strcmp(input, "QUIT") == 0) {
            break;
        }

        if (findWord(grid, input, strlen(input))) {
            points++;
            printf("Word found! Points: %d\n", points);
            break;
        }

        else {
            printf("Word not found. Points: %d\n", points);
        }
    }

    printf("Final score: %d points\n", points);

    return 0;
}

bool findWord(char grid[10][10], char *word, int len) {
    for (int row = 0; row < 10; row++) {
        for (int col = 0; col < 10; col++) {
            if (grid[row][col] == word[0]) {
                // Check right
                if (col + len <= 10) {
                    int i;
                    for (i = 1; i < len; i++) {
                        if (grid[row][col + i] != word[i])
                            break;
                    }
                    if (i == len) return true;
                }

                // Check left
                if (col - len >= -1) {
                    int i;
                    for (i = 1; i < len; i++) {
                        if (grid[row][col - i] != word[i])
                            break;
                    }
                    if (i == len) return true;
                }

                // Check down
                if (row + len <= 10) {
                    int i;
                    for (i = 1; i < len; i++) {
                        if (grid[row + i][col] != word[i])
                            break;
                    }
                    if (i == len) return true;
                }

                // Check up
                if (row - len >= -1) {
                    int i;
                    for (i = 1; i < len; i++) {
                        if (grid[row - i][col] != word[i])
                            break;
                    }
                    if (i == len) return true;
                }

                // Check diagonal right-down
                if (row + len <= 10 && col + len <= 10) {
                    int i;
                    for (i = 1; i < len; i++) {
                        if (grid[row + i][col + i] != word[i])
                            break;
                    }
                    if (i == len) return true;
                }

                // Check diagonal left-down
                if (row + len <= 10 && col - len >= -1) {
                    int i;
                    for (i = 1; i < len; i++) {
                        if (grid[row + i][col - i] != word[i])
                            break;
                    }
                    if (i == len) return true;
                }

                // Check diagonal right-up
                if (row - len >= -1 && col + len <= 10) {
                    int i;
                    for (i = 1; i < len; i++) {
                        if (grid[row - i][col + i] != word[i])
                            break;
                    }
                    if (i == len) return true;
                }

                // Check diagonal left-up
                if (row - len >= -1 && col - len >= -1) {
                    int i;
                    for (i = 1; i < len; i++) {
                        if (grid[row - i][col - i] != word[i])
                            break;
                    }
                    if (i == len) return true;
                }
            }
        }
    }
    return false;
}

void fillGridWithRandomLetters(char grid[10][10]) {
    for (int row = 0; row < 10; row++) {
        for (int col = 0; col < 10; col++) {
            grid[row][col] = 'A' + rand() % 26;
        }
    }
}

string convert_to_upper(string input)
{
    string output = "";
    for (int i = 0, n = strlen(input); i < n; i++)
    {
        output += toupper(input[i]);
    }
    return output;
}
