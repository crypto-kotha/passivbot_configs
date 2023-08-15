import subprocess

folders = ["clock", "recursive", "neat", "static"]  # set configs/live/List of config folders

# List of all bybit symbols and config.json name will be same
symbols = [
    "1000LUNCUSDT", "1000PEPEUSDT", "SHIB1000USDT", "AAVEUSDT",
    "ACHUSDT", "ADAUSDT", "AGIXUSDT", "AGLDUSDT", "AKROUSDT",
    "ALGOUSDT", "ALPHAUSDT", "ANKRUSDT", "APTUSDT",
    "ARBUSDT", "ARPAUSDT", "ATOMUSDT", "AVAXUSDT",
    "BCHUSDT", "BELUSDT", "BNBUSDT",
    "CELOUSDT", "CFXUSDT", "CHZUSDT", "COMPUSDT", "CRVUSDT",
    "DOGEUSDT", "DOTUSDT", "DYDXUSDT", "ENSUSDT",
    "ETCUSDT", "FETUSDT", "FILUSDT", "FTMUSDT", "GALAUSDT",
    "GMTUSDT", "GRTUSDT", "ICPUSDT",
    "INJUSDT", "JASMYUSDT", "KAVAUSDT", "KEYUSDT",
    "LDOUSDT", "LINAUSDT", "LINKUSDT", "LTCUSDT",
    "LUNA2USDT", "MANAUSDT", "MASKUSDT", "MATICUSDT",
    "MKRUSDT", "MTLUSDT", "NEARUSDT", "OCEANUSDT",
    "OPUSDT", "REEFUSDT", "RLCUSDT", "RNDRUSDT",
    "SANDUSDT", "SNXUSDT", "SOLUSDT", "STGUSDT", "SUIUSDT",
    "SUSHIUSDT", "SXPUSDT", "TOMOUSDT", "TRXUSDT", "UNIUSDT",
    "WAVESUSDT", "XLMUSDT", "XRPUSDT", "XVGUSDT",
    "ZECUSDT", "ZILUSDT", "ZRXUSDT", # ... add more symbols here
]

start_date = "2021-01-01"
end_date = "2023-08-15"
user = "bybit_01"
#long = "enable"
#short = "disable"
leverage = "0.25"
balance = "1000.0"

for folder in folders:
    for symbol in symbols:
        command = [
            "python3",
            "backtest.py",
            "-u", user,
            "-s", symbol,
            "-lw", leverage,
            "-sb", balance,
            f"configs/live/{folder}/{symbol}.json",
            "--start_date", start_date,
            "--end_date", end_date
        ]

        subprocess.run(command)
