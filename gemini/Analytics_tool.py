import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.displot(np.random.randn(100))  # Generate random data and create a distribution plot
plt.show()
# Load data
df = pd.read_csv('Quert Dataset.xlsx')

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Exploratory Data Analysis
print(df.describe())
sns.pairplot(df)
plt.show()

# Feature Engineering
df['new_feature'] = df['feature1'] * df['feature2']

# Model Building (Example: Linear Regression)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print('Mean Squared Error:', np.mean((y_test - y_pred) ** 2))