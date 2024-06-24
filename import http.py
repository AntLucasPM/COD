import http.client
import json
import pandas as pd

lista_produtos = []

conta = 0

for page in range(1, 50):
    conta += 1
    listapage = f"/produtos?pagina={page}"

    conn = http.client.HTTPSConnection("api.fbits.net")
    payload = ''
    headers = {
    'Authorization': 'Basic mamoe-0f0e1c0f-aa6c-4bfa-beeb-f254a8e04db7'
    }
    conn.request("GET", listapage, payload, headers)
    res = conn.getresponse()
    print(f"Pagina {conta} resposta ", res.status)
    dados = json.loads(res.read())
    
    try:
        for produto in dados:
            if "COMB" in produto["sku"]:
                lista_produtos.append(produto["sku"])
    except:
        pass

df = pd.DataFrame(lista_produtos)
df.to_excel(fr'C:\Users\Usuario\Downloads\produtos_kit.xlsx', index=False)
print(df)

lista = pd
# print("")
# print("SEPARA***")
# print("")
# print("")

# conn = http.client.HTTPSConnection("api.fbits.net")
# payload = json.dumps({
# "identificadores": lista_produtos})
# headers = {
# 'Authorization': 'Basic mamoe-0f0e1c0f-aa6c-4bfa-beeb-f254a8e04db7',
# 'Content-Type': 'application/json'
# }
# conn.request("DELETE", "/produtos?tipoIdentificador=Sku", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))