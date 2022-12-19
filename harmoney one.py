import requests
import json

url = "https://api.harmony.one/"
pageSize = 10
data = json.dumps({
  "jsonrpc": "2.0",
  "method": "hmy_getTransactionsHistory",
  "params": [
    {
      "address": "one103q7qe5t2505lypvltkqtddaef5tzfxwsse4z7",
      "pageIndex": 0,
      "pageSize": pageSize,
      "fullTx": True,
      "txType": "ALL",
      "order": "DESC"
    }
  ],
  "id": 1
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'DO-LB="MTAuMTA2LjAuMTA6ODUwMA=="'
}

try:
    response = requests.request("POST", url, headers=headers, data=data, proxies={
        "http": "http://pingi:600602@68.183.214.82:443",
        "https": "http://pingi:600602@68.183.214.82:443",
    })
    clean_res = []
    data = json.loads(response.text)
    transactions = data['result']['transactions']
    for transaction in transactions:
        value = transaction["value"]
        amount = int(value, 16)/(10**18)
        clean_transaction = {
            "sender": transaction["from"],
            "id": transaction["ethHash"],
            'amount': amount,
            # 'id': tx['hash'],
            'currency': 'One',
            'network': 'Hermoney_One',
            }
        clean_res.append(clean_transaction)
    print(clean_res)

except Exception as e:
    print(e)
