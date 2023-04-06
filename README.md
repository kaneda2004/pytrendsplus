# PyTrendsPlus 📈📊

A Python library to fetch and analyze Google Trends data with additional functionalities such as data visualization 📊, keyword suggestions 💡, and trend predictions 🔮.

## Installation 🛠️

To install the library, run the following command:



```
pip install pytrendsplus
```

## Configuration

First, you need to import the library and create an instance of the `PyTrendsPlus` class:

```python
from pytrendsplus import PyTrendsPlus

trends = PyTrendsPlus()
```
## Usage

### Fetch Google Trends Data
To fetch Google Trends data for a list of keywords and a specified time range:

```
keywords = ['Python', 'JavaScript']
time_range = '2020-01-01 2020-02-01'
data = trends.fetch_data(keywords, time_range)
```

### Data Visualization
To visualize the fetched data as a line chart:

```
trends.plot_line_chart(data, title='Google Trends Interest Over Time')
```

### Keyword Suggestions
To get keyword suggestions based on a given keyword:

```
keyword = 'Python'
suggestions = trends.get_suggestions(keyword)
print(suggestions)
```

### Trend Predictions
To predict future trends based on the fetched data:

```
predictions = trends.predict_trends(data)
print(predictions)
```

### Export data
To export the fetched data to a CSV or JSON file:

```
file_name = 'data.csv'
trends.export_data(data, file_name)

file_name = 'data.json'
trends.export_data(data, file_name)
```

## Examples
To demonstrate the usage of the pytrendsplus library, you can create a script with the following code:

```commandline
from pytrendsplus import PyTrendsPlus

# Create an instance of the PyTrendsPlus class
trends = PyTrendsPlus()

# Fetch Google Trends data
keywords = ['Python', 'JavaScript']
time_range = '2020-01-01 2020-02-01'
data = trends.fetch_data(keywords, time_range)

# Visualize the data as a line chart
trends.plot_line_chart(data, title='Google Trends Interest Over Time')

# Get keyword suggestions
keyword = 'Python'
suggestions = trends.get_suggestions(keyword)
print(suggestions)

# Predict future trends
predictions = trends.predict_trends(data)
print(predictions)

# Export the data to a CSV file
file_name = 'data.csv'
trends.export_data(data, file_name)

# Export the data to a JSON file
file_name = 'data.json'
trends.export_data(data, file_name)
```

Save this script as example.py and run it with the command:

```
python example.py
```

## License
MIT License
