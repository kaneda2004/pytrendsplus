import matplotlib.pyplot as plt
import pandas as pd


def visualize_line_chart(data: pd.DataFrame, title: str = None) -> None:
    """
    Visualize the Google Trends data as a line chart.

    Args:
        data: A DataFrame containing the Google Trends data.
        title: The title for the chart. Default is None.

    Returns:
        None
    """
    if not isinstance(data, pd.DataFrame) or data.empty:
        raise ValueError("Data must be a non-empty DataFrame.")
    data.plot(kind="line", figsize=(10, 6))
    plt.xlabel("Date")
    plt.ylabel("Trends Interest")

    if title:
        plt.title(title)
    else:
        plt.title("Google Trends Interest Over Time")
    plt.legend(title="Keywords", loc="upper left")
    plt.grid()
    plt.show()
