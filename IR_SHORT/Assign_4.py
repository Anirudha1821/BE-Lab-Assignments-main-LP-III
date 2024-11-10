from collections import defaultdict

# Map function
def map_function(data):
    map_output = []#list
    for item in data:
        map_output.append((item, 1))  # Emit key-value pair
    return map_output

# Reduce function
def reduce_function(mapped_data):
    reduce_output = defaultdict(int)
    for key, value in mapped_data:
        reduce_output[key] += value  # Aggregate values by key
    return dict(reduce_output)

# Example data
data = ["apple", "banana", "apple", "apple", "banana", "cherry"]

# Step 1: Map step
mapped_data = map_function(data)

# Step 2: Reduce step
reduced_data = reduce_function(mapped_data)

# Final result
print(reduced_data)