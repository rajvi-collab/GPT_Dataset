import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class AnalyticsTool:
    def __init__(self, data):
        """
        Initialize the AnalyticsTool with a Pandas DataFrame.

        Args:
            data (pd.DataFrame): Input dataset.
        """
        self.data = data

    def data_summary(self):
        """
        Generate a summary of the dataset.

        Returns:
            dict: Summary statistics.
        """
        summary = {
            "count": self.data.count(),
            "mean": self.data.mean(),
            "std": self.data.std(),
            "min": self.data.min(),
            "25%": self.data.quantile(0.25),
            "50%": self.data.quantile(0.5),
            "75%": self.data.quantile(0.75),
            "max": self.data.max(),
        }
        return pd.DataFrame(summary).T

    def correlation_analysis(self):
        """
        Perform correlation analysis on the dataset.

        Returns:
            pd.DataFrame: Correlation matrix.
        """
        return self.data.corr()

    def visualize_distribution(self, column):
        """
        Visualize the distribution of a specific column.

        Args:
            column (str): Column name.
        """
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data[column], kde=True)
        plt.title(f"Distribution of {column}")
        plt.show()

    def visualize_relationship(self, column1, column2):
        """
        Visualize the relationship between two columns.

        Args:
            column1 (str): First column name.
            column2 (str): Second column name.
        """
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=self.data[column1], y=self.data[column2])
        plt.title(f"Relationship between {column1} and {column2}")
        plt.show()


# Example usage
if __name__ == "__main__":
    # Load sample dataset
    data = pd.DataFrame(
        {
            "Age": [25, 30, 28, 35, 40, 38, 32, 45, 50],
            "Income": [50000, 60000, 55000, 70000, 80000, 75000, 65000, 90000, 100000],
            "Expenses": [20000, 25000, 22000, 30000, 35000, 32000, 28000, 40000, 45000],
        }
    )

    # Create AnalyticsTool instance
    analytics = AnalyticsTool(data)

    # Generate data summary
    summary = analytics.data_summary()
    print("Data Summary:")
    print(summary)

    # Perform correlation analysis
    correlation = analytics.correlation_analysis()
    print("\nCorrelation Matrix:")
    print(correlation)

    # Visualize distribution of Age
    analytics.visualize_distribution("Age")

    # Visualize relationship between Income and Expenses
    analytics.visualize_relationship("Income", "Expenses")
