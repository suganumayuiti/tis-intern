#from zaifapi.impl import ZaifPublicApi, ZaifPrivateApi
from bottle import get, post, delete, request, run
import collections, json
import requests

URL = 'https://coincheck.com/api/ticker'
API ="https://api.bitflyer.jp/v1/ticker"
url ="https://api.zaif.jp/api/1/ticker/btc_jpy"



if __name__ == "__main__":
  store = collections.defaultdict(str)
  
  @get("/")
  def _alive():
    coincheck = requests.get(URL).json()
  #  coincheck2 = requests.get(URL2).json()
    print(coincheck)
    bitflyer = requests.get(API).json()
    bitflyer2 = requests.get(API2).json()
    print(bitflyer2['best_bid'])
    zaif = requests.get(url).json()


    i = 0
    bid_btc = []
    print(zaif['last'])
    print(coincheck['last'])
    bid_btc.append(int(bitflyer["best_bid"]))
    print("BTC_JP Bid: " + "{:,d}".format(bid_btc[i]) + "円")
    co=coincheck['last']
    o = "{:,d}".format(bid_btc[i])
    zai=zaif['last']
    cona='coincheck'

    #jsonString = '''
    l={
        "torihiki":{

                "co": {

                    "name": "coincheck",
                    "tuka": "Bit coin",
                    "price": co
                },
                "bit": {
                    "name": "bitflyer",
                    "tuka": "Bit coin",
                    "price": "{:,d}".format(bid_btc[i])
                },
                "zai": {
                    "name": "zaif",
                    "tuka": "Bit coin",
                    "price": zai
                }

        }

    }
    #data = json.loads(jsonString)
    return json.dumps(l)


  @get("/co")
  def _dict():
      coincheck = requests.get(URL).json()
      print(coincheck)
      co=coincheck['last']
      l={
          "name": "coincheck",
          "tuka": "Bit coin",
          "price": co
      }
      return json.dumps(l)


  @get("/coincheck")
  def _dict():
      coincheck = requests.get(URL).json()
      print(coincheck)
      co = coincheck['last']
      l = {
          "name": "coincheck",
          "tuka": "Bit coin",
          "price": co
      }
      return json.dumps(l)


  @get("/Coincheck")
  def _dict():
      coincheck = requests.get(URL).json()
      print(coincheck)
      co = coincheck['last']
      l = {
          "name": "coincheck",
          "tuka": "Bit coin",
          "price": co
      }
      return json.dumps(l)


  @get("/coin")
  def _dict():
      coincheck = requests.get(URL).json()
      print(coincheck)
      co = coincheck['last']
      l = {
          "name": "coincheck",
          "tuka": "Bit coin",
          "price": co
      }
      return json.dumps(l)
  @get("/bitflyer")
  def _add():
      i = 0
      bid_btc = []
      bitflyer = requests.get(API).json()
      bid_btc.append(int(bitflyer["best_bid"]))
      l={
          "name": "bitflyer",
          "tuka": "Bit coin",
          "price": "{:,d}".format(bid_btc[i])
      }
      return json.dumps(l)


  @get("/zaif")
  def _dict():
      zaif = requests.get(url).json()
      zai = zaif['last']
      l={
          "name": "zaif",
          "tuka": "Bit coin",
          "price": zai

      }
      return json.dumps(l)

  @get("/bit")
  def _dict():
      i = 0
      bid_btc = []
      bitflyer = requests.get(API).json()
      bid_btc.append(int(bitflyer["best_bid"]))
      zaif = requests.get(url).json()
      zai = zaif['last']
      coincheck = requests.get(URL).json()
      co = coincheck['last']
      l={
          "nameco": "coincheck",
          "priceco": co,
          "namezai": "zaif",
          "pricezai": zai,
          "namebit": "bitflyer",
          "pricebit": "{:,d}".format(bid_btc[i])

      }
      return json.dumps(l)




run(host="0.0.0.0", port=8080)

