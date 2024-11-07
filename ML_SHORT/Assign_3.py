import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv('ML/3-Churn_Modelling.csv')
df.head()

# Drop irrelevant columns
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# Convert the categorical variables to numerical values
# LabelEncoder is used to convert categorical values (like Gender and Geography) into numerical values that the model can understand.
label_encoder = LabelEncoder()

# Apply Label Encoding on 'Gender' and 'Geography'
df['Gender'] = label_encoder.fit_transform(df['Gender'])  # Female=0, Male=1
df['Geography'] = label_encoder.fit_transform(df['Geography'])  # France=0, Germany=1, Spain=2
# ----------------------------------------------------------
# Separate the features and the target variables
X = df.drop('Exited', axis = 1) # Features
Y = df['Exited'] # Target

# Split the dataset into training and testing set
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)

# Normalize the dataset
scaler = StandardScaler()
X_train = scaler.fit_transform(x_train)
X_test = scaler.transform(x_test)
# we use only transform on xtest as it uses the same mean and SD learned from the training set

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential()

# an input dimension matching the number of features in X_train.
model.add(Dense(activation='relu', units=32, input_dim=X_train.shape[1]))  # Input layer with more neurons
model.add(Dense(activation='relu', units=16))  # Second hidden layer
model.add(Dense(activation='sigmoid', units=1))  # Output layer for binary classification

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# During training, the cross-entropy loss function exponentially increases the penalty for wrong outputs 
# to drive the weights and biases more aggressively in the right direction.

model.fit(X_train, y_train, batch_size=32, epochs=50)

y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5) # to convert the probabilistic values to True or False


from sklearn.metrics import accuracy_score, confusion_matrix
# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)

# Print confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Print the results
print("Accuracy Score:", accuracy)
print("Confusion Matrix:\n", conf_matrix)


# Why Convert Probabilities to Binary Predictions?:

# Our goal is to classify each customer as either "churn" (1) or "not churn" (0), not as a probability. So, we need to convert these probability values to a straightforward "yes" or "no" decision.
# The Threshold of 0.5:

# We use a threshold of 0.5 to convert these probabilities into binary values:
# If the probability is greater than 0.5, we consider it a prediction of "churn" (1).
# If the probability is less than or equal to 0.5, we consider it a prediction of "not churn" (0).