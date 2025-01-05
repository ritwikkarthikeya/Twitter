Twitter Trends Scraper
This project is a web application that scrapes trending topics from Twitter and displays them in an interactive interface. The project integrates several technologies for scraping, processing, and presenting the data, with features like IP rotation and persistent storage for historical trends.

Tech Stack
Backend: Python, Flask
Web Scraping: Selenium (headless mode for seamless automation)
Frontend: HTML, CSS, JavaScript
Database: MongoDB
IP Rotation: ProxyMesh for dynamic IP allocation
Features
Headless Web Scraping
The web scraper uses Selenium in headless mode, ensuring the process runs entirely in the background without displaying a browser window.

Automated Login
The scraper securely logs in using predefined credentials to access Twitter and retrieve trends.

IP Rotation
Each scraping session uses a new IP address, thanks to ProxyMesh integration, which ensures anonymity and avoids IP blocking.

Dynamic Execution

A "Run Script" button triggers the scraper dynamically.
The process can be restarted at any time to fetch updated results.
Data Storage and Retrieval

Scraped trends are stored in MongoDB for persistence.
Users can view all historical trends directly from the database.
User-Friendly Interface
A clean, interactive front end enables users to control the scraper and view results in real time.

Screenshots
1. Initial Interface
When the server starts, users see the main interface:
![image](https://github.com/user-attachments/assets/a76eebe6-3987-4962-b19c-eb28ac7ad1e0)

2. Real-Time Scraping 
After clicking "Run Script," the headless scraping process begins:
![image](https://github.com/user-attachments/assets/9b8de513-19a7-4259-9235-1ea22b770275)

3. Scraping Results
and the results are displayed:
![image](https://github.com/user-attachments/assets/9a329406-eace-477d-826a-dcaed14ee367)


5. Detailed Trend List
Clicking "All Results" retrieves and displays data from MongoDB:
![image](https://github.com/user-attachments/assets/9a329406-eace-477d-826a-dcaed14ee367)


How It Works
Start the Server
Launch the Flask server to initialize the application.

1)Run Script

2)Click the "Run Script" button.
3)Selenium, running  logs into Twitter and fetches current trends.
4)ProxyMesh rotates the IP for anonymity.
5)View Results

The scraped trends are displayed on the front end.
All historical trends are accessible by clicking the "All Results" button, which retrieves data from MongoDB.
Repeat
Restart the process at any time to fetch updated trends with a new IP address.
