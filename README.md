# Terracoin Sentinel

All masternodes must run Sentinel.

Will update instructions soon.

1. Download trcsentinel.exe
2. Create a sentinel.conf file in the same directory that you downloaded trcsentinel.exe with this inside:
terracoin_conf=C:\Users\USERNAME\AppData\Roaming\TerracoinCore\terracoin.conf

Change the username part to your username on your computer.

3. Go into %appdata% terracoincore

Open terracoin.conf and make sure it as at least:

rpcuser=someuser

rpcpassword=somepass

server=1

rpcport=13332

rpcconnect=127.0.0.1


Restart Terracoin-QT and wait for it to sync.

Run trcsentinel

Press 1.


# Building

Install pyinstaller `pip install pyinstaller`

Generate output EXE/ELF: `pyinstaller --onefile --paths=lib/ main.py`
