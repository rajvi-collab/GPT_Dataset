import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Data Ingestion
def ingest_data(file_path):
    """
    Ingest data from CSV file.

    Args:
        file_path (str): Path to CSV file.

    Returns:
        pd.DataFrame: Ingested data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
         print(f"Error ingesting data: {e}")
         return None

# Data Processing
def process_data(data):
    """
    Clean and preprocess data.

    Args:
        data (pd.DataFrame): Ingested data.

    Returns:
        pd.DataFrame: Processed data.
    """
    # Handle missing values
    data.fillna(data.mean(), inplace=True)

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    # Encode categorical variables
    categorical_cols = data.select_dtypes(include=['object']).columns
    data[categorical_cols] = data[categorical_cols].apply(lambda x: pd.Categorical(x).codes)

    return data
# Data Analysis
def analyze_data(data):
    """
    Perform regression analysis.

    Args:
        data (pd.DataFrame): Processed data.

    Returns:
        dict: Analysis results.
    """
    # Split data into training and testing sets
    X = data.drop('target', axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate model performance
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    return {'model': model, 'mse': mse}

# Data Visualization
def visualize_data(data, analysis_results):
    """
    Visualize data and analysis results.

    Args:
        data (pd.DataFrame): Processed data.
        analysis_results (dict): Analysis results.
    """
    # Plot data distribution
    sns.distplot(data['target'])
    plt.title('Target Variable Distribution')
    plt.show()

    # Plot predicted vs. actual values
    plt.scatter(analysis_results['y_test'], analysis_results['y_pred'])
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Predicted vs. Actual Values')
    plt.show()
# Insight Generation
def generate_insights(analysis_results):
    """
    Generate insights from analysis results.

    Args:
        analysis_results (dict): Analysis results.

    Returns:
        str: Insights.
    """
    insights = f"Model Performance (MSE): {analysis_results['mse']:.2f}\n"
    insights += f"Model Coefficients: {analysis_results['model'].coef_}\n"
    return insights

# Example Usage
if __name__ == "__main__":
    file_path = 'data/data.csv'
    data = ingest_data(file_path)
    processed_data = process_data(data)
    analysis_results = analyze_data(processed_data)
    visualize_data(processed_data, analysis_results)
    insights = generate_insights(analysis_results)
    print(insights)