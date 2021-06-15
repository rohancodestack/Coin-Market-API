from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title("My first Crypto Portfolio")
pycrypto.iconbitmap("/Users/rohanaggarwal/Downloads/Favicon.ico")


def font_color(amount):
    if amount>=0:
        return "green"
    else:
        return "red"



def my_portfolio():

    API_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=2809eb7d-f98f-46b8-954b-cae75115ed15")
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
            "price_per_coin": 2000.70

        },
        {
            "symbol": "LTC",
            "amount_owned": 2,
            "price_per_coin": 2000.62

        },
        {
            "symbol": "DOGE",
            "amount_owned": 2,
            "price_per_coin": 0.068

        }

    ]

    total_pl_portfolio = 0
    coin_row = 1

    for i in range(0, 10):  # taking number of coins range (0=BTC, 3=EOS)
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
                print("Total Profit and loss with Coin", API["data"][i]["name"], "is: ","${0:.2f}".format(total_profitLoss_per_coin))
                print("===================")
                print("Total Profit/Loss for this portfolio", API["data"][i]["name"], "{0:.2f}".format(total_pl_portfolio))
                print("*******************")

                name = Label(pycrypto, text=API["data"][i]["symbol"], bg="#F3F4F6", fg="black", font="Lato 14 bold", padx="5", pady="5", borderwidth=2, relief="groove")
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)

                price = Label(pycrypto, text="${0:.2f}".format(API["data"][i]["quote"]["USD"]["price"]), bg="yellow", fg="black", font="Lato 14 bold", padx="5", pady="5", borderwidth=2, relief="groove")
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)

                Coins_owned = Label(pycrypto, text=coin["amount_owned"], bg="yellow", fg="black", font="Lato 14 bold", padx="5", pady="5", borderwidth=2, relief="groove")
                Coins_owned.grid(row=coin_row, column=2, sticky=N + S + E + W)

                Total_Amount_paid= Label(pycrypto, text="{0:.2f}".format(total_paid), bg="yellow", fg="black", font="Lato 14 bold", padx="5", pady="5", borderwidth=2, relief="groove")
                Total_Amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

                Current_value = Label(pycrypto, text="${0:.2f}".format(current_value), bg="yellow", fg=font_color(float("{0:.2f}".format(current_value))), font="Lato 14 bold", padx="5", pady="5", borderwidth=2, relief="groove")
                Current_value.grid(row=coin_row, column=4, sticky=N + S + E + W)

                PL_per_coin = Label(pycrypto, text="${0:.2f}".format(total_profitLoss_per_coin), bg="yellow", fg=font_color(float("{0:.2f}".format(PL_per_coin))), font="Lato 14 bold", padx="5", pady="5", borderwidth=2, relief="groove")
                PL_per_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                total_pl_Portfolio = Label(pycrypto, text="{0:.2f}".format(total_pl_portfolio), bg="yellow", fg=font_color(float("{0:.2f}".format(total_pl_portfolio))), font="Lato 14 bold", padx="5", pady="5", borderwidth=2, relief="groove")
                total_pl_Portfolio.grid(row=coin_row, column=6, sticky=N + S + E + W)

                coin_row = coin_row + 1

    update = Button(pycrypto, text="Update", bg="red", fg="black", command=my_portfolio , font="Lato 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    update.grid(row=coin_row, column=6, sticky=N + S + E + W)


# for header and their respective colors
name = Label(pycrypto, text="Coin Name", bg="grey", fg="white", font="Lato 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

name = Label(pycrypto, text="Price", bg="grey", fg="white", font="Lato 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=1, sticky=N+S+E+W)

name = Label(pycrypto, text="Coins owned", bg="grey", fg="white", font="Lato 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=2, sticky=N+S+E+W)

name = Label(pycrypto, text="Total Amount paid", bg="grey", fg="white", font="Lato 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=3, sticky=N+S+E+W)

name = Label(pycrypto, text="Current Value", bg="grey", fg="white", font="Lato 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=4, sticky=N+S+E+W)

name = Label(pycrypto, text="P/L per coin", bg="grey", fg="white", font="Lato 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=5, sticky=N+S+E+W)

name = Label(pycrypto, text="Total P/L with coin", bg="grey", fg="white", font="Lato 16 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=6, sticky=N+S+E+W)

my_portfolio()

pycrypto.mainloop()

print("Program has executed")