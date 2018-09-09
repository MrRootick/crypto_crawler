from data.BaseData import BaseData


class OrderBookUpdate(BaseData):
    def __init__(self, sequence_id, bid, ask, timest_ms, trades_sell, trades_buy, sequence_id_end=None):
        self.sequence_id = sequence_id
        self.sequence_id_end = sequence_id_end

        self.bid = bid
        self.ask = ask
        self.timest_ms = timest_ms
        self.trades_sell = trades_sell
        self.trades_buy = trades_buy

    def __str__(self):
        attr_list = [a for a in dir(self) if not a.startswith('__') and
                     not a.startswith("ask") and not a.startswith("bid") and not a.startswith("trades") and not callable(getattr(self, a))]
        str_repr = "["
        for every_attr in attr_list:
            str_repr += every_attr + " - " + str(getattr(self, every_attr)) + " "

        str_repr += "bids - ["
        for b in self.bid:
            str_repr += "\n" + str(b)
        str_repr += "] "

        str_repr += "asks - ["
        for a in self.ask:
            str_repr += "\n" + str(a)
        str_repr += "]"

        str_repr += "]"

        str_repr += "trades_sell - ["
        for b in self.trades_sell:
            str_repr += "\n" + str(b)
        str_repr += "] "

        str_repr += "trades_buy - ["
        for a in self.trades_buy:
            str_repr += "\n" + str(a)
        str_repr += "]"
        return str_repr
