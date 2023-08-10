# Web Service Detector

## Introduction
The Web Service Detector is a Python script designed to discover web services running on a range of IP addresses and ports. It utilizes multithreading to improve efficiency and employs the requests library for making HTTP requests and the BeautifulSoup library for parsing HTML content.


## Features
Scans a range of IP addresses and ports for web services.
Utilizes multithreading to speed up the scanning process.
Searches for a specified string within the HTML content of each service.
Outputs the URLs where the search string is found.


## Usage
1. Modify the `start_ip`, `end_ip`, `start_port`, and `end_port` variables in the script to specify the range of IP addresses and ports you want to scan.

2. Customize the `search_string` in the run method of the ServiceDetector class to define the string you want to search for in the HTML content of the services.

3. Open a terminal or command prompt and navigate to the directory containing the script.

4. Run the script using the following command:
```python
python web_service_detector.py
```


## Important Notes
1. Be cautious when scanning IP addresses and ports that you do not own or have explicit permission to scan.
2. Scanning certain IP addresses or ports without authorization may violate terms of use and legal regulations.


## License
This project is licensed under the MIT License.

## Disclaimer
The authors of this project are not responsible for any misuse, damage, or legal consequences caused by the usage of this script. Always ensure you have proper authorization before scanning any network.