import requests
import json
class ConvertionException(Exception):
    pass

class CurrencyConverter():
    @staticmethod
    def convert(base, quote, amount, values):
        if base == quote:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')
        try:
            am = float(amount)
        except:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        url = 'https://api.currencyapi.com/v3/latest?apikey=pv9asoEfxOElSEsHEoVaEYidGriarlt9CFJugemg&currencies=EUR%2CUSD%2CCAD%2CRUB%2CJPY'
        res = requests.get(url)
        js = json.loads(res.content)

        try:
            ticker_base = js['data'][base]['value']
        except:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            ticker_base = js['data'][quote]['value']
        except:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        result = 1 / js['data'][base]['value'] * js['data'][quote]['value'] * int(amount)
        return result
