from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link_list = []
prices_list = []
address_list = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)


response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
for i in price:
    price_T = i.getText()
    price = price_T.split("+")[0]
    prices_list.append(price)
    
clean_price_list = []

for i in prices_list:
    price = i.split("/")[0]
    clean_price_list.append(price)
    
# print(clean_price_list)

link = soup.find_all(name="a")
for i in link:
    href = i.get("href")
    link_list.append(href)

# print(link_list)

address = soup.find_all(name="address")
for i in address:
    addr = i.getText()
    clean_addr = addr.strip()
    address_list.append(clean_addr)

# print(address_list)

for n in range(len(link_list)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc3TS29uPXR-OyyDvUembs_fQte3s5IOdU5V8_-fRUYf6iWTw/viewform?usp=sf_link")
    time.sleep(2)
    
    addresses = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prices = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    links = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    
    addresses.send_keys(address_list[n])
    prices.send_keys(clean_price_list[n])
    links.send_keys(link_list[n])
    submit_button.click()