"""
Test suite for Al Amin's AI/ML Utilities
"""

import pytest
import numpy as np
import pandas as pd
from main import DataProcessor, MLHelper


class TestDataProcessor:
    """Test cases for DataProcessor class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.processor = DataProcessor()
        self.sample_data = pd.DataFrame({
            'A': [1, 2, 2, 4, 5],
            'B': [1, np.nan, 3, 4, 5],
            'C': ['a', 'b', 'b', 'd', 'e']
        })
    
    def test_processor_initialization(self):
        """Test processor initialization."""
        assert self.processor.name == "Al Amin's Data Processor"
        assert self.processor.version == "1.0.0"
    
    def test_clean_data_removes_duplicates(self):
        """Test that clean_data removes duplicate rows."""
        cleaned = self.processor.clean_data(self.sample_data)
        assert len(cleaned) == 4  # One duplicate should be removed
    
    def test_feature_stats(self):
        """Test feature statistics generation."""
        stats = self.processor.feature_stats(self.sample_data)
        
        assert 'shape' in stats
        assert 'columns' in stats
        assert 'missing_values' in stats
        assert 'data_types' in stats
        
        assert stats['shape'] == (5, 3)
        assert 'A' in stats['columns']
        assert 'B' in stats['columns']
        assert 'C' in stats['columns']


class TestMLHelper:
    """Test cases for MLHelper class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        np.random.seed(42)  # For reproducible tests
        self.X = np.random.randn(100, 2)
        self.y = np.random.randint(0, 2, 100)
    
    def test_train_test_split_custom(self):
        """Test custom train-test split."""
        X_train, X_test, y_train, y_test = MLHelper.train_test_split_custom(
            self.X, self.y, test_size=0.2
        )
        
        assert len(X_train) == 80
        assert len(X_test) == 20
        assert len(y_train) == 80
        assert len(y_test) == 20
        
        # Check that all samples are accounted for
        assert len(X_train) + len(X_test) == len(self.X)
        assert len(y_train) + len(y_test) == len(self.y)
    
    def test_accuracy_score(self):
        """Test accuracy score calculation."""
        y_true = np.array([1, 0, 1, 1, 0])
        y_pred = np.array([1, 0, 1, 0, 0])
        
        accuracy = MLHelper.accuracy_score(y_true, y_pred)
        assert accuracy == 0.8  # 4 out of 5 correct
    
    def test_accuracy_score_perfect(self):
        """Test accuracy score with perfect predictions."""
        y_true = np.array([1, 0, 1, 1, 0])
        y_pred = np.array([1, 0, 1, 1, 0])
        
        accuracy = MLHelper.accuracy_score(y_true, y_pred)
        assert accuracy == 1.0


def test_main_function():
    """Test the main function runs without errors."""
    from main import main
    
    result = main()
    assert result == "Success! 🎉"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
