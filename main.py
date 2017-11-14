from bin import sentinel
from bin import config
import time

if __name__ == '__main__':
    print('Using desire.conf: {}'.format(config.desire_config))

    while True:
        sentinel.main()
        time.sleep(60) # Wait for a minute

