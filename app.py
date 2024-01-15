import gradio as gr
import pandas as pd
import joblib

model = joblib.load("random_forest_regressor_model.pkl")


def encode_weather_condition(condition):
    weather_mapping = {
        '晴': 1,
        '多云': 2,
        '阴': 3,
        '雪': 4,
        '扬沙': 5,
    }
    if '雨' in condition:
        return 6
    if '霾' in condition or '雾' in condition:
        return 7
    return weather_mapping.get(condition, 0)

    
def predict_air_quality(pm25, pm10, so2, no2, co, o3, weather_condition):
    day_weather_condition, night_weather_condition = weather_condition.split('/')
    
    day_weather_condition = encode_weather_condition(day_weather_condition)
    night_weather_condition = encode_weather_condition(night_weather_condition)
    
    input_data = pd.DataFrame([[pm25, pm10, so2, no2, co, o3, day_weather_condition, night_weather_condition]],
                              columns=['pm25', 'pm10', 'so2', 'no2', 'co', 'o3', 'day_weather_condition', 'night_weather_condition'])

    prediction = model.predict(input_data)[0]
    quality_mapping = {1: "GOOD(优): 0 to 50 AQI", 2: "Moderate(良): 51 to 100 AQI", 3: "Unhealthy for Sensitive Groups(轻度污染): 101 to 150 AQI",
                       4: "Unhealthy(中度污染): 151 to 200 AQI", 5: "Very Unhealthy(重度污染): 201 to 300 AQI", 6: "Hazardous(严重污染): 301 to 500 AQI"}
    return quality_mapping.get(prediction, "Unknown(未知)")


iface = gr.Interface(
    fn=predict_air_quality,
    inputs=[
            gr.Number(label="PM2.5"),
            gr.Number(label="PM10"),
            gr.Number(label="SO2"),
            gr.Number(label="NO2"),
            gr.Number(label="CO"),
            gr.Number(label="O3"),
            gr.Text(label="Weather Condition"),
    ],
    outputs="text",
    title="Air Quality Prediction",
    description="Predict the air quality level based on the input parameters."
)

iface.launch()
