#External Modules
from binance.um_futures import UMFutures
#My Modules
from credentials import api_key, api_secret
from notifications import Text as txt

client = UMFutures(key=api_key, secret=api_secret)
coin = input(txt.inputCoin).upper()
coinPair = f"{coin}USDT"
amount = float(input(txt.inputAmount))
percent = float(input(txt.inputPercent))