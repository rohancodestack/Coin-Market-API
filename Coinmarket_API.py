
import requests
import json
API_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=3&convert=USD&CMC_PRO_API_KEY=2809eb7d-f98f-46b8-954b-cae75115ed15")
API = json.loads(API_requests.content)

print("================")
print("================")

coins = [
    {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_per_coin": 33452,

    },
    {
        "symbol": "ETH",
        "amount_owned": 2,
        "price_per_coin": 1341.70

    }
]

total_pl_portfolio = 0
for i in range(0, 2): # taking number of coins range (0=BTC, 3=EOS)
    for coin in coins:

        if API["data"][i]["symbol"] == coin["symbol"]:
            print(API["data"][i]["symbol"])
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * API["data"][i]["quote"]["USD"]["price"]
            PL_per_coin = API["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            total_profitLoss_per_coin = PL_per_coin * coin["amount_owned"]

            total_pl_portfolio = total_pl_portfolio + total_profitLoss_per_coin

            print("Coin Name:  ", API["data"][i]["name"] + "-" + API["data"][i]["symbol"])
            print("Price - ${0:.2f}".format(API["data"][i]["quote"]["USD"]["price"]))
            print("Total amount paid:", total_paid)
            print("Current value for", API["data"][i]["name"], "is:", "${0:.2f}".format(current_value))
            print("Profit and loss for", API["data"][i]["name"], "is:", "${0:.2f}".format(PL_per_coin))
            print("Total Profit and loss with Coin", API["data"][i]["name"], "is: ", "${0:.2f}".format(total_profitLoss_per_coin))
            print("===================")
            print("Total Profit/Loss for this portfolio", API["data"][i]["name"], "{0:.2f}".format(total_pl_portfolio))
            print("*******************")

