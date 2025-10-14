import json 

#DESERIALIZAÇÂO

# dados_json = 

# dados_python = json.loads(dados_json)


# print(dados_python)

#SERIALIZAÇÂO

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

strinfOfJsonData = json.dumps(pythonValue)
print(strinfOfJsonData) 