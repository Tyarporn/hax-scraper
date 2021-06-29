import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import csv
iso_url = "https://sosv.com"
link = "/portfolio/notifai"

driver_path = "/Users/tyarpornsuksant/Downloads/chromedriver"
driver = webdriver.Chrome(driver_path)

names = []
founders = []
linkedins = []
websites = []
descriptions = []
locations = []
hrefs = []
company_hrefs = []

iso_com_url = iso_url + link
driver.get(iso_com_url)
iso_src = driver.page_source
iso_soup = BeautifulSoup(iso_src, 'html.parser')
try:
    websites_links_raw = iso_soup.find_all('a',class_="sosv-link-dark mb-3")
    weblinks = []
    for w in websites_links_raw:
        if w['href'][0] == "h":
            websites.append(w['href'])
except:
    print("website for " + link + " not found")
company_ppl = iso_soup.find('div', class_="company-people col")
try:
    founder = company_ppl.find('p', class_="sosv-text mb-1")
    striped = founder.text.strip()
    n = striped.find("\n")
    striped_striped = striped[0:n]
    founders.append(striped_striped)
except:
    print("founder for " + link + " not found")
try:
    linkedin = company_ppl.find('a', {'title' : 'LinkedIn'})['href']
    linkedins.append(linkedin)
except:
    print("linkedin for " + link + " not found")

print(websites)
print(founders)
print(linkedins)