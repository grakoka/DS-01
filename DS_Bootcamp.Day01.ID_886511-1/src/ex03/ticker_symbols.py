import sys

def main():

    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    args = sys.argv[1:]

    if len(args) != 1:
        return

    ticker = args[0].upper()

    company_name = next((company for company, ticker_symbol in COMPANIES.items() if ticker_symbol == ticker), None)  

    if company_name:
        stock_price = STOCKS[ticker]
        print(f'{company_name} {stock_price}')
    else:
        print('Unknown ticker')

if __name__ == '__main__':
    main()        


