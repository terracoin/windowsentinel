from bin import sentinel
from lib import config
import time
import datetime

from colorama import init
from termcolor import colored

if __name__ == '__main__':
    init()

    print colored('Using desire.conf: {}'.format(config.desire_conf), 'green')

    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        print colored('{} Running sentinel'.format(now), 'green')
        try:
            sentinel.entrypoint()
        except Exception as e:
            print colored('Error: {}'.format(e), 'red')
        
        time.sleep(60) # Wait for a minute

