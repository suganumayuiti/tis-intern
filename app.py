#from zaifapi.impl import ZaifPublicApi, ZaifPrivateApi
from bottle import get, post, delete, request, run
import collections, json
import requests

URL = 'https://coincheck.com/api/ticker'
URL2='https://coincheck.com/api/rate/btc_jpy'
API ="https://api.bitflyer.jp/v1/ticker"
API2 ="https://api.bitflyer.jp/v1/ticker?product_code_JPY"
url ="https://api.zaif.jp/api/1/ticker/btc_jpy"



if __name__ == "__main__":
  store = collections.defaultdict(str)
  
  @get("/")
  def _alive():
    coincheck = requests.get(URL).json()
    coincheck2 = requests.get(URL2).json()
    print(coincheck2)
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
   # jsonString = '''
    l={
        "coincheck": {

            "name": "coincheck",
            "tuka":"Bit coin",
            "price":co
        },
        "bitflyer":{
            "name": "bitflyer",
            "tuka": "Bit coin",
            "price": "{:,d}".format(bid_btc[i])
        },
        "zaif": {
            "name": "zaif",
            "tuka": "Bit coin",
            "price": zai
        }
    }
  # data = json.loads(jsonString)
    return json.dumps(l)


  @get("/dict")
  def _dict():
    return json.dumps(store)


  @post("/update")
  def _add():
    req = json.load(request.body)
    store.update(req)
    return json.dumps(store)


  run(host="0.0.0.0", port=8080)

