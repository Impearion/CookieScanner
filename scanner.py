import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import json

url = 'https://cookie-script.com/'  # Replace with the website URL you want to scan

# Fetch first-party cookies using requests
response = requests.get(url)

first_party_cookies = {}

if response.status_code == 200:
    cookies = response.cookies
    print("First-party cookies:")
    for cookie in cookies:
        first_party_cookies[cookie.name] = cookie.value
        print(f"Name: {cookie.name}, Value: {cookie.value}")
else:
    print(f"Failed to fetch the website. Status code: {response.status_code}")

# Use Selenium for inspecting third-party cookies
chrome_driver_path = 'C:\webdrivers\chromedriver.exe'  # Replace this with the path to your ChromeDriver
chrome_service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

driver.get(url)

third_party_cookies = driver.get_cookies()
print("\nThird-party cookies:")
for cookie in third_party_cookies:
    print(f"Name: {cookie['name']}, Value: {cookie['value']}, Domain: {cookie['domain']}")

driver.quit()

# Save cookies to a JSON file
cookies_data = {
    "first_party_cookies": first_party_cookies,
    "third_party_cookies": [cookie for cookie in third_party_cookies]
}

with open('cookies.json', 'w') as file:
    json.dump(cookies_data, file, indent=4)
