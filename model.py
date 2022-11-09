#My Modules
from settings import coinPair, amount

cancel_all_orders = {
    "symbol": coinPair
}

open_long_order = {
    "symbol": coinPair,
    "side": "BUY",
    "type": "MARKET",
    "positionSide": "LONG",
    "quantity": amount
}

close_long_order = {
    "symbol": coinPair,
    "side": "SELL",
    "type": "MARKET",
    "positionSide": "LONG",
    "quantity": amount
}

open_short_order = {
    "symbol": coinPair,
    "side": "SELL",
    "type": "MARKET",
    "positionSide": "SHORT",
    "quantity": amount
}

close_short_order = {
    "symbol": coinPair,
    "side": "BUY",
    "type": "MARKET",
    "positionSide": "SHORT",
    "quantity": amount,
}

def get_order_model(order, stop_price):

    if order == 1:
        stop_market_long_order = {
            "symbol": coinPair,
            "side": "BUY",
            "type": "STOP_MARKET",
            "timeInForce": 'GTC',
            "stopPrice": stop_price,
            "positionSide": "LONG",
            "quantity": amount
        }
        return stop_market_long_order

    elif order == 2:
        stop_market_short_order = {
            "symbol": coinPair,
            "side": "SELL",
            "type": "STOP_MARKET",
            "timeInForce": 'GTC',
            "stopPrice": stop_price,
            "positionSide": "SHORT",
            "quantity": amount
        }
        return stop_market_short_order

    elif order == 3:
        stop_market_m_long_order = {
            "symbol": coinPair,
            "side": "BUY",
            "type": "STOP_MARKET",
            "timeInForce": 'GTC',
            "stopPrice": stop_price,
            "positionSide": "LONG",
            "quantity": amount
        }
        return stop_market_m_long_order
        
    elif order == 4:
        stop_market_m_short_order = {
            "symbol": coinPair,
            "side": "SELL",
            "type": "STOP_MARKET",
            "timeInForce": 'GTC',
            "stopPrice": stop_price,
            "positionSide": "SHORT",
            "quantity": amount
        }
        return stop_market_m_short_order