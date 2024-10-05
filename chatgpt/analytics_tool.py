import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class AnalyticsTool:
    def __init__(self, file_path, file_type='csv', chunk_size=None):
        """
        Initialize the Analytics Tool with the dataset.
        
        :param file_path: Path to the dataset (csv, excel, etc.).
        :param file_type: Type of file ('csv', 'excel', etc.).
        :param chunk_size: If specified, process the dataset in chunks.
        """
        self.file_path = file_path
        self.file_type = file_type
        self.chunk_size = chunk_size
        self.data = None
    
    def load_data(self):
        """
        Load the dataset into memory. If chunk_size is provided, it loads in chunks.
        """
        if self.file_type == 'csv':
            if self.chunk_size:
                self.data = pd.read_csv(self.file_path, chunksize=self.chunk_size)
            else:
                self.data = pd.read_csv(self.file_path)
        elif self.file_type == 'excel':
            self.data = pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file type. Supported: 'csv', 'excel'")
    
    def preprocess_data(self):
        """
        Perform basic data cleaning such as handling missing values and standardizing columns.
        """
        if isinstance(self.data, pd.DataFrame):
            # Remove rows with any missing values
            self.data = self.data.dropna()
            # Remove duplicates
            self.data = self.data.drop_duplicates()
            # Standardize column names (lowercase and replace spaces with underscores)
            self.data.columns = [col.lower().replace(' ', '_') for col in self.data.columns]
        else:
            print("Data is not loaded yet or is being processed in chunks.")
    
    def descriptive_stats(self):
        """
        Compute and return descriptive statistics of the dataset.
        """
        if isinstance(self.data, pd.DataFrame):
            return self.data.describe()
        else:
            print("Data is not available for descriptive statistics.")
    
    def correlation_analysis(self):
        """
        Perform correlation analysis on numerical features in the dataset.
        """
        if isinstance(self.data, pd.DataFrame):
            correlations = self.data.corr()
            sns.heatmap(correlations, annot=True, cmap='coolwarm')
            plt.title("Correlation Matrix")
            plt.show()
        else:
            print("Data is not available for correlation analysis.")
    
    def rolling_average(self, column_name, window_size=5):
        """
        Calculate rolling average for a specific column over a given window size.
        
        :param column_name: The column to calculate rolling average for.
        :param window_size: Window size for the rolling average.
        """
        if isinstance(self.data, pd.DataFrame):
            if column_name in self.data.columns:
                self.data[f'rolling_avg_{column_name}'] = self.data[column_name].rolling(window=window_size).mean()
            else:
                print(f"Column '{column_name}' not found in the dataset.")
        else:
            print("Data is not available for rolling average.")
    
    def visualize_trends(self, column_name):
        """
        Visualize trends in a specific column (e.g., line plot).
        
        :param column_name: The column to visualize.
        """
        if isinstance(self.data, pd.DataFrame):
            if column_name in self.data.columns:
                plt.figure(figsize=(10, 6))
                plt.plot(self.data[column_name], label=column_name)
                plt.title(f"Trend of {column_name}")
                plt.xlabel("Index")
                plt.ylabel(column_name)
                plt.legend()
                plt.show()
            else:
                print(f"Column '{column_name}' not found in the dataset.")
        else:
            print("Data is not available for visualization.")

    def generate_report(self, output_file='report.csv'):
        """
        Generate a report of the processed data and save it as a CSV.
        """
        if isinstance(self.data, pd.DataFrame):
            self.data.to_csv(output_file, index=False)
            print(f"Report saved to {output_file}")
        else:
            print("Data is not available to generate a report.")

# Example usage (assuming the dataset is loaded as a CSV file):
tool = AnalyticsTool('large_dataset.csv')
tool.load_data()
tool.preprocess_data()
print(tool.descriptive_stats())
tool.correlation_analysis()
tool.rolling_average('some_column')
tool.visualize_trends('some_column')
tool.generate_report('final_report.csv')
