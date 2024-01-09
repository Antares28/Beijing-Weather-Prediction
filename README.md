# Beijing Weather Prediction

We use data crawling to get weather data in Beijing. For the data processing part, we use pandas and numpy. Matplotlib is implemented for data visualization. Sklearn is used for air condition prediction based on ML models. 

Based on the historical weather and air condition data, we try to predict the air quality level for the present. We compare two algorithms, and finally, we choose the optimal algorithm and finish the fine-tuning process of hyperparameters.

DataCrawler.py: 2011-2024 Beijing's weather data. 

MergeTwoExcel.py: Merge Beijing's air quality data with weather data from 2011 to 2019. 

WeatherPie.py: Count the number of sunny, rainy, cloudy, snowy, hazy, and sand-raising days yearly, and draw a pie chart.

ContinuePollution.py: Count the times which have continuous pollution days each year

Prediction.py: We predict the air quality level based on the historical weather data and air quality data. 
