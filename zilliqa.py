import requests
import json

hash = '14456246cc53d31f0a2eb00fa0248f7aebd3fa89'
page = 25  # max
data = {}
url_address = "https://api.viewblock.io/v1/zilliqa/addresses/14456246cc53d31f0a2eb00fa0248f7aebd3fa89"
url_transaction = f"https://api.viewblock.io/v1/zilliqa/addresses/{hash}/txs?page={page}"
api_key = '42c837ae2a534905d385ee7dfa02e43b23401df55528cfe6baf79baf1dee2025'
headers = {
  'X-APIKEY': '42c837ae2a534905d385ee7dfa02e43b23401df55528cfe6baf79baf1dee2025'
}
proxies = {
        "http": "http://pingi:600602@68.183.214.82:443",
        "https": "http://pingi:600602@68.183.214.82:443",
    }


# get address from hash
address_response = requests.request("GET", url_address, headers=headers, data=data, proxies=proxies)
address_data = json.loads(address_response.text)
address = address_data[0]['hash']


# get transactions
transaction_response = requests.request("GET", url_transaction, headers=headers, data=data, proxies=proxies)
clean_res = []
transactions_data = json.loads(transaction_response.text)
transactions = transactions_data
page_count = 0
for transaction in transactions:
    sender = transaction["from"]
    receipt = transaction['to']
    if (transaction["receiptSuccess"]) and (address == receipt) and (page_count < 10):
        page_count += 1
        amount = int(transaction['value']) / (10**12)
        clean_transaction = {
            "sender": sender,
            "id": transaction['hash'],
            'amount': amount,
            'receipt': receipt,
            'currency': 'ZIL',
            'network': 'zilliqa',
        }
        clean_res.append(clean_transaction)
    else:
        pass
print(clean_res)