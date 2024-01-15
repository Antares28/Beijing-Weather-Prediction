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
    
    # adjust date format
    InfoString = InfoString.replace('年', '-', 1)
    InfoString = InfoString.replace('月', '-', 1)
    InfoString = InfoString.replace('日', '', 1)
    
    return InfoString



def ExtractBJWeather():
    # Create an Excel table Beijing Weather Crawler.xlsx, each year has its own worksheet
    BJWeatherExcel = xlsxwriter.Workbook('Beijing Weather Crawler.xlsx')

    url = 'http://www.tianqihoubao.com/lishi/beijing.html'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36','Connection': 'close'}
    html = requests.get(url, headers = head)
    bsObj = BeautifulSoup(html.content, 'lxml')

    OneYearWeather = bsObj.find_all('div', class_ = "box pcity")
    # print(OneYearWeather)
    Year = 2010
    for AQuarter in OneYearWeather:  # a quarter's data
        Year += 1
        if Year <= 2024:
            # create new worksheet for a new year
            WorkSheet = BJWeatherExcel.add_worksheet(str(Year))
            titles = ['Date', 'Weather Condition', 'Temperature', 'Wind Force and Wind Direction']
            row = 0
            for col, title in enumerate(titles):
                WorkSheet.write(row, col, title)
                
            AQuarterData = AQuarter.find_all('ul')
            # print(AQuarterData)
            
            for AMonth in AQuarterData:  # traverse each month's data within a quarter
                # print(AMonth)  
                ThreeMonthLink = AMonth.find_all('a')
                for Link in ThreeMonthLink:
                    AMonthLink = Link['href']
                    
                    if '/lish' in str(AMonthLink): # some years' data is missing
                        AMonthurl = 'http://www.tianqihoubao.com' + AMonthLink  
                    else: # missing link processing
                        AMonthurl = 'http://www.tianqihoubao.com/lish' + AMonthLink
                    try: # excessively frequent requests
                        AMonth_HTML = requests.get(AMonthurl, headers = head)
                        AMonthObj = BeautifulSoup(AMonth_HTML.content, 'lxml')
                        # print(AMonthObj)
                        AMonthData = AMonthObj.find_all('tr')
                        i = 1
                        for ADay in AMonthData:
                            if i ==1:
                                i = 2
                                continue
                            else:
                                ALine = ADay.find_all('td')
                                col = 0
                                row += 1
                                for info in ALine:
                                    AnInfo = str(info.get_text())
                                    AnInfo = PreprocessingData(AnInfo)
                                    WorkSheet.write(row, col, AnInfo)
                                    col += 1
                    except:  # the request is too fast, rest for 5 seconds
                        print("requests speed so high,need sleep!")
                        time.sleep(5)
                        print("continue...")
                        continue
            print('Year: '+ str(Year) + ', done.')
        else:
            break
    BJWeatherExcel.close()
    print('---------------------end----------------')
    return 



if __name__ == '__main__':
    ExtractBJWeather()   