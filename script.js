   function checkout() {
            CinetPay.setConfig({
                apikey: '447088687629111c58c3573.70152188',
                site_id: 83aa4249-3109-46a2-9938-1bf8ca2a4e47,
                mode: 'PRODUCTION',
                notify_url: 'https://kondropay.netlify.app'
            });
            CinetPay.getCheckout({
                transaction_id: Math.floor(Math.random() * 100000000).toString(),
                amount: 100,
                currency: 'XOF',
                channels: 'ALL',
                description: 'Test de paiement',
                 //Fournir ces variables pour le paiements par carte bancaire
                customer_name:"Super",//Le nom du client
                customer_surname:"Nova",//Le prenom du client
                customer_email: "support@kondronetworks.com",//l'email du client
                customer_phone_number: "0769469844",//l'email du client
                customer_address : "BP 01 ABIDJAN",//addresse du client
                customer_city: "Cocody",// La ville du client
                customer_country : "Ivory coast",// le code ISO du pays
                customer_state : "Abidjan",// le code ISO l'état
                customer_zip_code : "06510", // code postal

            });
            CinetPay.waitResponse(function(data) {
                if (data.status == "REFUSED") {
                    if (alert("Votre paiement a échoué")) {
                        window.location.reload();
                    }
                } else if (data.status == "ACCEPTED") {
                    if (alert("Votre paiement a été effectué avec succès")) {
                        window.location.reload();
                    }
                }
            });
            CinetPay.onError(function(data) {
                console.log(data);
            });
        }