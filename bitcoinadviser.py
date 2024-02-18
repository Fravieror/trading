import requests
import json
import datetime

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']

def main():
    try:
        with open("previous_price.txt", "r") as file:
            previous_price = float(file.read())
    except FileNotFoundError:
        previous_price = None

    current_price = fetch_bitcoin_price()
    print(f"Current Bitcoin Price: ${current_price}")

    if previous_price is not None:
        if current_price < previous_price:
            with open("logfile.log", "a") as log_file:
                log_file.write(f"{datetime.datetime.now()}, price," + str(current_price) + "\n")
            print("Bitcoin price is lower than the last check. It might be a good time to buy.")
        else:
            with open("logfile.log", "a") as log_file:
                log_file.write(f"{datetime.datetime.now()}, price:" + str(current_price) + "\n")
            print("Bitcoin price is higher than or equal to the last check. Maybe wait for a better price.")

    with open("previous_price.txt", "w") as file:
        file.write(str(current_price))

if __name__ == "__main__":
    main()