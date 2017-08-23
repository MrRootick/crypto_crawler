from constants import KRAKEN_GET_ORDER_BOOK
from data.OrderBook import OrderBook
from debug_utils import should_print_debug
from data_access.internet import send_request


def get_order_book_kraken(currency, timest):
    # https://api.kraken.com/0/public/Depth?pair=XETHXXBT
    final_url = KRAKEN_GET_ORDER_BOOK + currency

    if should_print_debug():
        print final_url

    err_msg = "get_order_book_kraken called for {pair} at {timest}".format(pair=currency, timest=timest)
    r = send_request(final_url, err_msg)

    if r is not None and "result" in r:
        if currency in r["result"]:
            return OrderBook.from_kraken(r["result"][currency], currency, timest)

    return None
