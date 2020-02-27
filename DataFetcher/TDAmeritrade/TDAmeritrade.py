import urllib

def read_api_key(file="APIKEY.apikey"):
    f = open(file, 'r')
    apikey = f.readline()
    f.close()
    return apikey

def get_option_chain(symbol):
    print("Getting option chain for symbol")




if __name__ == "__main__":
    print(read_api_key())
    print("")