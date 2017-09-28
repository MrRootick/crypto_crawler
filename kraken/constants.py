KRAKEN_GET_TICKER = "https://api.kraken.com/0/public/Ticker?pair="

# OHLC ~ canddle stick urls
# https://api.kraken.com/0/public/OHLC?pair=XXRPXXBT&since=1497916800&interval=15
KRAKEN_GET_OHLC = "https://api.kraken.com/0/public/OHLC?pair="

# https://api.kraken.com/0/public/Depth?pair=XETHXXBT
KRAKEN_GET_ORDER_BOOK = "https://api.kraken.com/0/public/Depth?pair="

# https://api.kraken.com/0/public/Trades?pair=XETHXXBT&since=1501693512
KRAKEN_GET_HISTORY = "https://api.kraken.com/0/public/Trades?pair="

KRAKEN_CURRENCIES = ["DASHXBT", "XETHXXBT", "XLTCXXBT", "XXRPXXBT", "BCHXBT", "XETCXXBT"]

KRAKEN_CANCEL_ORDER = "https://api.kraken.com/0/private/CancelOrder"
KRAKEN_BUY_ORDER = "https://api.kraken.com/0/private/AddOrder"
KRAKEN_SELL_ORDER = "https://api.kraken.com/0/private/AddOrder"
KRAKEN_CHECK_BALANCE = "https://api.kraken.com/0/private/Balance"
