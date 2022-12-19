import requests
import json

address = 'erd1d5g9ddfkvn76lhhhgflvmsvevg7av62xnfal6xn5qxp69ql0pyrschu29k'
sender = 'erd1mhf2nza045hnkh6k4309uhntff7juxe28nvy59htxjd0a2ffmfmqw3cj6v'
receiver = 'erd1d5g9ddfkvn76lhhhgflvmsvevg7av62xnfal6xn5qxp69ql0pyrschu29k'
status = 'success'
order = 'desc'
url = f"https://api.elrond.com/accounts/{address}/transactions?sender={sender}&status={status}&order={order}&receiver={receiver}&withLogs=false"

data = {}
headers = {
  'Cookie': '__cflb=02DiuFSQqTyKxWxxwQjpVbmLzMsfdCMUJJR7exq7LwkvQ'
}

response = requests.request("GET", url, headers=headers, data=data, proxies={
        "http": "http://pingi:600602@68.183.214.82:443",
        "https": "http://pingi:600602@68.183.214.82:443",
    })

clean_res = []
data = json.loads(response.text)
transactions = data
count = 0
for transaction in transactions:
    count += 1
    if ('action' not in transaction) and ('data' not in transaction) and (count <= 10):
        amount = int(transaction["value"]) / (10**18)
        clean_transaction = {
            "sender": transaction["sender"],
            "id": transaction["txHash"],
            'amount': amount,
            'receipt': transaction["receiver"],
            'currency': 'EGLD',
            'network': 'Elrond',
        }
        clean_res.append(clean_transaction)
    else:
        pass
print(clean_res)