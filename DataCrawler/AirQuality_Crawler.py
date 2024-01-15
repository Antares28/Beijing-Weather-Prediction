import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup
import re
import xlsxwriter
import time


def PreprocessingData(InfoString):
    # replace redundant characters
    InfoString = InfoString.replace('\n', '',)
    InfoString = InfoString.replace('\r', '',)
    InfoString = InfoString.replace(' ', '',)
    
    return InfoString



def ExtractBJWeather():
    # Create an Excel table Beijing Weather Crawler.xlsx, each year has its own worksheet
    BJAirQualityExcel = xlsxwriter.Workbook('Beijing Air Quality Crawler.xlsx')

    url = 'http://www.tianqihoubao.com/aqi/beijing.html'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36','Connection': 'close'}
    html = requests.get(url, headers = head)
    bsObj = BeautifulSoup(html.content, 'lxml')

    BJAirQuality = bsObj.find('div', class_ = "box p")
    
    WorkSheet = BJAirQualityExcel.add_worksheet("Beijing Air Quality")
    titles = ['Date', 'Quality Level', 'AQI', 'AQI Rank in China', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    row = 0
    for col, title in enumerate(titles):
        WorkSheet.write(row, col, title)

    Data = BJAirQuality.find('ul')
    ThreeMonthLink = Data.find_all('a')
    for Link in ThreeMonthLink:
        print(Link)
        AMonthLink = Link['href']
        AMonthurl = urljoin('http://www.tianqihoubao.com', AMonthLink)
        
        try:
            AMonth_HTML = requests.get(AMonthurl, headers=head)
            AMonthObj = BeautifulSoup(AMonth_HTML.content, 'lxml')
            AMonthData = AMonthObj.find_all('tr')
            
            for ADay in AMonthData[1:]: # Skip the header row
                col = 0
                row += 1
                ALine = ADay.find_all('td')
                for info in ALine:
                    AnInfo = str(info.get_text())
                    AnInfo = PreprocessingData(AnInfo)
                    WorkSheet.write(row, col, AnInfo)
                    col += 1
        except Exception as e:
            print(f"Error: {e}. Need to sleep!")
            time.sleep(5)
            print("Continuing...")
            continue

    BJAirQualityExcel.close()
    print('---------------------end----------------')




if __name__ == '__main__':
    ExtractBJWeather()