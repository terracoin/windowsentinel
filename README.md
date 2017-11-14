# Desire Sentinel

## Usage

Pick the appropiate file from [https://github.com/ZonnCash/sentinel/releases](Releases)

Open file `sentinel.conf` and change `desire_conf` to point to your desire configuration file

Run `sentinel.exe` and keep it open, that's all.

You might pass arguments to `sentinel.exe`, for example `sentinel.exe --config="C:\path\to\desire.conf"`


# Building

Install pyinstaller `pip install pyinstaller`

Generate output EXE/ELF: `pyinstaller --onefile --paths=lib/ main.py`
