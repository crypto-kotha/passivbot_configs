from os import system
from time import sleep

# Dictionary of users, their symbols, and corresponding paths
user_symbols_paths = {
    "bybit_01": {
        "symbols": ["LDOUSDT", "AKROUSDT", "ALGOUSDT", "HBARUSDT", "1000LUNCUSDT", "DYDXUSDT", "XRPUSDT", "DOGEUSDT", "SHIB1000USDT", "GALAUSDT"],
        "path_prefix": "configs/live/bybit_01/"
    }
}

# Iterate through each user, symbols, and paths
for user, data in user_symbols_paths.items():
    for symbol in data["symbols"]:
        # Construct the command and run it using the screen command
        command = f"python3 passivbot.py {user} {symbol} {data['path_prefix']}{symbol}.json"
        screen_name = f"{user}_{symbol}"
        system(f"screen -dmS {screen_name} bash -c '{command}'")
        print(f"{screen_name} started...")
        sleep(1)

print('All Bots are running :)')
