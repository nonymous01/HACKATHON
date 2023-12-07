# from flask import Flask, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/api/data', methods=['GET'])
# def get_api_data():
#     # URL de l'API
#     url = "https://sofasport.p.rapidapi.com/v1/search/suggest"
    
#     # Paramètres de la requête
#     querystring = {"query": "mess"}
    
#     # En-têtes de la requête
#     headers = {
#         "X-RapidAPI-Key": "2179d5b53fmshcd74e55345672b4p1b5658jsn5b54fea6295d",
#         "X-RapidAPI-Host": "sofasport.p.rapidapi.com"
#     }

#     # Envoi de la requête GET à l'API
#     response = requests.get(url, headers=headers, params=querystring)

#     # Vérification du statut de la réponse
#     if response.status_code == 200:
#         # Récupération des données JSON de la réponse
#         data = response.json()["data"]
#         return jsonify({"data": data})
#     else:
#         # En cas d'erreur, renvoyer un message d'erreur
#         return jsonify({"error": f"Erreur {response.status_code} lors de la requête à l'API."})

# if __name__ == '__main__':
#     app.run(debug=True)












from flask import Flask, jsonify
import requests
import bcrypt
app = Flask(__name__)

@app.route('/api/ivory_coast', methods=['GET'])
def get_ivory_coast_info():
    # URL de l'API
    url = "https://sofascores.p.rapidapi.com/v1/unique-tournaments/featured-events"
    
    # Paramètres de la requête
    querystring = {"unique_tournament_id":"270"}
    # Envoi de la requête GET à l'API
    headers = {
	"X-RapidAPI-Key": "2179d5b53fmshcd74e55345672b4p1b5658jsn5b54fea6295d",
	"X-RapidAPI-Host": "sofascores.p.rapidapi.com"
}
    response = requests.get(url, headers=headers, params=querystring)
    print(list(response))
    # Vérification du statut de la réponse
    if response.status_code == 200:
        # Récupération des données JSON de la réponse
        data = response.json()
        
        return jsonify({"ivory_coast_info": data})
    else:
        # En cas d'erreur, renvoyer un message d'erreur avec le statut de la réponse
        return jsonify({"error": f"Erreur {response.status_code} lors de la requête à l'API. Vérifiez vos clés d'API et les paramètres d'authentification."})

if __name__ == '__main__':
    app.run(debug=True)
