# Beijing Weather Prediction
Project group: 12

group member: WEI Jian, LI Xinyang
## Summary

We use data crawling to get weather data in Beijing. For the data processing part, we use pandas and numpy. Matplotlib is implemented for data visualization. Sklearn is used for air condition prediction based on ML models. 

Based on the historical weather and air condition data, we try to predict the air quality level for the present. We compare two algorithms, and finally, we choose the optimal algorithm and finish the fine-tuning process of hyperparameters.

`AirQuality_Crawler.py`: 2011-2024 Beijing's air quality data. 

`Weather_Crawler.py`: 2011-2024 Beijing's weather data. 

`MergeTwoExcel.py`: Merge Beijing's air quality data with weather data from 2011 to 2024. 

`WeatherPie.py`: Count the number of sunny, rainy, cloudy, snowy, hazy, and sand-raising days yearly, and draw a pie chart.

`feature-pipeline.ipynb`: preprocess features and store the feature group into hopsworks.

`training-pipeline.ipynb`: use RandomForestRegressor algorithm to train the data, the model is saved as `random_forest_regressor_model.pkl` in github and huggingface.

`app.py`: online interface on huggingface.

`requirements.txt`: needed libraries to run app.py on huggingface.

## The dataset
Data sources: http://www.tianqihoubao.com/lishi/beijing/20240115.html, http://www.tianqihoubao.com/aqi/beijing.html
- Data Crawler: Use `AirQuality_Crawler.py` and `Weather_Crawler.py` to get Beijing's weather and air quality data. They are saved in `DataCrawler` folder.
- Data: `Beijing Weather Crawler.xlsx` and `Beijing Air Quality Crawler.xlsx` are collected using the data crawler. We merge two parts of the data named `Beijing_Weather.csv`. All data are in `data` folder.
- Data Preprosessing: We drop some unrelated columns and use numerical encoding to translate characters into numbers.
## Our method
We use `Random Forest`for our regression work.
Since we have a large dataset and our high dimensionality feature of the dataset. We try to use random forest to finish the regression problem. Its prediction result is good as we think.
## Our results
For our training model, MAE is 0.04. It can be thought of as a good regression model. 
## User Interface
online interface on huggingface: https://huggingface.co/spaces/Antares28/weather
![image](https://github.com/Antares28/Beijing-Weather-Prediction/blob/2483c87dea9e6be958dcc89e169762de257a1900/imgs/Gradio.png)
## How to run the code

1. Download the dataset: in data folder.
   
2.feature_pipline.ipynb: Download the feature processing file and try to use this file to preprocess the dataset.

3.training_pipeline.ipynb : Download the file and use it to train a random forest regression model using orginial data. The metric we chose is MAE (Mean Absolute Error)

4.app.py: The code for the demo on huggingface

5.requirments.txt: It shows the needed version for some libraries.
