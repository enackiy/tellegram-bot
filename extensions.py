class Error(Exception):
    pass

class APIException(Error):
	pass

    

def get_price(base, quote, amount):
	url = f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}'
	response = requests.get(url)
	chislo=json.loads(response.text)[f'{str(quote)}']*float(amount)
	return(chislo)