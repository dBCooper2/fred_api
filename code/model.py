# This is the Code for an API Scraper that pulls FRED Data and runs calculations

# imports
import requests
import json # handles data after scraping

# Test API Call:
url = "ADD API LINK HERE"
response = requests.get(url)

print(response.status_code)

'''
parts to study:
	- CPI
	- GDP
	- Inflation Rate
	- Unemployment Rate
'''