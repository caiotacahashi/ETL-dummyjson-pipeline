import requests
import json
import os

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
def load_data(data, path):
  os.makedirs(path, exist_ok=True)

  id = data["id"]
  with open(f"{path}/{id}.json", "w", encoding='utf-8') as file:
    json.dump(data, file)

# Função para carregar os dados nas respectivas pastas
def loop_load_data(resource):
  base_url = (f"https://dummyjson.com/{resource}/")
  i = 1
  while True and i <= 10: # Traz apenas os 10 primeiros
    data = extract_data(base_url + str(i))
    if data:
      load_data(data, resource)
      i += 1
    else:
      print(f"Erro ao extrair os dados da API: {data}")
      break


endpoints = ["users", "products"]

def main():
  for endpoint in endpoints:
    loop_load_data(endpoint) 

if __name__ == '__main__':
    main()
