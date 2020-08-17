import requests
import pandas as pd
import io
from collections import Counter



class Dataset:

    def __init__(self):
        self.original_dataset = self.get_data()
        self.confirmed_cases = self.get_confirmed_cases(self.original_dataset)
        self.get_cases_infos(self.original_dataset)

    def get_data(self):
        request = requests.get('https://covid19.manaus.am.gov.br/wp-content/uploads/Manaus.csv', verify=False)
        content=request.content
        dataset=pd.read_csv(io.StringIO(content.decode('latin-1')), error_bad_lines=False, sep=';')
        return dataset

    def get_confirmed_cases(self, data):
        confirmed_cases = data.loc[data['_classificacao'] == 'Confirmado']
        return confirmed_cases

    def get_cases_infos(self, data):
        possible_values = list(data['_classificacao'])
        keys = Counter(possible_values).keys()
        values = Counter(possible_values).values()
        print(keys)
        print(values)

    def get_attributes_names(self, data);
        pass

data = Dataset()