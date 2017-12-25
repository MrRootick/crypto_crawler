import multiprocessing
from enums.currency import CURRENCY
from enums.currency_pair import CURRENCY_PAIR

SECONDS_IN_WEEK = 604800
SECONDS_IN_DAY = 86400

HTTP_TIMEOUT_SECONDS = 25
DEAL_MAX_TIMEOUT = 10

ZERO_BALANCE = 0.0
ARBITRAGE_CURRENCY = CURRENCY.values()
ARBITRAGE_PAIRS = CURRENCY_PAIR.values()

CACHE_HOST = "127.0.0.1"
CACHE_PORT = 6379

CORE_NUM = multiprocessing.cpu_count()
POOL_SIZE = 8 * CORE_NUM

LOGS_FOLDER = "./logs/"
