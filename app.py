from flask import Flask, request, jsonify, send_from_directory
from seleniumwire import webdriver as seleniumwire_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
import requests
import traceback
from urllib.parse import quote
import os
import json

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI if not local
db = client['trendsDB']
collection = db['trends']

# Proxy setup
proxy_username = "rithwik"
proxy_password = "rithwik"
proxy_host = "us-ca.proxyMesh.com"
proxy_port = "31280"

encoded_username = quote(proxy_username)
encoded_password = quote(proxy_password)
PROXY = f"http://{encoded_username}:{encoded_password}@{proxy_host}:{proxy_port}"

proxies = {
    "http": PROXY,
    "https": PROXY
}

try:
    response = requests.get("http://ipinfo.io/json", proxies=proxies)
    print("Proxy IP Info:", response.json())
except Exception as e:
    print(f"Error: {e}")


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')  # Serve the HTML file


@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        chromeoptions = Options()

        chromeoptions.add_argument('--disable-gpu')
        chromeoptions.add_argument('--no-sandbox')

        seleniumwire_options = {
            'proxy': {
                'http': PROXY,
                'https': PROXY,
            }
        }

        # Create the WebDriver with selenium-wire
        driver = seleniumwire_webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chromeoptions
        )
        driver.seleniumwire_options = seleniumwire_options
        driver.implicitly_wait(40)

        driver.get("https://x.com/?lang=en&mx=2")
        sigin = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')
        sigin.click()

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

        trends = []
        for i in range(3, 8):
            try:
                xpath = f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/section/div/div/div[{i}]'
                trendingName = driver.find_element(By.XPATH, xpath)
                trends.append(trendingName.text)
            except Exception as e:
                print(f"Error fetching item {i}: {e}")

        # Fetch the public IP address used via the proxy
        proxy_response = requests.get("http://ipinfo.io/json", proxies={'http': PROXY, 'https': PROXY})
        proxy_ip = proxy_response.json().get("ip", "Unknown IP")

        # Only save data if a valid IP address is returned
        if proxy_ip != "Unknown IP":
            # Save to MongoDB
            trends_data = {"ip": proxy_ip, "trends": trends}
            insert_result = collection.insert_one(trends_data)

            # Convert ObjectId to string before JSON serialization
            trends_data["_id"] = str(insert_result.inserted_id)

            # Format the response
            formatted_trends = "\n".join([f"{i+1}. {trend}" for i, trend in enumerate(trends)])
            formatted_result = f"""
            {formatted_trends}
            
            The IP address used for this query was {proxy_ip}.
            
            Here’s a JSON extract of this record from the MongoDB:
            {json.dumps(trends_data, indent=4)}

            """
            driver.quit()
            return formatted_result
        else:
            driver.quit()
            return "Failed to retrieve a valid IP address, data not saved."
        
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/fetch-trends', methods=['GET'])
def fetch_trends():
    try:
        all_trends = list(collection.find())
        if not all_trends:
            return "No trends data found in the database!", 200, {'Content-Type': 'text/plain; charset=utf-8'}

        formatted_output = ""
        for idx, entry in enumerate(all_trends, start=1):
            ip = entry.get("ip", "Unknown IP")
            trends = entry.get("trends", [])
            formatted_output += f"Entry {idx}:\n"
            formatted_output += f"IP Address: {ip}\n"
            for t_idx, trend in enumerate(trends, start=1):
                formatted_output += f"  Trend {t_idx}: {trend}\n"
            formatted_output += "\n" + "=" * 40 + "\n"


        return formatted_output, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    except Exception as e:
        traceback.print_exc()
        return f"Error: {e}", 500, {'Content-Type': 'text/plain; charset=utf-8'}


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=True)
