import requests
import pandas as pd
import io
from collections import Counter



class Dataset:

    def __init__(self):
        self.original_dataset = self.get_data()
        self.confirmed_cases = self.get_confirmed_cases(self.original_dataset)
        print(self.get_cases_infos(self.original_dataset))
        #self.attributes = self.get_attributes_names(self.original_dataset)
        #self.min_max_dates(self.original_dataset)
        self.cleaned_data, self.after_clean_number = self.clean_data(self.original_dataset)
        #self.recovered_percentage(self.cleaned_data)
        #list_keys, list_values, most_affectec_sex = self.m_and_f_confirmed_percentage(self.cleaned_data)
        #most_affected_neighbor = self.most_affected_neighborhood(self.cleaned_data)

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
        cleaned_data = data[['_idade','_sexo','_bairro','_classificacao','_conclusao','_dt_notificacao','_teste_pcr','_teste_anticorpo','_teste_antigeno','_teste_igm','_teste_igg']]
        initial_number = cleaned_data.shape[0]
        print(f'\nInitial number of lines: {initial_number}')
        cleaned_data = cleaned_data.dropna()
        after_clean_number = cleaned_data.shape[0]
        print(f'After cleaning, number of lines: {after_clean_number}')
        cleaned_data = cleaned_data.reset_index(drop=True)
        return cleaned_data, after_clean_number

    def recovered_percentage(self, data):
        # Poercentagem de individuos recuperados em relação a todos os casos confirmados
        possible_values = list(data['_conclusao'])
        keys = Counter(possible_values).keys()
        values = Counter(possible_values).values()
        print(f'\nrecovered percentage keys: {keys}')
        print(f'recovered percentage values: {values}')
        values_list = list(values)
        percentage = (values_list[0]/(sum(values_list)))*100 
        print(f'recovered percentage: {percentage:.2f}%')
        return (keys, values, percentage)

    def m_and_f_confirmed_percentage(self, data):
        possible_values = list(data['_sexo'])
        keys = Counter(possible_values).keys()
        values = Counter(possible_values).values()
        print(keys)
        print(values)
        m_f_keys = list(keys)
        m_f_values = list(values)
        bigger_values = max(m_f_values)
        index = m_f_values.index(bigger_values)
        most_affected = m_f_keys[index]
        print(f'Os casos acometeram mais: {most_affected}')
        return m_f_keys, m_f_values, most_affected

    def most_affected_neighborhood(self, data):
        possible_values = list(data['_bairro'])
        keys = Counter(possible_values).keys()
        values = Counter(possible_values).values()
        print(keys)
        print(values)
        neighbor_keys = list(keys)
        neighbor_values = list(values)
        bigger_values = max(neighbor_values)
        index = neighbor_values.index(bigger_values)
        most_affected = neighbor_keys[index]
        print(f'O bairro mais afetado foi: {most_affected}')
        return most_affected

data = Dataset()