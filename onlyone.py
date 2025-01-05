from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chromeoptions=Options()
chromeoptions.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chromeoptions)
driver.get("https://www.flipkart.com/search?q=mouse&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

name=driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[3]/div/div[1]/div/a[2]') 
print(name.text) 

price=driver.find_element(By.CLASS_NAME,"Nx9bqj")
print(price.text)

print("----------------------------------------------------------------------------------")

for i in range(1, 5):
    try:
        xpath = f'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[{i}]/div/a[2]'
        names = driver.find_element(By.XPATH, xpath)
        print(f"Item {i}: {names.text}")
        print('--------------------')
    except Exception as e:
        print(f"Error fetching item {i}: {e}")


