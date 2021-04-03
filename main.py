from tkinter import *
import requests
import json

pycrypto=Tk()
pycrypto.title("cryptocurrency")

def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=909c9705-4c6a-4338-8d16-04468cf918dd")

    api=json.loads(api_request.content)
    coins=[{
    "symbol":"BTC",
    "amount_owned":2,
    "price_per_coin":3200

    }, {
    "symbol":"ETH",
    "amount_owned":100,
    "price_per_coin":2.05
    }]



    total_pl=0

    coin_row=1

    for i in range(0,300):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid=coin["amount_owned"]*coin["price_per_coin"]
                currrent_value=(api["data"][i]["quote"]["USD"]["price"])*coin["amount_owned"]
                pl_percoin=(api["data"][i]["quote"]["USD"]["price"])-coin["price_per_coin"]
                total_pl_coin=pl_percoin * coin["amount_owned"]
                total_pl=total_pl + total_pl_coin


                name = Label(pycrypto, text=api["data"][i]["symbol"],bg="black",fg="blue")
                name.grid(row=coin_row,column=0,sticky=N+S+E+W)

                price = Label(pycrypto,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),bg="black",fg="white")
                price.grid(row=coin_row,column=1,sticky=N+E+W+S)

                no_coins = Label(pycrypto,text=coin["amount_owned"],bg="black",fg="white")
                no_coins.grid(row=coin_row,column=2,sticky=N+E+W+S)

                amount_paid = Label(pycrypto,text="${0:.2f}".format(total_paid),bg="black",fg="white")
                amount_paid.grid(row=coin_row,column=3,sticky=N+E+W+S)

                current_value = Label(pycrypto,text="${0:.2f}".format(currrent_value),bg="black",fg="white")
                current_value.grid(row=coin_row,column=4,sticky=N+E+W+S)

                pl_coin = Label(pycrypto,text="${0:.2f}".format(pl_percoin),bg="black",fg="white")
                pl_coin.grid(row=coin_row,column=5,sticky=N+E+W+S)

                totalpl = Label(pycrypto,text="${0:.2f}".format(total_pl),bg="black",fg="white")
                totalpl.grid(row=coin_row,column=6,sticky=N+E+W+S)

                coin_row=coin_row+1


            print("total P/L in the portfolio:","${0:.2f}".format(total_pl))

name = Label(pycrypto, text="coin name",bg="black",fg="blue")
name.grid(row=0,column=0,sticky=N+S+E+W)

price = Label(pycrypto,text="price",bg="black",fg="white")
price.grid(row=0,column=1,sticky=N+E+W+S)

no_coins = Label(pycrypto,text="coin owned",bg="black",fg="white")
no_coins.grid(row=0,column=2,sticky=N+E+W+S)

amount_paid = Label(pycrypto,text="total amount paid",bg="black",fg="white")
amount_paid.grid(row=0,column=3,sticky=N+E+W+S)

current_value = Label(pycrypto,text="current value",bg="black",fg="white")
current_value.grid(row=0,column=4,sticky=N+E+W+S)

pl_coin = Label(pycrypto,text="p/l per coin",bg="black",fg="white")
pl_coin.grid(row=0,column=5,sticky=N+E+W+S)

totalpl = Label(pycrypto,text="total p/l with coin",bg="black",fg="white")
totalpl.grid(row=0,column=6,sticky=N+E+W+S)


my_portfolio()
pycrypto.mainloop()

print("program completed")
