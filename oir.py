import random
import time
import sys


def slow_print(text, delay=0.15):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


slow_print("Welcome to a Simple Stockmarket Simulator. Type <start> to begin. If you would like an explanation on how to play type 'help' ")
start = input()

if start == "start" or start == "Start":
    slow_print("Day 1")
    day = 1
    slow_print("Starting wallet: $157")
    stock_price = 100
    wallet = 157
    slow_print(f"Beginning stock price: ${stock_price}")
    while True:
        wallet = 157
        rate = random.randint(0, 10)

        if rate == 0:
            rate = 0.95
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 1:
            rate = 0.96
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 2:
            rate = 0.97
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 3:
            rate = 0.98
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 4:
            rate = 0.99
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 5:
            rate = 1
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 6:
            rate = 1.01
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 7:
            rate = 1.02
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 8:
            rate = 1.03
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 9:
            rate = 1.04
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')
        if rate == 10:
            rate = 1.05
            stock_price = rate * stock_price
            slow_print(f'Rate: {rate}')
            slow_print(f'New stock price ${stock_price}')

        slow_print(f'Day {day}')
        day = day + 1


elif start == "help" or start == "Help":
    slow_print("stock")

elif start != "start" or start != "help" or start != "Help" or start != "Start":
    slow_print("Deleting system.32")
