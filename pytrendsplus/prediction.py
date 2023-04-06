import numpy as np
import pandas as pd
from typing import Dict
from sklearn.linear_model import LinearRegression


def predict_trends(data: pd.DataFrame) -> Dict[str, float]:
    """
    Predict future trends based on historical data.

    Args:
        data: A DataFrame containing the Google Trends data.

    Returns:
        A dictionary with the predicted trends for each keyword.
    """
    if not isinstance(data, pd.DataFrame) or data.empty:
        raise ValueError("Data must be a non-empty DataFrame.")
    predictions = {}
    for keyword in data.columns[:-1]:  # Exclude the 'isPartial' column
        X = np.arange(len(data)).reshape(-1, 1)
        y = data[keyword].values
        model = LinearRegression()
        model.fit(X, y)
        future_X = np.array([len(data)]).reshape(-1, 1)
        prediction = model.predict(future_X)
        predictions[keyword] = prediction[0]
    return predictions
