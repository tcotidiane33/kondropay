import requests
import json
import uuid
import random

 #definition des paramètres

 subscription_key_user_create = '447088687629111c58c3573.70152188'
 subscription_key_trans_create = '5336d33d51324b65a55d2d935298f3d'
 unique_ref = str(uuid.uuid4()) # a remplacer par la reference de l'utilisateur Go live
 url = 'https://sandbox.momodeveloper.mtn.com/v1_0/apiuser'
 body = {"providerCallbackHost": "string"}
 headers = {'X-Reference-Id': unique_ref, 'Content-type': 'application/json', 'Ocp-Apim-Subscription-Key': subscription_key_user_create}

# Creation de User API-  Si sucess alors on verra 201
r = requests.post(url, data=json.dumps(body), headers=headers)
print(r)

#Si la creation aboutit avec success, alors on continue pour la creation du API Key
if r.status_code==201:
  print("Creation de User API éffectif ")

  url = f'https://sandbox.momodeveloper.mtm.com/v1_0/apiuser/{unique_ref}/apikey'
  body = {"providerCallbackHost":"string"}
  headers = {'Ocp-Apim-Subscription-Key': subscription_key_user_create}

  r = requests.post(url, data=json.dumps(body), headers=headers)
  print(r)
  print(r.content)
  user_key_tojson r.json()
  apikey = user_key_tojson['apikey']
  print('le API Key a ete cree avec Success !', apikey)
  #print(type(apikey))

  #maintenant nous allons creer notre Autorization avec cryptage en base64
  #facultatif#
  print('Done !')

  # Demande de Token
  url = "https://sandbox.momodeveloper.mtn.com/collection/token/"
  headers = {'Ocp-Apim-Subscription-Key': subscription_key_trans_create}
  r = requests.post(url, headers=headers, auth=(unique_ref, apikey))
  #print(r)
  #print(r.content)

  if r.status_code== 200:
    json_content = r.json()
    access_token = json_content['access_token']
    token_type = json_content['token_type']
    expires_in = json_content['expires_in']
    print('access_token : ', access_token)
    print('token_type : ', token_type)
    print('expires_in : ', expires_in)


    #Pour effectuer une demande de payement !

    montant = 100
    devise = 'XOF'
    id = '123456789'
    payor_phone = '0022505084205108'
    payer_message = 'Paiement numero 0022505084205108'
    payee_message = 'Reglement OderID: 123456789'


    body = {
        'amount' : montant,
        'currency': devise,
        'externalId': id,
        'payer': {'partyIdType': 'MSISDN', 'partyId': payor_phone},
        'payerMessage':payer_message,
        'payeeNote': payee_message
    }

    headers ={
        #request headers
        'Authorization': 'Bearer'+ access_token,
        'X-Reference-Id': unique_ref,
        'X-target-Environment': 'sandbox',
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key_trans_create,
    }

    url = "sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"

    r = requests.post(url, data=json.dumps(body).encode("ascii"), headers=headers)
    print(r)
    print(" La transaction a ete derouler san aucun probleme ; Merci !")
    print("Good Bye Kondro !")
