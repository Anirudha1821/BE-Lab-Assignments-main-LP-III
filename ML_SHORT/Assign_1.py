import numpy as np          
import pandas as pd           
import seaborn as sns               
import matplotlib.pyplot as plt        
from sklearn.preprocessing import StandardScaler 

# Load dataset
df = pd.read_csv("uber.csv")       
df.head()

# Drop columns that are not needed for the analysis
# axis=1 means drop columns 
df = df.drop(['Unnamed: 0', 'key', 'pickup_datetime'], axis=1)

# Check for missing values
df.isnull().sum()                      # Display count of missing values in each column

# Fill NaN values with the mean of each column
# df = df.fillna(df.mean())

# Remove rows with missing values
df = df.dropna()                       # Drop rows with any NaN values

# Plot a boxplot to identify outliers
plt.figure(figsize=(10, 6))            # Set the plot size
sns.boxplot(data=df)                   # Create boxplots for each feature in the DataFrame
plt.show()                             # Display the boxplot

# Remove outliers using the Interquartile Range (IQR) method
for col in df.columns:                 # Iterate over each column
    Q1 = df[col].quantile(0.25)        # First quartile (25th percentile)
    Q3 = df[col].quantile(0.75)        # Third quartile (75th percentile)
    IQR = Q3 - Q1                      # Calculate the Interquartile Range (IQR)
    
    lb = Q1 - 1.5 * IQR                # Define the lower bound for outliers
    ub = Q3 + 1.5 * IQR                # Define the upper bound for outliers
    
    df = df[(df[col] >= lb) & (df[col] <= ub)]  # Remove rows outside the bounds

# Scale the data..feature scaling 
# ensures that all features contribute equally to the model 
# scale the data so that each feature has a mean of 0 and a standard deviation of 1.

scaler = StandardScaler()              # Initialize the StandardScaler for normalization
scaled_df = scaler.fit_transform(df)   # Scale the DataFrame
# ----------------------------------------------------
# Display a heatmap of correlations between features
sns.heatmap(data=df.corr(), annot=True)  # Plot the correlation heatmap with annotations
plt.show()                               # Display the heatmap

# Import additional libraries for model training and evaluation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Define features (X) and target (Y) for the regression model
X = df[["pickup_longitude", "pickup_latitude", "dropoff_longitude", "dropoff_latitude", "passenger_count"]]
Y = df["fare_amount"]

# Split data into training and testing sets (70% train, 30% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

# Train a linear regression model
model = LinearRegression()             # Initialize the Linear Regression model
model.fit(X_train, Y_train)            # Fit the model on the training data

# Predict on the test set
y_pred = model.predict(X_test)         # Predict fare amounts for the test set

# Evaluate the linear regression model
r2score = r2_score(Y_test, y_pred)     # Calculate the R2 score
print("R2 Score: ", r2score)           # Print R2 score
rmse = np.sqrt(mean_squared_error(Y_test, y_pred))  # Calculate Root Mean Square Error

# ----------------------------------------------------------
# Train a Random Forest Regressor for comparison
from sklearn.ensemble import RandomForestRegressor
# => multiple decesion trees 
model1 = RandomForestRegressor()       # Initialize the Random Forest Regressor
model1.fit(X_train, Y_train)           # Fit the model on the training data

# Predict on the test set with Random Forest
y_pred = model1.predict(X_test)        # Predict fare amounts for the test set

# Evaluate the Random Forest Regressor
r2score = r2_score(Y_test, y_pred)     # Calculate the R2 score
rmse = np.sqrt(mean_squared_error(Y_test, y_pred))  # Calculate Root Mean Square Error
