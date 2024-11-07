#include <bits/stdc++.h>
#include <vector>
using namespace std;

void printBoard(const vector<vector<int>>& board) {
    for (const auto& row : board) {
        for (int cell : row) {
            cout << (cell ? "Q " : ". ");
        }
        cout << endl;
    }
    cout << endl;
}

// Function to check if a queen can be placed at board[row][col]
bool isSafe(const vector<vector<int>>& board, int row, int col, int n) {
    // Check this column on upper side
    for (int i = 0; i < row; i++) {
        if (board[i][col]) return false;
    }

    // Check upper left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j]) return false;
    }

    // Check upper right diagonal
    for (int i = row, j = col; i >= 0 && j < n; i--, j++) {
        if (board[i][j]) return false;
    }

    return true;
}

// Function to solve N-Queens problem using backtracking
bool solveNQueens(vector<vector<int>>& board, int row, int n) {
    if (row >= n) return true; // All queens are placed successfully

    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 1; // Place queen

            if (solveNQueens(board, row + 1, n)) // Recur to place next queen
                return true;

            board[row][col] = 0; // Backtrack if placing queen here leads to no solution
        }
    }
    return false; // No place is found in this row for a queen
}

int main() {
    int n, firstQueenCol;
    cout << "Enter the size of the board (n): ";
    cin >> n;
    cout << "Enter the column (0 to " << n - 1 << ") for the first queen in the first row: ";
    cin >> firstQueenCol;

    vector<vector<int>> board(n, vector<int>(n, 0));
    board[0][firstQueenCol] = 1; // Place the first queen at (0, firstQueenCol)

    if (solveNQueens(board, 1, n)) { // Start placing queens from row 1
        cout << "Solution:\n";
        printBoard(board);
    } else {
        cout << "No solution exists.\n";
    }

    return 0;
}
