# python3 opt.py #(will start signle optimize process)

import subprocess

def run_optimize(symbol, backtest_config, optimize_config, start_date, end_date):
    command = [
        "python3",
        "optimize.py",
        "-s", symbol,
        "-b", backtest_config,
        "-o", optimize_config,
        "--start_date", start_date,
        "--end_date", end_date
    ]
    subprocess.run(command, check=True)

def main():
    symbols = ["ADAUSDT", "XRPUSDT", "MATICUSDT", "XLMUSDT", # qty precision 1.0 list
    "NEARUSDT", "APTUSDT", "ARBUSDT", "LDOUSDT", "OPUSDT", "DYDXUSDT", # low qty pct precision 0.1 list
    "HBARUSDT", "SHIB1000USDT", "DOGEUSDT", "GALAUSDT", "GRTUSDT", "CHZUSDT", "ALGOUSDT", "1000LUNCUSDT", "1000PEPEUSDT", # top 100 small coin
]

    backtest_config = "configs/backtest/default.hjson"
    optimize_config = "configs/optimize/default.hjson"
    start_date = "2021-01-01"
    end_date = "2023-08-19"

    for symbol in symbols:
        run_optimize(symbol, backtest_config, optimize_config, start_date, end_date)

if __name__ == "__main__":
    main()
