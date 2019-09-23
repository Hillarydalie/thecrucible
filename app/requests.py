import urllib.request,json
from config import Config
from .models import Quotes

quotes_url = Config.QUOTE_URL

def configure_request(app):
    pass
def get_quote():
     get_randomquotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

     with urllib.request.urlopen(get_randomquotes_url) as url:
       quotes = url.read()
       get_sources_response = json.loads(quotes)
       print(quotes)
    return get_sources_response