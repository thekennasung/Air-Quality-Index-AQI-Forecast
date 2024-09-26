import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta

def get_weather_data(date):
    url = f"https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467410&stname=%25E8%2587%25BA%25E5%258D%2597&datepicker={date}&altitude=40.8m"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find("table", id="MyTable")
    rows = table.find_all("tr")

    data = []
    for row in rows[3:]:
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)

    return data

def main():
    headers = ['觀測時間(hour)', '測站氣壓(hPa)', '海平面氣壓(hPa)', '氣溫(℃)', '露點溫度(℃)', '相對溼度(%)', '風速(m/s)', '風向(360degree)', '最大陣風(m/s)', '最大陣風風向(360degree)', '降水量(mm)', '降水時數(h)', '日照時數(h)', '全天空日射量(MJ/㎡)', '能見度(km)', '紫外線指數', '總雲量(0~10)']

    start_date = datetime(2020, 6, 13)
    end_date = datetime(2023, 5, 31)
    current_date = start_date

    with open('tainan_weather-1.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        while current_date <= end_date:
            date_str = current_date.strftime("%Y-%m-%d")
            print("Scraping data for", date_str)
            weather_data = get_weather_data(date_str)

            if len(weather_data) > 0:
                writer.writerows(weather_data)

            current_date += timedelta(days=1)

    print("Data scraping complete. Weather data saved in 'tainan_weather.csv'.")

if __name__ == '__main__':
    main()
