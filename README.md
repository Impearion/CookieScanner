# Cookie Scanner
This Python script scans a website for first and third-party cookies. These cookies will be saved in a .json file.

## Installation
To run this code you require Python, Pip and the libraries "requests", "selenium" and the chromedriver.

1. Install Python
2. Install pip
3. Install requests | python -m pip install requests
4. Install selenium | python -m pip install selenium
5. Download and move [chromedriver.exe](https://sites.google.com/chromium.org/driver/downloads) to C:\webdrivers. (create folder if it does not exist)
6. Create a new system environment variables for C:\webdrivers

## Usage
1. Put the link you want to scan into the url variable in the code
2. Open CMD in the folder of the script and run it with python scanner.py
3. The cookies will be stored in a .json file in the same folder in which the script is located
