from bin import sentinel
from lib import config
from lib import desire_config
import time
import datetime
import sys
import os
import shutil
import string
import random

from colorama import init
from termcolor import colored


def random_string(n):
    rnd = random.SystemRandom()
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
    m = len(pool) - 1

    return ''.join(pool[rnd.randint(0, m)] for _ in range(n))

def run_sentinel():
    print(colored('Sentinel is run every 1 minute', 'green'))

    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        print(colored('{} Running sentinel'.format(now), 'green'))
        try:
            sentinel.entrypoint()
        except Exception as e:
            print(colored('Error: {}'.format(e), 'red'))
        
        time.sleep(60) # Wait for a minute

def fix_masternode(data_folder):
    wallet_file = os.path.join(data_folder, 'wallet.dat')

    if not os.path.isfile(wallet_file):
        print('It seems data folder (the one containing wallet.data) is not the same as the folder where desire.conf is')
        data_folder = input('Please, write the data folder path: ')
        return fix_masternode(data_folder)

    print(colored('Make a copy of "wallet.data" and "desire.conf" before continuing.\nThis program will try it best not to touch them, but just in case!', attrs=['bold']))
    confirm = input('Once done, press [ENTER], or write cancel + [ENTER] to exit\n')
    if confirm.lower() == "cancel":
        return

    print(colored('Removing conflicting files', 'green'))
    for filename in os.listdir(data_folder):
        if filename in ('wallet.dat', 'desire.conf'):
            continue
        
        realpath = os.path.join(data_folder, filename)
        if os.path.isfile(realpath):
            os.remove(realpath)
        elif os.path.isdir(realpath):
            shutil.rmtree(realpath)
        
        print('\t{}'.format(filename))

    print(colored('Done removing', 'green'))
    print('')

    print(colored('Checking desire.conf contents', 'green'))
    tokens = desire_config.DesireConfig.tokenize(config.desire_conf)

    # Check if needed tokens are there, set them if not
    tokens['rpcuser'] = tokens.get('rpcuser', random_string(18))
    tokens['rpcpassword'] = tokens.get('rpcpassword', random_string(18))
    tokens['rpcconnect'] = tokens.get('rpcconnect', '127.0.0.1')
    tokens['rpcport'] = tokens.get('rpcport', 9918)
    tokens['server'] = 1

    # It must have a masternode=1
    try:
        if int(tokens['masternode']) != 1:
            raise Exception
    except:
        r = None
        while r not in ('y', 'n'):
            r = input(colored('It seems your desire.conf is not setting the wallet as masternode! Continuing will set it masternode=1, [y/n]: ', 'red'))
            if r == 'n':
                rewrite = False
            elif r != 'y':
                print('Please write y or n')

        if r == 'y':
            tokens['masternode'] = 1
        else:
            sys.exit(1)

    # It must have a masternodeprivkey
    if 'masternodeprivkey' not in tokens:
        print(colored('Your desire.conf does not contain a \'masternodeprivkey\' entry, please set it up before opening wallet', 'red'))

    # Rewrite config
    with open(config.desire_conf, 'w') as fp:
        for k, v in tokens.items():
            fp.write('{}={}\n'.format(k, v))

    print(colored('Done checking\n', 'green'))
    print(colored('Please open your wallet (desired on linux) and wait for it completely load/open before continuing', attrs=['bold']))
    input('Press [ENTER] to continue')
    print('')

    print(colored('Sentinel will automatically start in 15s', 'green', attrs=['bold']))
    print(colored('Until the wallet is fully synced, sentinel will show errors related to sync status, that\'s fine!', 'green'))
    print(colored('If it says it can not connect, check your desire.conf settings', 'yellow'))

    r = 15
    while r > 0:
        sys.stdout.write('Starting in {}s \r'.format(r))
        sys.stdout.flush()
        r -= 1
        time.sleep(1)

    print('\n')
    run_sentinel()
    

def menu():
    print('Select an option:')
    print('\t1. Start sentinel')
    print('\t2. Fix wallet and masternode')
    
    try:
        option = input('Write 1 or 2: ')
        option = int(option)
        if option < 1 or option > 2:
            raise Exception()

        return option
    except KeyboardInterrupt as e:
        print('')
        sys.exit(1)
    except:
        print(colored('Option not valid', 'red'))
        return None

if __name__ == '__main__':
    init()

    print(colored('Using desire.conf: {}'.format(config.desire_conf), 'green'))

    try: input = raw_input
    except NameError: pass

    option = None
    while option is None: 
        option = menu()

    if option == 1: 
        run_sentinel()
    elif option == 2: 
        # Use default data folder
        data_folder = os.path.dirname(config.desire_conf)
        fix_masternode(data_folder)
