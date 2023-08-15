# this is multi balance and multi timeframe backtest command. put this fill into passivbot main directory.
import subprocess

configs = ["test1", "test2", "test3"]  # this is config.json. for testing perpose.

symbols = [
    "SHIB1000USDT",  # Add more symbols "SHIB1000USDT","DOGEUSDT","GALAUSDT",
]

start_dates = ["2021-01-01", "2021-07-01", "2021-11-13"]  # main time range, some uptrend, crash zone.
end_date = "2023-08-13"
user = "bybit_01"
leverage = "0.25"
balance_values = ["100", "1000"]

# Function to execute backtest for a list of balance values
def run_backtest_for_balance(command, symbol, start_date):
    for config in configs:
        for balance in balance_values:
            full_command = command + [
                "-u", user,
                "-s", symbol,
                "-lw", leverage,
                "-m", "future",
                "-sb", balance,
                f"configs/live/{config}.json",
                "--start_date", start_date,
                "--end_date", end_date
            ]
            subprocess.run(full_command)

# Command for the backtest
base_command = [
    "python3",
    "backtest.py",
]

# Run the backtest for each starting date and symbol
for start_date in start_dates:
    for symbol in symbols:
        run_backtest_for_balance(base_command, symbol, start_date)
