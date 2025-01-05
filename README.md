*Twitter Trends Scraper*:

This project is a web application that scrapes trending topics from Twitter and displays them in an interactive interface. The project integrates several technologies for scraping, processing, and presenting the data, with features like IP rotation and persistent storage for historical trends.

**Tech Stack**:
Backend: Python, Flask Web Scraping: Selenium (headless mode for seamless automation)
Frontend: HTML, CSS, JavaScript
Database: MongoDB
IP Rotation: ProxyMesh for dynamic IP allocation

**Features:**
IP Rotation Each scraping session uses a new IP address, thanks to ProxyMesh integration, which ensures anonymity and avoids IP blocking.

Dynamic Execution

A "Run Script" button triggers the scraper dynamically. The process can be restarted at any time to fetch updated results. Data Storage and Retrieval

Scraped trends are stored in MongoDB for persistence. Users can view all historical trends directly from the database. User-Friendly Interface A clean, interactive front end enables users to control the scraper and view results in real time.

**Screenshots**
Initial Interface When the server starts, users see the main interface:

![Screenshot 2025-01-05 171526](https://github.com/user-attachments/assets/aaa57c92-7b85-4b01-a436-e5301089ec10)

Real-Time Scraping After clicking "Run Script," the headless scraping process begins:
![Screenshot 2025-01-05 171535](https://github.com/user-attachments/assets/bd273e40-9e9a-4ea9-beab-14967ce96358)

Scraping Results and the results are displayed: 

![Screenshot 2025-01-05 171555](https://github.com/user-attachments/assets/993f76da-ab12-48e1-ac14-e4128caa0c93)

Detailed Trend List Clicking "All Results" retrieves and displays data from MongoDB: 
![Screenshot 2025-01-05 171605](https://github.com/user-attachments/assets/f68e4562-1fd6-425d-96f5-b55d066ea9a4)

How It Works Start the Server Launch the Flask server to initialize the application.

1)Run Script

2)Click the "Run Script" button.

3)Selenium, running logs into Twitter and fetches current trends. 

4)ProxyMesh rotates the IP for anonymity. 5)View Results

The scraped trends are displayed on the front end. All historical trends are accessible by clicking the "All Results" button, which retrieves data from MongoDB. 

Repeat Restart the process at any time to fetch updated trends with a new IP address.




