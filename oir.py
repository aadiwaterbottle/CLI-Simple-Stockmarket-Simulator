import random

start = input("Welcome to a Simple Stock Market Simulator. Type <start> to begin. If you would like an explanation on how to play type 'help' ")

if start == "start" or start == "Start":
    print("Day 1")
    print("Starting wallet: $157")
    print("Beginning stock price: 10")
    wallet = 157
    stock_price = 10 * random.randint(5, 10)
    print(f'New stock price ${stock_price}')

elif start == "help" or start == "Help":
    print("stock")

elif start != "start" or start != "help" or start != "Help" or start != "Start":
    print("Deleting system.32")
