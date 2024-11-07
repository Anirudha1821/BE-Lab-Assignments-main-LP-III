#include <bits/stdc++.h>
using namespace std;

struct Item {
  int weight;
  int value;
  double ratio; // value per unit weight
};

// Structure to represent a node in the branch and bound tree
struct Node {
    int level;   // Level in the decision tree (which item we're considering)
    int profit;  // Profit accumulated so far
    int weight;  // Weight accumulated so far
    double bound; // Upper bound of possible maximum profit
};

// Function to sort items based on their value/weight ratio
bool compareItems(Item a, Item b) {
    return a.ratio > b.ratio;  // Sort in descending order of ratio
}

// Function to calculate the upper bound using a greedy approach
double upperBound(Node u, int n, int W, const vector<Item>& items) {
    if (u.weight >= W) {
        return 0;  // If weight exceeds capacity, no further profit can be made
    }
    
    double profitBound = u.profit;
    int j = u.level + 1;
    int totalWeight = u.weight;

    // Add as many items as possible from this point on without exceeding capacity
    while (j < n && totalWeight + items[j].weight <= W) {
        totalWeight += items[j].weight;
        profitBound += items[j].value;
        j++;
    }

    // If there is still capacity left, take a fractional part of the next item
    if (j < n) {
        profitBound += (W - totalWeight) * items[j].ratio;
    }

    return profitBound;  // Return the upper bound
}

int knapsack(int W, vector<Item>& items) {
  int n = items.size();
  sort(items.begin(), items.end(), compareItems); // Sort items by value-to-weight ratio.

  queue<Node> Q; // Queue to explore the nodes.
  Node u, v;
  // u = current node, v = child node
  u = {-1, 0, 0, 0}; // Start with an empty node (before the first item).
  Q.push(u);

  int maxProfit = 0;

  while (!Q.empty()) {
    u = Q.front();
    Q.pop();

    if (u.level == -1) {
      v.level = 0; // Start considering the first item (level 0).
    }

    if (u.level == n - 1) {
      continue; // If we have considered all items, stop.
    }

    v.level = u.level + 1; // Move to the next item.

    // Option 1: Include the item at index v.level.
    v.weight = u.weight + items[v.level].weight;
    v.profit = u.profit + items[v.level].value;

    // If the new weight doesn't exceed the capacity and the profit is better, update maxProfit.
    if (v.weight <= W && v.profit > maxProfit)
        maxProfit = v.profit;

    v.bound = upperBound(v, n, W, items);  // Calculate the upper bound for this branch.

    // If the bound is greater than the current maxProfit, push this node to the queue.
    // OTHERWISE PRUNE
    if (v.bound > maxProfit)
        Q.push(v);

    // Option 2: Don't include the item at index v.level.
    v.weight = u.weight;
    v.profit = u.profit;
    v.bound = upperBound(v, n, W, items);

    // If the bound is greater than the current maxProfit, push this node to the queue.
    // OTHERWISE PRUNE
    if (v.bound > maxProfit)
        Q.push(v);
  }

  return maxProfit;
}

int main() {
  int W = 50; // Knapsack capacity
  vector<Item> items = {
      {10, 60, 6}, {20, 100, 5}, {30, 120, 4}}; // {weight, value, ratio}

  // Calculate value-to-weight ratio for each item
  for (auto &item : items) {
    item.ratio = static_cast<double>(item.value) / item.weight;
  }

  int max_value = knapsack(W, items);
  cout << "Maximum value: " << max_value << endl;

  return 0;
}
