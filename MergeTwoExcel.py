import pandas as pd

def Merge(AllBJAirQualityData, AllBJWeatherData):

    AllBJAirQualityData['Date'] = pd.to_datetime(AllBJAirQualityData['Date'])
    AllBJWeatherData['Date'] = pd.to_datetime(AllBJWeatherData['Date'])
    
    # Merge 2 DataFrames, based on date columns
    merged_data = pd.merge(AllBJAirQualityData, AllBJWeatherData, on='Date', how='inner')
    
    # import to csv
    merged_data.to_csv('Beijing Weather1.csv')

 



if __name__ == '__main__':
    AllBJAirQualityData = pd.read_excel(r'Beijing Air Quality Crawler.xlsx')
    BJWeatherData = pd.ExcelFile(r'Beijing Weather Crawler.xlsx')

    # Merge weather information 
    SheetNames = BJWeatherData.sheet_names
    AllBJWeatherData = pd.DataFrame()
    for i in SheetNames:
        OneYearData = pd.read_excel(r'Beijing Weather Crawler.xlsx', sheet_name = i)
        AllBJWeatherData = pd.concat([AllBJWeatherData, OneYearData])
        
    Merge(AllBJAirQualityData, AllBJWeatherData)
