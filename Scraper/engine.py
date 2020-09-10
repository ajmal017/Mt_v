import time
from subprocess import Popen, PIPE


def main():
    scrape_url = [
        "https://www.tradingview.com/symbols/EURUSD/",
        "https://www.tradingview.com/symbols/GBPUSD/?exchange=OANDA",
        "https://www.tradingview.com/symbols/AUDUSD/?exchange=FX",
        "https://www.tradingview.com/symbols/USDCAD/?exchange=OANDA",
        "https://www.tradingview.com/symbols/USDJPY/?exchange=OANDA",
        "https://www.tradingview.com/symbols/USDINR/?exchange=FX_IDC",
        "https://www.tradingview.com/symbols/USDTRY/?exchange=OANDA",
        "https://www.tradingview.com/symbols/USDCNY/?exchange=FX_IDC",
        "https://www.tradingview.com/symbols/USDAED/?exchange=FX_IDC",
        "https://www.tradingview.com/symbols/USDRUB/?exchange=FOREXCOM"
    ]
    api_url = {
        "https://www.tradingview.com/symbols/EURUSD/": "https://www.markettime.ir/update/EURtoUSD/",
        "https://www.tradingview.com/symbols/GBPUSD/?exchange=OANDA": "https://www.markettime.ir/update/GBPtoUSD/",
        "https://www.tradingview.com/symbols/AUDUSD/?exchange=FX": "https://www.markettime.ir/update/AUDtoUSD/",
        "https://www.tradingview.com/symbols/USDCAD/?exchange=OANDA": "https://www.markettime.ir/update/USDtoCAD/",
        "https://www.tradingview.com/symbols/USDJPY/?exchange=OANDA": "https://www.markettime.ir/update/USDtoJPY/",
        "https://www.tradingview.com/symbols/USDINR/?exchange=FX_IDC": "https://www.markettime.ir/update/USDtoINR/",
        "https://www.tradingview.com/symbols/USDTRY/?exchange=OANDA": "https://www.markettime.ir/update/USDtoTRY/",
        "https://www.tradingview.com/symbols/USDCNY/?exchange=FX_IDC": "https://www.markettime.ir/update/USDtoCNY/",
        "https://www.tradingview.com/symbols/USDRUB/?exchange=FOREXCOM": "https://www.markettime.ir/update/USDtoRUB/",
        "https://www.tradingview.com/symbols/USDAED/?exchange=FX_IDC": "https://www.markettime.ir/update/USDtoAED/"
    }
    prc = []
    info = {}

    for url in scrape_url:
        cmd = ["python", "scraper.py", url, api_url[url]]
        p = Popen(cmd, stdout=PIPE, shell=True)
        prc.append(p)
        info[p] = {"url": url, "api_url": api_url[url]}
        time.sleep(5)

    while True:
        for process in prc:
            for stdout_line in iter(process.stdout.readline, ""):
                print(stdout_line.decode("utf-8"))
            rc = process.poll()
            if rc is not None:
                if rc < 0:
                    cmd = ["python", "scraper.py",
                           info[process]["url"], info[process]["api_url"]]
                    p = Popen(cmd, stdout=PIPE, shell=True)
                    prc.append(p)
                    info[p] = {"url": info[process]["url"],
                               "api_url": info[process]["api_url"]}
                    del info[process]
                continue
            time.sleep(0.200)
        time.sleep(3)


if __name__ == "__main__":
    main()
