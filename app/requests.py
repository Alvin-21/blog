import urllib.request, json
from .models import Quotes

# Getting the quotes base url
base_url= None

def configure_request(app):
   global base_url
   base_url = app.config['QUOTE_BASE_URL']


def get_quotes():
    
    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_result= None

        if get_quote_response:
            id = get_quote_response.get('id')
            author = get_quote_response.get('author')
            quote = get_quote_response.get('quote')
            quote_result = Quotes(id, author, quote)
        
    return quote_result
