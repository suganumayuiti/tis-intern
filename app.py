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
    zaif = requests.get(url).json()

    print(zaif)
    i = 0
   # zaif = ZaifPublicApi()
   # print(zaif.last_price('btc_jpy'))
    #zaif = ZaifTradeApi(key, secret)
   # print(zaif.get_info())

    bid_btc = []
    res = requests.get(API)
    coincheck = requests.get(URL).json()
    bitflyer = res.json()
    print(zaif['last'])
    print(coincheck["last"])
    bid_btc.append(int(bitflyer["best_bid"]))
    print("BTC_JP Bid: " + "{:,d}".format(bid_btc[i]) + "円")
    o = "{:,d}".format(bid_btc[i])
    #print(json.dumps(o))

    return json.dumps(o)


  @get("/dict")
  def _dict():
    return json.dumps(store)


  @post("/update")
  def _add():
    req = json.load(request.body)
    store.update(req)
    return json.dumps(store)


  run(host="0.0.0.0", port=8080)

