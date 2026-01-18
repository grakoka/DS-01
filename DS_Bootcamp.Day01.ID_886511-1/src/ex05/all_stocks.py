import sys

def get_data():
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
    return COMPANIES, STOCKS

def main():
    args = sys.argv[1:]

    if len(args) != 1:
        return

    input_string = args[0].strip()
    if ',,' in input_string:
        return

    expressions = [expr.strip().lower() for expr in input_string.split(',')]
    if '' in expressions:
        return

    COMPANIES, STOCKS = get_data()

    for expr in expressions:
        expr_upper = expr.upper()

        if expr_upper in STOCKS:
            print(f"{expr_upper} is a ticker symbol for {get_company_by_ticker(expr_upper)}")
        elif expr in [company.lower() for company in COMPANIES]:
            company_name = get_company_by_name(expr)
            stock_price = STOCKS[COMPANIES[company_name]]
            print(f"{company_name} stock price is {stock_price}")
        else:
            print(f"{expr.capitalize()} is an unknown company or an unknown ticker symbol")

def get_company_by_ticker(ticker):
    COMPANIES, _ = get_data()
    return next((company for company, company_ticker in COMPANIES.items() if company_ticker == ticker), None)

def get_company_by_name(name):
    COMPANIES, _ = get_data()
    return next((company for company in COMPANIES if name.lower() == company.lower()), None)

if __name__ == "__main__":
    main()
