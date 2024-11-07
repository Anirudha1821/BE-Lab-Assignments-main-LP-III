import pandas as pd

# Load dataset with a different encoding
df = pd.read_csv('../ML/5-sales_data_sample.csv', encoding ="unicode_escape")

print(df.head())

# Drop rows with missing values (optional)
df_cleaned = df.dropna()

# Select numerical columns for clustering
# Assume we are clustering based on 'SALES', 'QUANTITYORDERED', 'PRICEEACH'
X = df_cleaned[['SALES', 'QUANTITYORDERED', 'PRICEEACH']]

# Normalize the data (optional, but recommended for K-Means)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# ---------------------------------

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Elbow method to find optimal number of clusters
inertia = []
K = range(1, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 6))
plt.plot(K, inertia)
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# Choose k based on elbow point (e.g., k=3)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df_cleaned['Cluster'] = kmeans.fit_predict(X_scaled)

# Check cluster assignments
print(df_cleaned[['SALES', 'QUANTITYORDERED', 'PRICEEACH', 'Cluster']])

# The "elbow" point is where the WCSS begins to decrease at a slower rate as you increase the number of clusters. This point indicates the optimal number of clusters.
# Before the elbow, adding more clusters significantly reduces the WCSS, but after the elbow, the reduction becomes smaller.

# Within-Cluster Sum of Squares (WCSS)

# for standardizing numerical features, which means it scales the data so that each feature has a mean of 0 and a standard deviation of 1
# WHY-> reduce the influence of features with larger numeric ranges and help the model learn more effectively.

# inertia_ is an attribute of the K-Means model that measures how compact the clusters are, calculated as the sum of squared distances between each data point and its nearest cluster centroid.

# By setting df['Cluster'] =, we store these cluster labels in a new column called 'Cluster' in the original DataFrame (df). Each row now has a label indicating which cluster that particular data point belongs to.



