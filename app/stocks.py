


from pandas import read_csv

from app.alpha import API_KEY


def fetch_stock_data(symbol="NFLX"):
    """Returns a pandas dataframe with the stock data"""

    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv"

    return read_csv(request_url)



if __name__ == "__main__":

    print("STOCKS REPORT...")

    selected_symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
    print("SYMBOL:", selected_symbol)

    df = fetch_stock_data(selected_symbol)

    print(df.columns)
    print(df.head())
    #breakpoint()

    # CHALLENGE A:
    # print the latest closing date and price

    latest = df.iloc[0]

    #print(latest["timestamp"])
    #print(latest["close"])
    print("LATEST:", '${:,.2f}'.format(latest["adjusted_close"]), "as of", latest["timestamp"])

    # Challenge B
    #
    # What is the highest high price (formatted as USD)?
    # What is the lowest low price (formatted as USD)?

    print("HIGH:", '${:,.2f}'.format(df["high"].max()))
    print("LOW:", '${:,.2f}'.format(df["low"].min()))
