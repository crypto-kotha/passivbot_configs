import subprocess

symbols = [
    "ADAUSDT", "XRPUSDT", "MATICUSDT", "XLMUSDT", # high qty pct precision 1.0 list
    "NEARUSDT" "APTUSDT", "ARBUSDT", "LDOUSDT", "OPUSDT", "DYDXUSDT", # low qty pct precision 0.1 list
    "HBARUSDT", "SHIB1000USDT", "DOGEUSDT", "GALAUSDT", "GRTUSDT", "CHZUSDT", "ALGOUSDT", "1000LUNCUSDT", "1000PEPEUSDT", # top 100 small coin
]

folders = ["clock1", "recursive", "neat", "static"]  # set configs/live/List of config folders

start_dates = ["2021-01-01"]
end_date = "2023-08-19"
user = "bybit_01"

long_leverage_values = ["0.20"] # ["0.1", "0.15", "0.20", "1.0"]

short_leverage_values = ["0.15"]

balance_values = ["250"]  # ["250", "500", "1000"]

def run_backtest_for_balance(command, symbol, start_date, short_leverage, long_leverage):
    for folder in folders:
        for balance in balance_values:
            full_command = command + [
                "-u", user,
                "-s", symbol,
                "-sw", short_leverage,
                "-lw", long_leverage,
                "-m", "future",
                "-sb", balance,
                f"configs/live/{folder}/{symbol}.json",
                "--start_date", start_date,
                "--end_date", end_date
            ]
            subprocess.run(full_command)

# Command for the backtest
base_command = [
    "python3",
    "backtest.py",
]

# Run the backtest for each starting date, symbol, short_leverage, and long_leverage value
for start_date in start_dates:
    for symbol in symbols:
        for short_leverage_value in short_leverage_values:
            for long_leverage_value in long_leverage_values:
                run_backtest_for_balance(base_command, symbol, start_date, short_leverage_value, long_leverage_value)
