import time
import requests
import sqlite3

SYMBOL = "BTC-USD"
MARKET = "BITTREX"


def get_ticker(market_api: str, request_threshold: float, market: str, request_numbers: int):
    """ Function to fetch ASK-BID values from API call to the market """
    value = 0

    while (value := value + 1) < request_numbers + 1:

        r = requests.get(market_api)
        data = r.json()

        sqliteConnection = sqlite3.connect(f'{market}_TICKER.sqlite')
        cursor = sqliteConnection.cursor()
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {market} (TIME, SYMBOL, BID, ASK)"
        )
        cursor.execute(
            f"INSERT INTO {market}(TIME, SYMBOL, BID, ASK) VALUES(?,?,?,?)",
            (time.time(), data["symbol"], data["bidRate"], data["askRate"])
        )
        sqliteConnection.commit()
        sqliteConnection.close()

        time.sleep(request_threshold)


get_ticker(
    market_api=f"https://api.bittrex.com/v3/markets/{SYMBOL}/ticker",
    request_threshold=5.0,
    market=MARKET,
    request_numbers=3
)
