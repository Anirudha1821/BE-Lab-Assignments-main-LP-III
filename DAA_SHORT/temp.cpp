// #include<bits/stdc++.h>
// using namespace std;

// //Assign_2
// struct HuffmanNode {
//     char data;                  // Input character
//     int frequency;              // Frequency of the character
//     HuffmanNode *left, *right;  // Left and right children

//     HuffmanNode(char data, int frequency) {
//         this->data = data;
//         this->frequency = frequency;
//         left = right = nullptr;
//     }
// };

// struct Compare {
//     bool operator()(HuffmanNode* left, HuffmanNode* right) {
//         return left->frequency > right->frequency;
//     }
// };
// //Preorder
// void printCodes(HuffmanNode* root, string code, unordered_map<char, string>& huffmanCodes) {
//     if (!root) return;

//     // If this node is a leaf node, it contains a character
//     if (!root->left && !root->right) {
//         huffmanCodes[root->data] = code;
//         cout << root->data << ": " << code << endl;
//     }

//     // Traverse left and right subtrees
//     printCodes(root->left, code + "0", huffmanCodes);
//     printCodes(root->right, code + "1", huffmanCodes);
// }
// void buildHuffmanTree(const string& text) {
//     priority_queue<HuffmanNode*, vector<HuffmanNode*>, Compare> pq;
//     while (pq.size() > 1) {}
// }
// // --------------------------------------------------------------------------------------------------------------------

// // Assign_3

// struct Item {
//   int weight;
//   int profit;
// };

// int knapsack(int W, vector<Item> &items) {
//   int n = items.size();
//   vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

//   for (int i = 1; i <= n; i++) {
//     for (int w = 1; w <= W; w++) {
//       if (items[i - 1].weight <= w) {
//         dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].profit);
//       } else {
//         dp[i][w] = dp[i - 1][w];
//       }
//     }
//   }
//   return dp[n][W];
// }

// // --------------------------------------------------------------------------------------------------------------------
// // Assign_4 
// vector<vector<int>> board(n, vector<int>(n, 0));
// bool isSafe(const vector<vector<int>>& board, int row, int col, int n) {
//     for (int i = 0; i < col; i++) {
//         if (board[row][i]) return false;
//     }

//     for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
//         if (board[i][j]) return false;
//     }

//     for (int i = row, j = col; i < n && j >= 0; i++, j--) {
//         if (board[i][j]) return false;
//     }

//     return true;
// }

// bool solveNQueens(vector<vector<int>>& board, int col, int n) {
//     if (col >= n) return true;

//     for (int row = 0; row < n; row++) {
//         if (isSafe(board, row, col, n)) {
//             board[row][col] = 1;

//             if (solveNQueens(board, col + 1, n))
//                 return true;

//             board[row][col] = 0;
//         }
//     }
//     return false;
// }
// // ---------------------------------------------------------------------------------------

// // Assign_5
// int deterministicPartition(vector<int> &arr, int low, int high)
// {
//   int pivot = arr[low]; // Pivot is the first element
//   int i = low;
//   int j = high;

//   while (i < j)
//   {
//     while (arr[i] <= pivot && i <= high - 1)
//     {
//       i++;
//     }
//     while (arr[j] > pivot && j >= low + 1)
//     {
//       j--;
//     }
//     if (i < j)
//       swap(arr[i], arr[j]);
//   }
//   swap(arr[low], arr[j]);
//   return j;
// }

// void deterministicQuickSort(vector<int> &arr, int low, int high, int &comparisons, int &swaps)
// {
//   if (low < high)
//   {
//     int pivotIndex = deterministicPartition(arr, low, high);
//     comparisons += (high - low); // Count comparisons made during partition
//     swaps += 2;                  // Count the swaps made during partition

//     deterministicQuickSort(arr, low, pivotIndex - 1, comparisons, swaps);
//     deterministicQuickSort(arr, pivotIndex + 1, high, comparisons, swaps);
//   }
// }

// // FOR RENDOMIZED 

// int pivotIndex = low + rand() % (high - low + 1); // create a random pivot index
// swap(arr[low], arr[pivotIndex]); 



// int main(){


//     return 0;
// }