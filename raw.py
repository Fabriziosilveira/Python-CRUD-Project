from pymongo import MongoClient

connection = 'mongodb://localhost:27017/'
client = MongoClient(connection)

db_connection = client['DataBase']

colletion = db_connection.get_collection('Teste')

search_filter = { "firstName": "Carlos" }      ## filtro 

response = colletion.find(search_filter)   ## GET recebendo a resposta

for registry in response: print(registry)

colletion.insert_one({
    "fistName": "Pedro",
    "secoundName": "Silva"
})