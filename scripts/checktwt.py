from cinetpay_sdk.s_d_k import Cinetpay

apikey = "XXXXXXXXXXXXXXXXXX"
site_id = "XXXXXX"

client = Cinetpay(apikey,site_id)
token ="XXXXXX"

print(client.TransactionVerfication_token(token))