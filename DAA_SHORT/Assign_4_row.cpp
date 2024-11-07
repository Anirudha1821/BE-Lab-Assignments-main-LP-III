#include <bits/stdc++.h>
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
    // Check this row on the left side
    for (int i = 0; i < col; i++) {
        if (board[row][i]) return false;
    }

    // Check upper-left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j]) return false;
    }

    // Check lower-left diagonal
    for (int i = row, j = col; i < n && j >= 0; i++, j--) {
        if (board[i][j]) return false;
    }

    return true;
}

// Function to solve N-Queens problem using backtracking
bool solveNQueens(vector<vector<int>>& board, int col, int n) {
    if (col >= n) return true; // All queens are placed successfully

    for (int row = 0; row < n; row++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 1; // Place queen

            if (solveNQueens(board, col + 1, n)) // Recur to place queen in the next column
                return true;

            board[row][col] = 0; // Backtrack if placing queen here leads to no solution
        }
    }
    return false; // No place is found in this column for a queen
}

int main() {
    int n, firstQueenRow;
    cout << "Enter the size of the board (n): ";
    cin >> n;
    cout << "Enter the row (0 to " << n - 1 << ") for the first queen in the first column: ";
    cin >> firstQueenRow;

    vector<vector<int>> board(n, vector<int>(n, 0));
    board[firstQueenRow][0] = 1; // Place the first queen at (firstQueenRow, 0)

    if (solveNQueens(board, 1, n)) { // Start placing queens from column 1
        cout << "Solution:\n";
        printBoard(board);
    } else {
        cout << "No solution exists.\n";
    }

    return 0;
}
