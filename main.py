# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests  # inbuilt used for HTTP file or link
import json  # to read json file


API_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=3&convert=USD&CMC_PRO_API_KEY=2809eb7d-f98f-46b8-954b-cae75115ed15")
API_status = {'timestamp': '2021-01-29T21:58:10.555Z', 'error_code': 0, 'error_message': None, 'elapsed': 12, 'credit_count': 1, 'notice': None, 'total_count': 3980}
API_tags = ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channels', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio']
API_DATA2= {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'num_market_pairs': 5748, 'date_added': '2015-08-07T00:00:00.000Z', 'tags': ['mineable', 'pow', 'smart-contracts', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio'], 'max_supply': None, 'circulating_supply': 114456238.0615, 'total_supply': 114456238.0615, 'platform': None, 'cmc_rank': 2, 'last_updated': '2021-01-30T00:10:02.000Z', 'quote': {'USD': {'price': 1401.9156418626967, 'volume_24h': 53910660101.923996, 'percent_change_1h': 1.11921757, 'percent_change_24h': 4.10245287, 'percent_change_7d': 13.91692365, 'percent_change_30d': 87.67911379, 'market_cap': 160457990447.1774, 'last_updated': '2021-01-30T00:10:02.000Z'}}}

API = json.loads(API_requests.content)

for key in API_status:
    print(key, '<-->', API_status[key])


print("************ DETAILS OF THE API DATA ***********")

print("API DATA ID:", API["data"][0]["id"])
print("Name: for ID", API["data"][0]["id"],  API["data"][0]["name"])
print("Symbol for ID", API["data"][0]["id"],API["data"][0]["symbol"])
print("Slug for ID:", API["data"][0]["id"], API["data"][0]["slug"])
print("num_market_pairs for iD", API["data"][0]["id"], API["data"][0]["num_market_pairs"])
print("Date_added for ID:", API["data"][0]["id"], API["data"][0]["date_added"])
print("\n")

print("Tags for ID", API["data"][0]["id"])

for i in API_tags:
    print("'", i, "'")

print("\n")

print("Max Supply for ID", API["data"][0]["id"], "is", API["data"][0]["max_supply"])
print("Circulating supply for ID:", API["data"][0]["id"], "is", API["data"][0]["circulating_supply"])
print("Total supply for ID:", API["data"][0]["id"], "is", API["data"][0]["total_supply"])
print("Platform for ID:", API["data"][0]["id"],API["data"][0]["platform"])
print("CMC Rank:", API["data"][0]["id"], API["data"][0]["cmc_rank"])
print("Last updated for ID", API["data"][0]["id"], "is", API["data"][0]["last_updated"])

print("\n")

print("API DATA for id:", API["data"][1]["id"])
for items in API_DATA2:
    print(items, ' : ', API_DATA2[items])
