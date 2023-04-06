import json
from typing import List, Dict
import pandas as pd
from pytrends.request import TrendReq
from pytrendsplus.visualization import visualize_line_chart
from pytrendsplus.suggestions import get_suggestions
from pytrendsplus.prediction import predict_trends
from selenium import webdriver
import time


# get_cookie fixes issues with Google 429 error when fetching trends.
def get_cookie():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://trends.google.com/")
    time.sleep(5)
    cookie = driver.get_cookie("NID")["value"]
    driver.quit()
    return cookie


nid_cookie = f"NID={get_cookie()}"


class PyTrendsPlus:
    def __init__(self):
        self.pytrends = TrendReq(requests_args={"headers": {"Cookie": nid_cookie}})

    def fetch_data(self, keywords: List[str], time_range: str = "all") -> pd.DataFrame:
        """
        Fetch Google Trends data for the given keywords and time range.

        Args:
            keywords: A list of keywords to fetch data for.
            time_range: The time range for the data. Default is 'all'.

        Returns:
            A DataFrame containing the Google Trends data.
        """
        if not keywords:
            raise ValueError("Keywords must be a non-empty list.")
        self.pytrends.build_payload(keywords, timeframe=time_range)
        try:
            data = self.pytrends.interest_over_time()
        except Exception as e:
            raise ValueError(f"Invalid time range: {time_range}. Error: {str(e)}")
        if data.empty:
            raise ValueError("No data found for the given keywords and time range.")
        return data

    def plot_line_chart(self, data: pd.DataFrame, title: str = None) -> None:
        """
        Visualize the Google Trends data as a line chart.

        Args:
            data: A DataFrame containing the Google Trends data.
            title: The title for the chart. Default is None.

        Returns:
            None
        """
        visualize_line_chart(data, title)

    def get_suggestions(self, keyword: str) -> List[str]:
        """
        Get keyword suggestions based on the given keyword.

        Args:
            keyword: The input keyword.

        Returns:
            A list of suggested keywords related to the input keyword.
        """
        return get_suggestions(keyword)

    def predict_trends(self, data: pd.DataFrame) -> Dict[str, float]:
        """
        Predict future trends based on historical data.

        Args:
            data: A DataFrame containing the Google Trends data.

        Returns:
            A dictionary with the predicted trends for each keyword.
        """
        return predict_trends(data)

    def export_data(self, data: pd.DataFrame, file_name: str) -> None:
        """
        Export the Google Trends data to a file.

        Args:
            data: A DataFrame containing the Google Trends data.
            file_name: The name of the file to export the data to.

        Returns:
            None
        """
        file_extension = file_name.split(".")[-1].lower()

        if file_extension == "csv":
            data.to_csv(file_name)
        elif file_extension == "json":
            with open(file_name, "w") as f:
                # Convert Timestamp objects to strings for inner dictionaries
                json_data = data.to_dict()
                json_data = {
                    key: {
                        str(inner_key): value for inner_key, value in inner_dict.items()
                    }
                    for key, inner_dict in json_data.items()
                }
                json.dump(json_data, f)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
