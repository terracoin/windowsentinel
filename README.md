# Desire Sentinel

Please test it and consider it to be a [b]beta[/b], something might fail (I don't have desire in Windows).

Pick an executable (either win/lin) from https://github.com/ZonnCash/sentinel/releases
Just for reference, sentinel-win64 virustotal (3/67): https://www.virustotal.com/es/file/3a65c0df1fb89607531d8c02bb2a3070f1c39f555944d118c67d8ee616be5b18/analysis/1510697796/

Use at your own risk, it has been compiled exactly as the Github repo says

## Before running it

**1.** Make sure you are running v0.12.2.1

**2.** Resync the whole wallet, from the menu "Tools" > "Wallet Repair" > "Rebuild Index"

**3.** Make sure your "desire.conf" contains at least, the following data:
rpcuser=someuser
rpcpassword=somepass
server=1
rpcport=9918
rpcconnect=127.0.0.1

Try to make rcpuser and rpcpassword hard to guess, you won't need to remember/use them for anything else, so feel free to smash the keyboard

**4** Restart you wallet after setting them, so that it loads the changes.
Make sure the wallet is running and completely synced before continuing

## How to

To make it point to your desire.conf, you have three options:

**A)** Create a file **sentinel.conf** in the same folder as the EXE with the following content:
desire_conf=C:\path\to\desire.conf

Start sentinel-win64.exe

**B)** From a console, execute the EXE by passing arguments 
sentinel-win64.exe --config=C:\path\to\desire.conf

**C)** By creating a shortcut

1) Right click the sentinel-win64.exe, "Create Shortcut". 
2) Right click the shortcut, Properties
3) Edit Target and, at the end, add a SPACE and then "--config=C:\path\to\desire.conf" INCLUDING the quotes "

Double click the shortcut to start sentinel.

### Feedback
If it doesn't work, create an *Issue* with detailed explanations


## Usage

Pick the appropiate file from [https://github.com/ZonnCash/sentinel/releases](Releases)

Open file `sentinel.conf` and change `desire_conf` to point to your desire configuration file

Run `sentinel.exe` and keep it open, that's all.

You might pass arguments to `sentinel.exe`, for example `sentinel.exe --config="C:\path\to\desire.conf"`


# Building

Install pyinstaller `pip install pyinstaller`

Generate output EXE/ELF: `pyinstaller --onefile --paths=lib/ main.py`
