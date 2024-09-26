# Air Quality Index (AQI) Forecast

## Project Overview

This project focuses on forecasting the Air Quality Index (AQI) using various machine learning and deep learning models. The goal is to provide accurate predictions of AQI based on historical data and model analysis. The models used include Random Forest, LightGBM, XGBoost, and a PyTorch-based neural network, providing a comparison of different techniques for time series forecasting.

Additionally, the project integrates **web scraping** techniques to collect real-time AQI data from public sources, ensuring up-to-date information is available for training and testing purposes.

## Features

- **Data Preprocessing**: The data is normalized using `StandardScaler` and `MinMaxScaler` from `sklearn.preprocessing` to ensure optimal model performance.

- **Modeling**:
  - **Random Forest**: A robust ensemble learning method from the `sklearn` library, suitable for handling non-linear relationships and feature interactions in time series data.
  - **LightGBM**: An efficient gradient boosting method, ideal for handling large datasets and fast model training.
  - **XGBoost**: A powerful gradient boosting model for time series regression.
  - **LSTM**: A specialized type of recurrent neural network (RNN) built with PyTorch, designed for capturing long-term dependencies in time series data. LSTMs are particularly effective for AQI forecasting as they can learn complex temporal patterns in the data.

- **Web Scraping**: Automated data collection from online AQI monitoring websites, ensuring fresh data for training and testing.

- **Model Evaluation**: Models are evaluated using accuracy metrics and confusion matrices, giving insight into their forecasting abilities.

## Project Structure

- `final_project_dt&rf&LightGBM.ipynb`: Contains the full implementation of data preprocessing, model training, and evaluation for Decision Tree, Random Forest, and LightGBM models. These models provide traditional machine learning techniques for time series forecasting of AQI data.
  
- `Final_Project_XGBoost&LSTM.ipynb`: Implements more advanced modeling techniques, including XGBoost and Long Short-Term Memory (LSTM) neural networks. This notebook includes additional evaluation metrics and improvements aimed at capturing more complex patterns in AQI data, combining gradient boosting with deep learning.

- `DataCrawler.py`: A module for web scraping weather and AQI data from online sources. This script automates the process of collecting up-to-date weather information, ensuring fresh input for the forecasting models.

- `data/`: A directory where the AQI datasets are stored (datasets are not included in this repository). This is where pre-processed and real-time scraped data would be located for model training and evaluation.


## Requirements

- `Python 3.x`

- Key libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `torch`
  - `statsmodels`
  - `xgboost`
  - `sklearn`
  - `beautifulsoup4` (for web scraping)
  - `requests` (for fetching data from websites)

Install the required libraries with:

```bash
pip install -r requirements.txt
```


## How to Run
1. Clone the repository and navigate to the project directory.
   
2. Ensure you have the necessary dependencies by installing the packages in `requirements.txt`.

3. Run either of the notebooks (`final_project_dt&rf&LightGBM.ipynb` or `Final_Project_XGBoost&LSTM.ipynb`) using Jupyter Notebook or Google Colab.

4. If you want to fetch real-time data, ensure the web scraper is correctly set up and configured to fetch data from the chosen source.
   
## Web Scraping Component

This project uses web scraping to collect real-time AQI data from external websites. The web scraper is written using `BeautifulSoup` and `requests` and can be extended to scrape from multiple sources. Ensure that you have appropriate permissions to scrape the target website, and adjust the scraper code to comply with the site's `robots.txt` policies.

## Future Work
- Expand the web scraping module to support additional data sources.
  
- Explore more advanced deep learning models like LSTMs and GRUs for improved time series forecasting.
  
- Enhance the evaluation metrics to include other time-series-specific measures like MAE and RMSE.
