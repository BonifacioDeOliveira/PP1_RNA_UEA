import requests
import pandas as pd
import io
from collections import Counter



class Dataset:

    def __init__(self):
        self.original_dataset = self.get_data()
        self.confirmed_cases = self.get_confirmed_cases(self.original_dataset)
        self.cleaned_data = None
        #self.get_cases_infos(self.original_dataset)
        self.attributes = self.get_attributes_names(self.original_dataset)
        #self.min_max_dates(self.original_dataset)
        self.clean_data(self.original_dataset)

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
        return keys, values

    def get_attributes_names(self, data):
        original_attributes = data.columns.tolist()
        removed_underline = [i[1:] for i in original_attributes]
        return removed_underline

    def min_max_dates(self, data):
        # the date is given by dt_notificacao attribute
        dates = pd.to_datetime(data['_dt_notificacao'])
        min_date = dates.min()
        max_date = dates.max()
        return min_date, max_date

    def clean_data(self, data):
        cleaned_data = data[['_idade','_faixa etária','_sexo','_bairro','_classificacao','_dt_notificacao']]
        print(f'Initial number of lines: {cleaned_data.shape[0]}')
        cleaned_data = cleaned_data.dropna()
        print(f'After cleaning, number of lines: {cleaned_data.shape[0]}')
        cleaned_data = cleaned_data.reset_index(drop=True)
        return cleaned_data

    def count_data(self, data):
        pass

    def m_and_f_confirmed_percentage(self, data):
        pass




data = Dataset()