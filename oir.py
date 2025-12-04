import random
import time
import sys

def slow_print(text, delay=0.15):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


slow_print("Welcome to a Simple Stockmarket Simulator. Type 'start' to begin. If you would like an explanation on how to play type 'help' ")
start = input()

if start == "start" or start == "Start":
    slow_print("Day 1")
    day = 1
    slow_print("Starting wallet: $157")
    stock_price = 100
    wallet = 157
    slow_print(f"Beginning stock price: ${stock_price}")
    stock = 0
    while True:
        rate = random.randint(0, 10)


        if rate == 0:
            rate = 0.95
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash ${wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock_price * stock
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif stock != 0:
                    slow_print(f"Would you like to buy or sell? ")
                    buy_sell = input('')
                    if buy_sell == "buy" or buy_sell == "Buy":
                        slow_print('how much would you like to buy? ')
                        stock_purchase = int(input(''))
                        stock = stock_purchase
                        stock_total_price = stock * stock_price
                        slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                    elif buy_sell == "sell" or buy_sell == "Sell":
                        slow_print('how much would you like to sell? ')
                        stock_sell = int(input(''))
                        stock = stock - stock_sell
                        stock_total_price = stock * stock_price
                        wallet = wallet + stock_total_price
                        wallet = wallet + stock_total_price
                        slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 1:
            rate = 0.96
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 2:
            rate = 0.97
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 3:
            rate = 0.98
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 4:
            rate = 0.99
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 5:
            rate = 1
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 6:
            rate = 1.01
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 7:
            rate = 1.02
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 8:
            rate = 1.03
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 9:
            rate = 1.04
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        if rate == 10:
            rate = 1.05
            stock_price = rate * stock_price
            slow_print(f"Today's rate: {rate}")
            slow_print(f'New stock price ${stock_price}')
            if stock == 0:
                slow_print(f"Would you like you buy stock? (your cash {wallet}) (y/n)")
                yn = input('')
                if yn == "y":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
            elif stock != 0:
                slow_print(f"Would you like to buy or sell? ")
                buy_sell = input('')
                if buy_sell == "buy" or buy_sell == "Buy":
                    slow_print('how much would you like to buy? ')
                    stock_purchase = int(input(''))
                    stock = stock_purchase
                    stock_total_price = stock * stock_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")
                elif buy_sell == "sell" or buy_sell == "Sell":
                    slow_print('how much would you like to sell? ')
                    stock_sell = int(input(''))
                    stock = stock - stock_sell
                    stock_total_price = stock * stock_price
                    wallet = wallet + stock_total_price
                    slow_print(f"You now have {stock} stock! This totals at a price of ${stock_total_price}")

        slow_print(f'Day {day}')
        day = day + 1



elif start == "help" or start == "Help":
    slow_print("stock")

elif start != "start" or start != "help" or start != "Help" or start != "Start":
    slow_print("Deleting system.32")
