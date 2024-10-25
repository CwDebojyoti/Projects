import requests
from bs4 import BeautifulSoup
import json
import pandas

# Getting the match list:
response = requests.get("https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450")

cric_data_response = response.text

soup = BeautifulSoup(cric_data_response, "html.parser")

match_results = soup.find_all(name= 'td', class_ = 'ds-min-w-max')

item_list = []
for item in match_results:
    item_list.append(item.text)


match_list = []

for i in range(0, len(item_list), 7):
    match_list.append(item_list[i:i+7])

df = pandas.DataFrame(match_list[1:], columns=match_list[0])

print(df)








