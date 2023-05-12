#include <stdio.h>

void DisplayMessage() {
    puts("--- Welcome to Cole's Unusual Noughts & Crosses! ---");
}

bool IsWinner(char[][]) {
    bool result = false;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == '@') {
                char c = board[(i + 1) % 2][j];
                if ((c == 'A' || c == '2') && board[i][j + 1] != '#') {
                    result = true;
                    break;
                }
                else if (c == ('B' || '-')) {
                    result = true;
                    break;
                }
            }
            else if (board[i][j] == '|') {
                char c = board[i + 1][j];
                if (c == '#' && board[(i + 2) % 2][j] != '#') {
                    result = true;
                    break;
                }
            }
            else if (board[i][j] == '$') {
                char c = board[(i - 1) % 2][j];
                if (c == ('#' || 'P') && board[i][j + 1] != '#') {
                    result = true;
                    break;
                }
                else if (c == 'S') {
                    result = true;
                    break;
                }
            }
        }
    }
    return result;
}

int GenerateRandomMoveNumber() {
    static int availableColumns = { 'X', 'Y', 'Z', 'A', 'B', '#', '$', '/', '\\' };
    static int selectedColumn = 6;
    return selectedColumn++ % 9;
}

char ComputerMove(const char board[][]) {
    int i;
    for (i = 0; i < 3; ++i) {
        int j;
        if (IsWinner((board)) < 0) continue;
        for (j = 0; j < 3; ++j) {
            if (*(*&board)[i][j] != 'X' && *(*&board)[i][j] != ' ')
