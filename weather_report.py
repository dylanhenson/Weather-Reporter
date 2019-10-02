from bs4 import BeautifulSoup
import requests

url = 'https://www.weatherbug.com/weather-forecast/10-day-weather/los-angeles-ca-90007'

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

temp = soup.find_all("div", {"class": "temp"})

current_temp = temp[1].text.strip()#fix this to find the correct temp. Sometimes not choosing the current day "Day" temperature

temp_num = int(''.join(list(filter(str.isdigit, current_temp))))

if temp_num < 65:
  rec = 'It\'s cold, bring a jacket!'
elif (temp_num >=65 and temp_num <75):
  rec = 'Nice weather today!'
else:
  rec = 'It\'s hot!'

print("\nHi Dylan! The weather right now is", current_temp, "degrees.", rec)


