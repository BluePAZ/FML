import urllib
import urllib.parse as urlparse
from urllib.parse import urlencode
from datetime import timezone
import datetime
dt = datetime.datetime(2015, 10, 19)

timestamp = dt.replace(tzinfo=timezone.utc).timestamp()

class Equity():
    symbol = ""
    def __init__(self, symbol):
        self.symbol = symbol
    def print(self):
        print(self.symbol)


class RequestBuilder:
    _base_url = "https://api.tdameritrade.com"
    def __init__():
        pass
    def HistoricalPrice():
        return 42

def read_api_key(file="APIKEY.apikey"):
    f = open(file, 'r')
    apikey = f.readline()
    f.close()
    return apikey

def request_builder(symbol):
    pass


def get_option_chain(symbol):
    print("Getting option chain for symbol")




if __name__ == "__main__":
    print(read_api_key())
    AMD = Equity("AMD")
    AMD.print()
    print("")