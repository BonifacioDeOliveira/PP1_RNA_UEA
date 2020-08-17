import requests
import pandas as pd
import io

print('\nVai baixar\n')
url="https://covid19.manaus.am.gov.br/wp-content/uploads/Manaus.csv"
request_csv=requests.get(url, verify=False).content
print('pega o results \n')
#print(request_csv)
csv=pd.read_csv(io.StringIO(request_csv.decode('utf-8')))
print(csv.head())