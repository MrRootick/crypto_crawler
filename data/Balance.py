from BaseData import BaseData
import json
from constants import ARBITRAGE_CURRENCY
from enums.exchange import EXCHANGE
from utils.currency_utils import get_currency_id_from_kraken, get_currency_id_from_bittrex, get_currency_id_from_poloniex

"""
time_of_last_update,

    pair_id: volume,
    pair_id: volume,
    ... ,
    pair_id: volume
"""


class Balance(BaseData):
    def __init__(self, exchange_id, last_update, initial_balance):
        self.exchange_id = exchange_id
        self.last_update = last_update
        self.balance = initial_balance

    @classmethod
    def from_poloniex(cls, last_update, json_document):

        json_object = json.load(json_document)

        initial_balance = {}

        """
         {u'XVC': u'0.00000000', u'SRCC': u'0.00000000', u'EXE': u'0.00000000',

         FIXME NOTE: those bastards always return ALL coins not very efficient
        """

        for currency_name in json_object:
            currency_id = -1
            try:
                currency_id = get_currency_id_from_poloniex(currency_name)
            except Exception, e:
                print "Balance.Poloniex: Unknown currency: ", currency_name, str(e)

            if currency_id in ARBITRAGE_CURRENCY:
                volume = json_object[currency_name]
                initial_balance[currency_id] = volume

        return Balance(EXCHANGE.POLONIEX, last_update, initial_balance)

    @classmethod
    def from_kraken(cls, last_update, json_document):

        json_object = json.load(json_document)

        initial_balance = {}

        """
        {u'DASH': u'33.2402410500', u'BCH': u'22.4980093900', ... }
        """

        for currency_name in json_object:
            currency_id = -1

            try:
                currency_id = get_currency_id_from_kraken(currency_name)
            except Exception, e:
                print "Balance.Kraken: Unknown currency: ", currency_name, str(e)

            if currency_id in ARBITRAGE_CURRENCY:
                volume = json_object[currency_name]
                initial_balance[currency_id] = volume

        return Balance(EXCHANGE.KRAKEN, last_update, initial_balance)

    @classmethod
    def from_bittrex(cls, last_update, json_document):

        # json_object = json.load(json_document)

        initial_balance = {}

        """
        [{u'Available': 21300.0, u'Currency': u'ARDR', u'Balance': 21300.0, u'Pending': 0.0,
        u'CryptoAddress': u'76730d86115b49b9b7f71578feb35b7da1ca6c13e5f745aa9b630707f5439e68'},

        {u'Available': 49704.04069438, u'Currency': u'BAT', u'Balance': 49704.04069438, u'Pending': 0.0,
        u'CryptoAddress': None},
        """

        for entry in json_document:
            currency_name = entry["Currency"]
            currency_id = -1
            try:
                currency_id = get_currency_id_from_bittrex(currency_name)
            except Exception, e:
                print "Balance.Bittrex: Unknown currency: ", currency_name, str(e)

            if currency_id in ARBITRAGE_CURRENCY:
                volume = entry["Balance"]
                initial_balance[currency_id] = volume

        return Balance(EXCHANGE.BITTREX, last_update, initial_balance)

    def is_there_disbalance(self, pair_id, threshold):
        # FIXME check accros all exchange
        return True
