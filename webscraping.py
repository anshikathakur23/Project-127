from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import requests
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import expected_condition as EC

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"
browser = webdriver.Chrome()
headers = ["Name", "Distance", "Mass", "Radius"]
data = []

response = requests.get (START_URL, headers = headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find ("table", {"class": "wikitable"})
    headers = [header.text.strip () for header in table.find_all ("th")]
    rows = table.find_all ("tr")

    for row in rows:
        cols = row.find_all ("td")
        cols = [col.text.strip () for col in cols]
        if cols:
            data.append (cols)
            break

with open ("stars.csv", "w", newline = "") as file:
    writer = csv.writer (file)
    writer.writerow (headers)
    writer.writerow (data)