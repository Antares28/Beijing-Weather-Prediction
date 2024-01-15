# Beijing Weather Prediction
Project group: 12
group member: WEI Jian, LI Xinyang
## Summary

We use data crawling to get weather data in Beijing. For the data processing part, we use pandas and numpy. Matplotlib is implemented for data visualization. Sklearn is used for air condition prediction based on ML models. 

Based on the historical weather and air condition data, we try to predict the air quality level for the present. We compare two algorithms, and finally, we choose the optimal algorithm and finish the fine-tuning process of hyperparameters.

DataCrawler.py: 2011-2024 Beijing's weather data. 

MergeTwoExcel.py: Merge Beijing's air quality data with weather data from 2011 to 2019. 

WeatherPie.py: Count the number of sunny, rainy, cloudy, snowy, hazy, and sand-raising days yearly, and draw a pie chart.

ContinuePollution.py: Count the times which have continuous pollution days each year

Prediction.py: We predict the air quality level based on the historical weather data and air quality data. 

## The dataset
- Data Crawler: Use `AirQuality_Crawler.py` and `Weather_Crawler.py` to get Beijing's weather and air quality data. They are saved in `DataCrawler` folder.
- Data: `Beijing Weather Crawler.xlsx` and `Beijing Air Quality Crawler.xlsx` are collected using the data crawler. We merge two parts of the data named `Beijing_Weather.csv`. All data are in `data` folder.
- Data Preprosessing: We drop some unrelated columns and use numerical encoding to translate characters into numbers.
## Our method
We use `Random Forest`for our regression work.
Since we have a large dataset and our high dimensionality feature of the dataset. We try to use random forest to finish the regression problem. Its prediction result is good as we think.
## Our results
For our training model, MAE is 0.04. It can be thought of as a good regression model. 
## How to run the code

1. Download the dataset: in data folder.
   
2.feature_pipline.ipynb: Download the feature processing file and try to use this file to preprocess the dataset.

3.training_pipeline.ipynb : Download the file and use it to train a random forest regression model using orginial data. The metric we chose is MAE (Mean Absolute Error)

4.app.py: The code for the demo on huggingface

5.requirments.txt: It shows the needed version for some libraries.
