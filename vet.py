import requests
import json

address = "S7QLKPLSSPFFDK2GPOJAV7BBGFK3IPBS6FQCR2QT5XA4CHW4SEOQ5RST4I"
url = f"https://algoindexer.algoexplorerapi.io/v2/transactions?limit=10&address={address}"

data={}
headers = {
  'Cookie': '__cflb=0H28umPqHHxMibtJ1GY6DthrPTJRvfm1zMeQWx31eoo'
}

response = requests.request("GET", url, headers=headers, data=data, proxies={
        "http": "http://pingi:600602@68.183.214.82:443",
        "https": "http://pingi:600602@68.183.214.82:443",
    })

clean_res = []
data = json.loads(response.text)
transactions = data['transactions']
for transaction in transactions:
    receipt = transaction["payment-transaction"]["receiver"]
    if (transaction["confirmed-round"] > 100) and (address == receipt):
        clean_transaction = {
            "sender": transaction["sender"],
            "id": transaction["id"],
            'amount': transaction["payment-transaction"]["amount"],
            'receipt': receipt,
            'currency': 'ALGO',
            'network': 'algorand',
        }
        clean_res.append(clean_transaction)
    else:
        pass
print(clean_res)