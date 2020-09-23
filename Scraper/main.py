import os
import time
from subprocess import Popen, PIPE
from colorama import Fore, Style, init
init()
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class Scraper:
    __slots__ = ('name', 'status', 'process')

    def __init__(self, name):
        self.name = name


def main():
    clear()
    files = ['investing.py', 'investing_saham.py',
             'forex_factory.py', 'mex.py', 'tgju.py']

    print(f"{Fore.GREEN}Starting...{Style.RESET_ALL}")
    classes = []
    label = ""
    sep = ""
    st_bar = ""
    for file in files:
        prc = Scraper(file)
        classes.append(prc)
        cmd = ['python', file]
        prc.process = Popen(cmd, stdout=PIPE, shell=True)
        label += f'{file}\t'
        sep += ('-' * len(file)) + "\t"
        prc.status = prc.process.poll()
        clear()
        print(label)
        print(sep)
        time.sleep(15)

    clear()
    print(label)
    print(sep)
    while 1:
        try:
            st_bar = ""
            for prc in classes:
                prc.status = prc.process.poll()
                t = ''
                if not prc.status:
                    t = 'WORKING'
                    prc.status = f'{Fore.GREEN}WORKING{Style.RESET_ALL}'
                else:
                    t = 'STOPPED'
                    prc.status = f'{Fore.RED}STOPPED{Style.RESET_ALL}'
                spaces = len(prc.name) - len(t)
                st_bar += prc.status + (" " * spaces) + '\t'
            print(st_bar, end="\r")
            time.sleep(1)
        except KeyboardInterrupt:
            for prc in classes:
                prc.process.terminate()
            os.system("taskkill /f /im  chrome.exe")
            raise


if __name__ == '__main__':
    main()
