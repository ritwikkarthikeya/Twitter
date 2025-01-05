from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import json
import pymongo
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# MongoDB Setup
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Change the URL if necessary
db = client["trends_db"]  # Database name
collection = db["trends"]  # Collection name

# Proxy configuration
proxy = "http://rithwik:rithwik@us-ca.proxyMesh.com:31280"

chrome_options = Options()
            
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920x1080')  # Set window size to avoid hidden elements

# Set proxy
proxy_config = Proxy()
proxy_config.http_proxy = proxy
proxy_config.ssl_proxy = proxy
proxy_config.add_to_capabilities(webdriver.DesiredCapabilities.CHROME)

# Initialize WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options,
    desired_capabilities=proxy_config.to_capabilities()
)

try:
    # Navigate to the target URL
    driver.get("https://x.com/?lang=en&mx=2")

    # Set an implicit wait to handle loading delays
    driver.implicitly_wait(10)

    # Login process
    try:
        signin_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')
        signin_button.click()

        username = "RithwikK63164"
        username_field = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        username_field.send_keys(username)

        login_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        login_button.click()

        password = "ritwik@143"
        password_field = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(password)

        login_submit_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_submit_button.click()

        print('Login Successful')
    except Exception as login_error:
        print(f"Login failed: {login_error}")
        driver.quit()
        exit()

    # Fetching trending items using explicit wait for each element
    trends = []
    for i in range(3, 8):  # Adjust the range based on the number of trends to fetch
        try:
            xpath = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/section/div/div/div[{i}]'
            # Use WebDriverWait to ensure the element is loaded
            trend_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            trends.append(trend_element.text)
        except Exception as fetch_error:
            print(f"Error fetching item {i}: {fetch_error}")

    # Get current timestamp dynamically
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Fetch IP address used for the request
    ip_address = requests.get('https://api.ipify.org').text  # Fetch the public IP address

    # Prepare the data to be stored in MongoDB
    trend_data = {
        "timestamp": timestamp,
        "ip_address": ip_address,
        "trends": {f"nameoftrend{i+1}": trend for i, trend in enumerate(trends)}
    }

    # Insert the data into MongoDB
    collection.insert_one(trend_data)

    # Output formatted data
    formatted_output = "\n".join([f"- {trend}" for trend in trends])
    print(f"Name of trend1\n{formatted_output}")
    print(f"The IP address used for this query was {ip_address}.")
    print("Here’s a JSON extract of this record from MongoDB:")
    print(json.dumps(trend_data, indent=4))  # Pretty print for better readability

    # Fetch and display all data from MongoDB
    print("\nFetching all data from MongoDB:")
    records = collection.find()
    for record in records:
        print(f"Timestamp: {record['timestamp']}")
        print(f"IP Address: {record['ip_address']}")
        print("Trends:")
        for trend_key, trend_value in record['trends'].items():
            print(f"- {trend_key}: {trend_value}")
        print("\n" + "="*40 + "\n")

except Exception as general_error:
    print(f"An error occurred: {general_error}")
finally:
    driver.quit()  # Ensure the WebDriver is closed properly
