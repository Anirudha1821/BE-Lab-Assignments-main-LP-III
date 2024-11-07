#include<bits/stdc++.h>
using namespace std;

struct Item {
  int weight;
  int profit;
};

// The IDEA is to decide, for each item and for each capacity, whether to include the item in the knapsack or exclude it

// dp[i][w] represents the maximum profit that can be obtained using the first i items (from item 1 to item i) with a knapsack capacity of w.
int knapsack(int W, vector<Item> &items) {
  int n = items.size();
  vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

  for (int i = 1; i <= n; i++) {
    for (int w = 1; w <= W; w++) {
      // If the current item's weight is less than or equal to the current capacity

      //curr item = (i-1)...not i as we are looping till n
      if (items[i - 1].weight <= w) {
        //PICK -> max between take or not-take
        dp[i][w] = max(dp[i - 1][w],dp[i - 1][w - items[i - 1].weight] + items[i - 1].profit);
      } else {//NOT-PICK
        // current item's weight is more than the current capacity, then skip
        dp[i][w] = dp[i - 1][w];
      }
    }
  }

  return dp[n][W];
}

int main() {
  int W = 50;                                            // Knapsack capacity
  vector<Item> items = {{10, 60}, {20, 100}, {30, 120}}; // {weight, profit}

  int max_value = knapsack(W, items);
  cout << "Maximum profit: " << max_value << endl;

  return 0;
}