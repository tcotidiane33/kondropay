from cinetpay_sdk.s_d_k import Cinetpay

apikey = "447088687629111c58c3573.70152188"
site_id = "558658"

client = Cinetpay(apikey,site_id)

data = {
    'amount' : 00000,
    'currency' : "XOF",
    'transaction_id' : "XXXXXXXXXXXXXXXX",
    'description' : "TRANSACTION DESCRIPTION",
    'return_url' : "https://www.exemple.com/return",
    'notify_url' : "https://www.exemple.com/notify",
    'customer_name' : "XXXXXXXXXXXX",
    'customer_surname' : "XXXXXXXXXXXXX",
}
print(client.PaymentInitialization(data) )