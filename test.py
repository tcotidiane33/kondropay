from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Informations d'authentification
api_key = '447088687629111c58c3573.70152188'
api_secret = '415625848629a242b4b94d1.61917217'


# Route pour recevoir les notifications de paiement
@app.route('/notify', methods=['POST'])
def notify():
    data = request.json

    # Vérification de la signature
    received_signature = data.get('signature')
    calculated_signature = hashlib.sha256(f'{data["transaction_id"]}{data["method"]}{data["amount"]}{api_secret}'.encode()).hexdigest()

    if received_signature == calculated_signature:
        # Signature vérifiée, gérer la notification
        if data['status'] == 'paid':
            # Le paiement a été effectué avec succès, effectuez les actions nécessaires ici
            print(f"Paiement réussi pour la transaction {data['transaction_id']}")
        else:
            # Le paiement a échoué ou a été annulé, prenez des mesures en conséquence
            print(f"Paiement échoué pour la transaction {data['transaction_id']}")
    else:
        # Signature non valide, rejeter la demande
        print("Signature non valide pour la notification")

    return jsonify({'status': 'ok'})

# Route pour initier une demande de paiement
@app.route('/initiate_payment', methods=['POST'])
def initiate_payment():
    amount = 1000  # Montant en centimes
    transaction_id = 'REF12345'  # Référence unique pour la transaction

    signature = hashlib.sha256(f'{api_key}{transaction_id}{amount}{api_secret}'.encode()).hexdigest()

    payment_data = {
        "api_key": api_key,
        "transaction_id": transaction_id,
        "amount": amount,
        "signature": signature,
        "currency": "XOF",
        "return_url": "YOUR_RETURN_URL",
        "notify_url": "YOUR_NOTIFY_URL"
    }

    return jsonify(payment_data)

if __name__ == '__main__':
    app.run(debug=True)
