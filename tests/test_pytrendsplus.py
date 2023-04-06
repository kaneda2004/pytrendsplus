import unittest
import time
import pandas as pd
from unittest.mock import patch
from pytrendsplus import PyTrendsPlus
from pytrendsplus.visualization import visualize_line_chart
from pytrendsplus.suggestions import get_suggestions
from pytrendsplus.prediction import predict_trends


class TestPyTrendsPlus(unittest.TestCase):
    def setUp(self):
        self.trends = PyTrendsPlus()
        self.keywords = ["Python", "JavaScript"]
        self.time_range = "2020-01-01 2020-02-01"  # Use a smaller time range
        time.sleep(1)  # Add a delay between requests
        self.data = self.trends.fetch_data(self.keywords, self.time_range)

    # Existing tests...

    def test_visualize_line_chart(self):
        with patch("pytrendsplus.visualization.plt.show") as mock_show:
            visualize_line_chart(self.data)
            mock_show.assert_called_once()

    def test_visualize_line_chart_empty_data(self):
        with self.assertRaises(ValueError):
            visualize_line_chart(pd.DataFrame())

    def test_get_suggestions(self):
        keyword = "Python"
        time.sleep(1)  # Add a delay between requests
        suggestions = get_suggestions(keyword)
        self.assertIsInstance(suggestions, list)
        self.assertTrue(len(suggestions) > 0)

    def test_get_suggestions_empty_keyword(self):
        with self.assertRaises(ValueError):
            get_suggestions("")

    def test_predict_trends(self):
        predictions = predict_trends(self.data)
        self.assertIsInstance(predictions, dict)
        self.assertTrue(set(self.keywords).issubset(predictions.keys()))

    def test_predict_trends_empty_data(self):
        with self.assertRaises(ValueError):
            predict_trends(pd.DataFrame())


if __name__ == "__main__":
    unittest.main()
