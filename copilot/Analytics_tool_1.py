import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chardet

with open('Query Dataset.xlsx', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

# Load the dataset
data = pd.read_csv('Query Dataset.xlsx', encoding=encoding)

# Display basic information about the dataset
print(data.info())

# Handle missing values (if any)
data.fillna(method='ffill', inplace=True)

# Display basic statistics
print(data.describe())

# Calculate correlation matrix
correlation_matrix = data.corr()

# Display the correlation matrix
print(correlation_matrix)


# Plot a histogram of a specific column
data['column_name'].hist(bins=50)
plt.title('Histogram of Column Name')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Plot a scatter plot between two columns
plt.scatter(data['column1'], data['column2'])
plt.title('Scatter Plot between Column1 and Column2')
plt.xlabel('Column1')
plt.ylabel('Column2')
plt.show()


# Identify top 5 most correlated features with a specific column
target_column = 'target_column_name'
correlations = correlation_matrix[target_column].sort_values(ascending=False)
top_5_correlations = correlations.head(6)[1:]  # Exclude the target column itself

print("Top 5 features most correlated with", target_column)
print(top_5_correlations)



# Example output of top 5 correlations
print("Top 5 features most correlated with Sales:")
print(top_5_correlations)
