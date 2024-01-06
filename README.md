
# TS_visual: Time Series Visualization Class

## Overview
`TS_visual` is a Python class designed to simplify the visualization of time series data using Matplotlib. It provides an easy-to-use interface for creating various types of plots directly from a pandas DataFrame. This class is especially useful for quick, preliminary visual explorations of time series data in Jupyter notebooks.

## Features
- Line plots for single and multiple time series.
- Autocorrelation and partial autocorrelation plots.
- Histograms and box plots for distribution analysis.
- Comprehensive statistical plot that includes trend, seasonality, and residuals.
- Support for custom themes, including light and dark modes.
- Simple integration with pandas DataFrames.
- Customizable plot settings for improved visual appeal.

## Installation
To use `TS_visual`, you need Python installed on your system along with the following libraries:
- pandas
- numpy
- matplotlib
- statsmodels
- sklearn

Clone the repository to your local machine:
```
git clone https://github.com/[your-username]/TS_visual.git
```

## Usage
Import the class and create an instance by passing a pandas DataFrame and the name of the date column:
```python
from TS_visual import TS_visual

# Assuming 'df' is your DataFrame and 'date' is the date column
visualizer = TS_visual(df, 'date')
```

### Creating Plots
Here are some examples of how to create different plots:

**Line Plot:**
```python
visualizer.line_plot('your_time_series_column')
```

**Autocorrelation Plot:**
```python
visualizer.autoCorrelation_plot('your_time_series_column')
```

Refer to the class documentation for more details on each method.

## Customization
You can customize the appearance of your plots using the theme feature. Supported themes include 'default', 'light', and 'dark'. You can also create your own theme as a JSON file.

To apply a theme:
```python
visualizer.apply_theme('light')
```

## Contributing
Contributions to `TS_visual` are welcome. Please ensure to follow the project's code style and add unit tests for any new or changed functionality. Fork the repository and submit pull requests for review.

## License
This project is licensed under [License Name].

## Acknowledgements
Special thanks to [Contributors' Names] for their contributions and support in developing this project.
