#!/usr/bin/env python3
"""
Al Amin's AI/ML Utilities
A collection of data science and machine learning utilities.
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Any


class DataProcessor:
    """Simple data processing utilities for AI/ML projects."""
    
    def __init__(self):
        self.name = "Al Amin's Data Processor"
        self.version = "1.0.0"
    
    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Clean and preprocess data."""
        # Remove duplicates
        cleaned = data.drop_duplicates()
        
        # Handle missing values
        cleaned = cleaned.fillna(cleaned.mean(numeric_only=True))
        
        return cleaned
    
    def feature_stats(self, data: pd.DataFrame) -> Dict[str, Any]:
        """Generate feature statistics."""
        return {
            'shape': data.shape,
            'columns': list(data.columns),
            'missing_values': data.isnull().sum().to_dict(),
            'data_types': data.dtypes.to_dict()
        }


class MLHelper:
    """Machine Learning helper functions."""
    
    @staticmethod
    def train_test_split_custom(X: np.ndarray, y: np.ndarray, test_size: float = 0.2):
        """Custom train-test split implementation."""
        n_samples = len(X)
        n_test = int(n_samples * test_size)
        
        # Random indices
        indices = np.random.permutation(n_samples)
        test_indices = indices[:n_test]
        train_indices = indices[n_test:]
        
        return X[train_indices], X[test_indices], y[train_indices], y[test_indices]
    
    @staticmethod
    def accuracy_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Calculate accuracy score."""
        return np.mean(y_true == y_pred)


def main():
    """Main function demonstrating the utilities."""
    print(f"🚀 Welcome to Al Amin's AI/ML Utilities!")
    
    # Create sample data
    data = pd.DataFrame({
        'feature1': np.random.randn(100),
        'feature2': np.random.randn(100),
        'target': np.random.randint(0, 2, 100)
    })
    
    # Initialize processor
    processor = DataProcessor()
    
    # Process data
    cleaned_data = processor.clean_data(data)
    stats = processor.feature_stats(cleaned_data)
    
    print(f"📊 Data shape: {stats['shape']}")
    print(f"📋 Columns: {stats['columns']}")
    print(f"✅ Data processing complete!")
    
    # ML example
    X = cleaned_data[['feature1', 'feature2']].values
    y = cleaned_data['target'].values
    
    X_train, X_test, y_train, y_test = MLHelper.train_test_split_custom(X, y)
    
    print(f"🔬 Training set size: {len(X_train)}")
    print(f"🧪 Test set size: {len(X_test)}")
    
    return "Success! 🎉"


if __name__ == "__main__":
    result = main()
    print(result)
