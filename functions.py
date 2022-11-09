#Built-in Modules
from decimal import Decimal
#External Modules
from termcolor import colored
#My Modules
from settings import client, coinPair, percent
from notifications import Text as txt
import model

def get_balance():
    var_balance = client.balance()[6]["balance"]
    print(txt.starDivider)
    print("Balance: " + colored(var_balance, "red"))
    print(txt.starDivider)

def get_tick_size(symbol):
    info = client.exchange_info()
    for sy in info["symbols"]:
        if sy["pair"] == symbol:
            tickSize = sy["filters"][0]['tickSize']
            return tickSize

def get_entry_price(symbol, side):
    futures = client.get_position_risk(symbol=symbol)
    side = side
    if side == "short":
        for f in futures:
            if f["positionSide"] == "SHORT":
                return f["entryPrice"]
    elif side == "long":
        for f in futures:
            if f["positionSide"] == "LONG":
                return f["entryPrice"]

def get_mark_price(symbol):
    res = client.mark_price(symbol)
    return res["markPrice"]

def round_step_size(quantity, size):
    quantity = Decimal(quantity)
    return float(quantity - quantity % Decimal(size))

#Stop-limit prices
tick_size = float(get_tick_size(coinPair))
def stop_price(side, base):
    open_position_entry_price = get_entry_price(coinPair, side)
    current_market_price = get_mark_price(coinPair)
    if side == "short" and base == "position_price":
        stop_short_price = float(open_position_entry_price) * (1 + percent / 100)
        stop_short_price_sized = round_step_size(stop_short_price, tick_size)
        return stop_short_price_sized
    elif side == "long" and base == "position_price":
        stop_long_price = float(open_position_entry_price) * (1 - percent / 100)
        stop_long_price_sized = round_step_size(stop_long_price, tick_size)
        return stop_long_price_sized
    elif side == "short" and base == "market_price":
        stop_short_price = float(current_market_price) * (1 + percent / 100)
        stop_short_price_sized = round_step_size(stop_short_price, tick_size)
        return stop_short_price_sized
    elif side == "long" and base == "market_price":
        stop_long_price = float(current_market_price) * (1 - percent / 100)
        stop_long_price_sized = round_step_size(stop_long_price, tick_size)
        return stop_long_price_sized

#Stop-limit orders
def stop_order(side):
    if side == "long":
        price = str(stop_price("short", "position_price")),
        return model.get_order_model(1, price)
    elif side == "short":
        price =  str(stop_price("long", "position_price"))
        return model.get_order_model(2, price)
    elif side == "m_long":
        price = str(stop_price("short", "market_price"))
        return model.get_order_model(3, price)
    elif side == "m_short":
        price = str(stop_price("long", "market_price"))
        return model.get_order_model(4, price)