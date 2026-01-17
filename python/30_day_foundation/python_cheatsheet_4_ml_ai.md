# 🤖 Python ML/AI Cheat Sheet
## NumPy, Pandas, Scikit-Learn & PyTorch

---

## 1. NumPy - Numerical Computing

NumPy is the foundation for numerical computing in Python. It provides fast, efficient arrays and mathematical operations.

### Installation & Import
```python
pip install numpy

import numpy as np
```

### Creating Arrays
```python
# From Python lists
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Special arrays
np.zeros((3, 4))            # 3x4 array of zeros
np.ones((2, 3))             # 2x3 array of ones
np.full((2, 2), 7)          # 2x2 array filled with 7
np.eye(3)                   # 3x3 identity matrix
np.empty((2, 3))            # Uninitialized array

# Range arrays
np.arange(0, 10, 2)         # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)        # [0, 0.25, 0.5, 0.75, 1.0]

# Random arrays
np.random.rand(3, 4)        # Random floats [0, 1)
np.random.randn(3, 4)       # Random from normal distribution
np.random.randint(0, 10, (3, 4))  # Random integers
np.random.choice([1, 2, 3], size=5)  # Random from list
np.random.seed(42)          # Set seed for reproducibility
```

### Array Properties
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape           # (2, 3) - dimensions
arr.ndim            # 2 - number of dimensions
arr.size            # 6 - total elements
arr.dtype           # int64 - data type
arr.itemsize        # 8 - bytes per element
```

### Array Operations
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
a + b               # [5, 7, 9]
a - b               # [-3, -3, -3]
a * b               # [4, 10, 18]
a / b               # [0.25, 0.4, 0.5]
a ** 2              # [1, 4, 9]
np.sqrt(a)          # [1.0, 1.414, 1.732]

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A @ B               # Matrix multiplication (Python 3.5+)
np.dot(A, B)        # Matrix multiplication
A.T                 # Transpose
np.linalg.inv(A)    # Inverse
np.linalg.det(A)    # Determinant
```

### Indexing & Slicing
```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr[0]              # [1, 2, 3] - first row
arr[0, 1]           # 2 - element at (0, 1)
arr[:, 0]           # [1, 4, 7] - first column
arr[0:2, 1:3]       # [[2, 3], [5, 6]] - slice
arr[arr > 5]        # [6, 7, 8, 9] - boolean indexing
```

### Reshaping & Stacking
```python
arr = np.arange(12)

arr.reshape(3, 4)       # Reshape to 3x4
arr.reshape(3, -1)      # -1 = infer dimension
arr.flatten()           # To 1D array
arr.ravel()             # To 1D (view when possible)

# Stacking
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.vstack([a, b])       # Vertical stack: [[1,2,3], [4,5,6]]
np.hstack([a, b])       # Horizontal stack: [1,2,3,4,5,6]
np.concatenate([a, b])  # Along axis
```

### Aggregation Functions
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

np.sum(arr)             # 21 (all elements)
np.sum(arr, axis=0)     # [5, 7, 9] (column sums)
np.sum(arr, axis=1)     # [6, 15] (row sums)

np.mean(arr)            # Mean
np.std(arr)             # Standard deviation
np.var(arr)             # Variance
np.min(arr), np.max(arr)
np.argmin(arr), np.argmax(arr)  # Index of min/max
```

---

## 2. Pandas - Data Analysis

Pandas provides DataFrames for handling tabular data efficiently.

### Installation & Import
```python
pip install pandas

import pandas as pd
```

### Creating DataFrames
```python
# From dictionary
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
})

# From list of dicts
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30}
]
df = pd.DataFrame(data)

# From NumPy array
arr = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(arr, columns=['A', 'B'])

# From CSV/Excel
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
df = pd.read_json('data.json')
```

### Exploring Data
```python
df.head()               # First 5 rows
df.tail(10)             # Last 10 rows
df.shape                # (rows, columns)
df.columns              # Column names
df.dtypes               # Data types
df.info()               # Summary info
df.describe()           # Statistical summary

df.isnull().sum()       # Count nulls per column
df.nunique()            # Unique values per column
df['col'].value_counts()  # Value counts
```

### Selecting Data
```python
# Single column (returns Series)
df['name']
df.name

# Multiple columns (returns DataFrame)
df[['name', 'age']]

# Rows by index
df.iloc[0]              # First row by position
df.iloc[0:3]            # Rows 0-2
df.iloc[0, 1]           # Element at row 0, col 1

# Rows by label
df.loc[0]               # Row with index 0
df.loc[0:2, 'name']     # Rows 0-2, 'name' column

# Conditional selection
df[df['age'] > 25]
df[(df['age'] > 25) & (df['city'] == 'NYC')]
df[df['name'].isin(['Alice', 'Bob'])]
df.query('age > 25 and city == "NYC"')
```

### Modifying Data
```python
# Add column
df['new_col'] = [1, 2, 3]
df['age_plus_10'] = df['age'] + 10

# Modify column
df['age'] = df['age'] * 2

# Rename columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Drop columns/rows
df.drop('col', axis=1, inplace=True)       # Drop column
df.drop([0, 1], axis=0, inplace=True)      # Drop rows

# Fill missing values
df.fillna(0, inplace=True)
df.fillna(df.mean(), inplace=True)
df.dropna(inplace=True)                     # Drop rows with NaN

# Replace values
df.replace({'old': 'new'}, inplace=True)

# Apply function
df['age'] = df['age'].apply(lambda x: x * 2)
df['name'] = df['name'].str.upper()
```

### Grouping & Aggregation
```python
# Group by single column
df.groupby('city').mean()
df.groupby('city')['age'].sum()

# Group by multiple columns
df.groupby(['city', 'gender']).agg({
    'age': 'mean',
    'salary': ['min', 'max', 'sum']
})

# Custom aggregation
df.groupby('city').agg(
    avg_age=('age', 'mean'),
    max_salary=('salary', 'max'),
    count=('name', 'count')
)

# Pivot tables
pd.pivot_table(df, values='sales', index='month', 
               columns='product', aggfunc='sum')
```

### Merging & Joining
```python
# Merge (like SQL JOIN)
pd.merge(df1, df2, on='key')                    # Inner join
pd.merge(df1, df2, on='key', how='left')        # Left join
pd.merge(df1, df2, on='key', how='outer')       # Outer join
pd.merge(df1, df2, left_on='a', right_on='b')   # Different column names

# Concatenate
pd.concat([df1, df2])                           # Stack vertically
pd.concat([df1, df2], axis=1)                   # Stack horizontally
```

### Saving Data
```python
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
df.to_json('output.json')
```

---

## 3. Scikit-Learn - Machine Learning

Scikit-learn provides simple tools for machine learning.

### Installation & Import
```python
pip install scikit-learn

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_squared_error
```

### Standard ML Workflow
```python
# 1. Load & prepare data
from sklearn.datasets import load_iris
data = load_iris()
X = data.data           # Features
y = data.target         # Labels

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Scale features (often important!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 5. Predict & evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2%}")
```

### Common Preprocessing

```python
from sklearn.preprocessing import (
    StandardScaler,     # Standardize features (mean=0, std=1)
    MinMaxScaler,       # Scale to range [0, 1]
    LabelEncoder,       # Encode labels to integers
    OneHotEncoder,      # One-hot encode categories
)
from sklearn.impute import SimpleImputer

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Min-Max scaling
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Label encoding
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# One-hot encoding
ohe = OneHotEncoder(sparse=False)
X_encoded = ohe.fit_transform(X[['category_column']])

# Handle missing values
imputer = SimpleImputer(strategy='mean')  # or 'median', 'most_frequent'
X_imputed = imputer.fit_transform(X)
```

### Classification Models
```python
# Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)  # Probabilities

# Random Forest
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=10)

# Support Vector Machine
from sklearn.svm import SVC
model = SVC(kernel='rbf', C=1.0)

# K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)

# Gradient Boosting
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
```

### Regression Models
```python
# Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100)

# Ridge & Lasso (regularized)
from sklearn.linear_model import Ridge, Lasso
model = Ridge(alpha=1.0)
model = Lasso(alpha=1.0)
```

### Evaluation Metrics
```python
# Classification
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
roc_auc = roc_auc_score(y_test, y_proba[:, 1])

# Regression
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
)

mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

### Cross-Validation & Hyperparameter Tuning
```python
from sklearn.model_selection import (
    cross_val_score,
    GridSearchCV,
    RandomizedSearchCV,
)

# Cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"CV Scores: {scores.mean():.3f} (+/- {scores.std():.3f})")

# Grid Search
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 20, None],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.3f}")
best_model = grid_search.best_estimator_
```

### Pipelines
```python
from sklearn.pipeline import Pipeline

# Create pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

# Fit and predict
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Use in GridSearchCV
param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [5, 10]
}
grid_search = GridSearchCV(pipeline, param_grid, cv=5)
```

---

## 4. PyTorch - Deep Learning

PyTorch is a deep learning framework with dynamic computation graphs.

### Installation & Import
```python
pip install torch torchvision

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
```

### Tensors (like NumPy arrays, but with GPU support)
```python
# Create tensors
t = torch.tensor([1, 2, 3])
t = torch.zeros(3, 4)
t = torch.ones(3, 4)
t = torch.rand(3, 4)            # Random [0, 1)
t = torch.randn(3, 4)           # Random normal
t = torch.arange(0, 10, 2)      # [0, 2, 4, 6, 8]

# From NumPy
arr = np.array([1, 2, 3])
t = torch.from_numpy(arr)
arr = t.numpy()                 # Back to NumPy

# Properties
t.shape                         # Size
t.dtype                         # Data type
t.device                        # CPU or GPU

# GPU operations
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
t = t.to(device)
```

### Tensor Operations
```python
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Element-wise
a + b, a - b, a * b, a / b
torch.sqrt(a)
torch.exp(a)

# Matrix operations
a @ b                           # Matrix multiplication
torch.matmul(a, b)
a.T                             # Transpose
torch.inverse(a)                # Inverse

# Aggregations
torch.sum(a), torch.mean(a)
torch.max(a), torch.min(a)
torch.argmax(a), torch.argmin(a)

# Reshaping
a.view(4)                       # Reshape to 1D
a.view(-1)                      # Flatten
a.unsqueeze(0)                  # Add dimension
a.squeeze()                     # Remove dimensions of size 1
```

### Building Neural Networks
```python
import torch.nn as nn
import torch.nn.functional as F

# Method 1: Sequential
model = nn.Sequential(
    nn.Linear(784, 256),        # Input layer
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(256, 128),        # Hidden layer
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(128, 10),         # Output layer
)

# Method 2: Custom class (more flexible)
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, num_classes)
        self.dropout = nn.Dropout(0.2)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return x

model = NeuralNet(784, 256, 10)
```

### Training Loop
```python
# Setup
model = NeuralNet(784, 256, 10)
criterion = nn.CrossEntropyLoss()       # Loss function
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Data loaders
train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Training loop
num_epochs = 10
for epoch in range(num_epochs):
    model.train()               # Training mode
    total_loss = 0
    
    for batch_X, batch_y in train_loader:
        # Forward pass
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        
        # Backward pass
        optimizer.zero_grad()   # Clear gradients
        loss.backward()         # Compute gradients
        optimizer.step()        # Update weights
        
        total_loss += loss.item()
    
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {total_loss/len(train_loader):.4f}")

# Evaluation
model.eval()                    # Evaluation mode
with torch.no_grad():           # No gradient computation
    outputs = model(X_test)
    _, predicted = torch.max(outputs, 1)
    accuracy = (predicted == y_test).sum().item() / len(y_test)
    print(f"Accuracy: {accuracy:.2%}")
```

### Common Layers & Activations
```python
# Layers
nn.Linear(in_features, out_features)    # Fully connected
nn.Conv2d(in_channels, out_channels, kernel_size)  # 2D convolution
nn.MaxPool2d(kernel_size)               # Max pooling
nn.BatchNorm1d(num_features)            # Batch normalization
nn.Dropout(p=0.5)                       # Dropout

# Activations
nn.ReLU()
nn.Sigmoid()
nn.Tanh()
nn.Softmax(dim=1)
nn.LeakyReLU(0.1)

# Or functional versions
F.relu(x)
F.softmax(x, dim=1)
```

### CNN Example
```python
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.dropout = nn.Dropout(0.25)
    
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))  # 28x28 -> 14x14
        x = self.pool(F.relu(self.conv2(x)))  # 14x14 -> 7x7
        x = x.view(-1, 64 * 7 * 7)            # Flatten
        x = self.dropout(F.relu(self.fc1(x)))
        x = self.fc2(x)
        return x
```

### Saving & Loading Models
```python
# Save
torch.save(model.state_dict(), 'model.pth')

# Load
model = NeuralNet(784, 256, 10)
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

---

## 💡 Pro Tips

### NumPy
- Use vectorized operations instead of loops—much faster
- Use `np.random.seed()` for reproducible results
- Broadcasting automatically handles shape mismatches

### Pandas
- Use `df.query()` for readable filtering
- Chain methods with `df.pipe()` for cleaner code
- Use `df.memory_usage()` to check memory consumption

### Scikit-Learn
- Always split data before preprocessing (to avoid data leakage)
- Use pipelines to prevent data leakage and simplify deployment
- Use `cross_val_score` instead of a single train/test split

### PyTorch
- Use `model.train()` and `model.eval()` appropriately
- Use `torch.no_grad()` during inference to save memory
- Move data to GPU with `.to(device)` for faster training
- Use `DataLoader` for efficient batching

### General ML Tips
1. **Start simple** - try logistic regression or random forest before deep learning
2. **Always visualize your data** before modeling
3. **Watch for data leakage** - never use test data for training
4. **Feature engineering** often matters more than model choice
5. **Cross-validate** to get reliable performance estimates

---

*Created for W Chats Marketplace*
