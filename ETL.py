import requests
import json
import os
import pandas as pd

# Extract
# Extrair os dados da API DummyJson
def extract_data(endpoint):
  response = requests.get(endpoint)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Erro ao extrair os dados da API: {response.status_code}")
    return None

# Load
def load_data(data, resource):
  path = os.path.join("raw", resource)
  os.makedirs(path, exist_ok=True)

  id = data["id"]
  with open(os.path.join(path, f"{id}.json"), "w", encoding='utf-8') as file:
    json.dump(data, file)

# Função para carregar os dados nas respectivas pastas
def loop_load_data(resource):
  base_url = (f"https://dummyjson.com/{resource}/")
  i = 1
  while True:
    data = extract_data(base_url + str(i))
    if data and i <= 10: # Traz os 10 primeiros
      load_data(data, resource)
      i += 1
    elif i > 10:
      break
    else:
      print(f"Erro ao extrair os dados da API: {data}")
      break

# Transform
def transform_data_json_to_csv(endpoint, i):
  with open(f"raw/{endpoint}/{i}.json", "r", encoding='utf-8') as file:
    data = json.load(file)
  
  path = os.path.join("transformed", endpoint)
  os.makedirs(path, exist_ok=True)

  df = pd.DataFrame([data])
  df.to_csv(os.path.join(path, f"{i}.csv"), index = False)


endpoints = ["users", "products"]

def main():
  for endpoint in endpoints:
  #   loop_load_data(endpoint) 
    for i in range(1, 11):
      transform_data_json_to_csv(endpoint, i)

if __name__ == '__main__':
    main()
