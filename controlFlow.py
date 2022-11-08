#Built-in Modules
import time
#My Modules
from notifications import Text as txt
from settings import client
import functions
import model

i = 1
while i == 1:
    it = 1
    while it == 1:
        try:
            print(txt.menu)
            order = input(txt.inputLabel)
            print(txt.shortDashDivider)

            if order == "s":
                client.new_order(**model.open_short_order)
                print(txt.shortPosition)
                functions.get_balance()
                
            elif order == "l":
                client.new_order(**model.open_long_order)
                print(txt.longPosition)
                functions.get_balance()

            elif order == "sh":
                client.new_order(**model.open_short_order)
                time.sleep(0.2)
                try:
                    client.new_order(**functions.stop_order("long"))
                except Exception as e:
                    print(e)
                    print("Try again!")
                    time.sleep(0.2)
                    client.new_order(**model.close_short_order)

                print(txt.shortHedge)
                functions.get_balance()

            elif order == "lh":
                client.new_order(**model.open_long_order)
                try:
                    client.new_order(**functions.stop_order("short"))
                except Exception as e:
                    print(e)
                    print("Try again!")
                    time.sleep(0.2)
                    client.new_order(**model.close_long_order)

                print(txt.longHedge)
                functions.get_balance()

            elif order == "cs":
                close_short = client.new_order(**model.close_short_order)
                print(txt.shortPositionClosed)
                functions.get_balance()

            elif order == "cl":
                client.new_order(**model.close_long_order)
                print(txt.longPositionClosed)
                functions.get_balance()

            elif order == "hgl":
                try:
                    client.new_order(**functions.stop_order("m_long"))
                except Exception as e:
                    print(e)
                    print("Try again!")
                print(txt.longHedge)
                functions.get_balance()

            elif order == "hgs":
                try:
                    client.new_order(**functions.stop_order("m_short"))
                except Exception as e:
                    print(e)
                    print("Try again!")
                print(txt.hedgeShortOrder)
                functions.get_balance()

            elif order == "co":
                client.cancel_open_orders(**model.cancel_all_orders)
                print(txt.ordersCanceled)
                functions.get_balance()

            elif order == "ns":
                try:
                    client.new_order(**model.close_short_order)
                except Exception as e:
                    print("???")
                time.sleep(0.2)
                try:
                    client.new_order(**model.close_long_order)
                except Exception as e:
                    print("???")
                time.sleep(0.2)
                try:
                    client.new_order(**model.open_short_order)
                except Exception as e:
                    print("???")
                time.sleep(0.2)
                try:
                    client.cancel_open_orders(**model.cancel_all_orders)
                except Exception as e:
                    print("???")
                time.sleep(0.2)
                try:
                    client.new_order(**functions.stop_order("long"))
                except Exception as e:
                    print(e)
                    print("Try again!")
                print(txt.renewShortLong)
                functions.get_balance()

            elif order == "nl":
                try:
                    client.new_order(**model.close_long_order)
                except Exception as e:
                    print("???")
                time.sleep(0.2)
                try:
                    client.new_order(**model.close_short_order)
                except Exception as e:
                    print("???")
                time.sleep(0.2)
                try:
                    client.new_order(**model.open_long_order)
                except Exception as e:
                    print("???")
                time.sleep(0.2)
                try:
                    client.cancel_open_orders(**model.cancel_all_orders)
                except Exception as e:
                    print("???")
                time.sleep(0.2)
                try:
                    client.new_order(**functions.stop_order("short"))
                except Exception as e:
                    print(e)
                    print("Try again!")
                print(txt.renewLongShort)
                functions.get_balance()

            elif order == "f":
                it = 0
                print(txt.finishDivider)
                functions.get_balance()
            
            elif order == "a":
                print(txt.about)
        except Exception as e:
            print(e)

    print(txt.continueText)
    x = input()
    if x == "n":
        i = 0

print(txt.gameOverDivider)
