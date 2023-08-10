import ipaddress
import requests
import threading
from bs4 import BeautifulSoup

class ServiceDetector(threading.Thread):
    def __init__(self, start_ip, end_ip, start_port, end_port):
        threading.Thread.__init__(self)
        self.start_ip = start_ip
        self.end_ip = end_ip
        self.start_port = start_port
        self.end_port = end_port
        self.find_list = []

    def run(self):
        start_ip = self.start_ip
        end_ip = self.end_ip

        start_ip_int = int(ipaddress.IPv4Address(start_ip))
        end_ip_int = int(ipaddress.IPv4Address(end_ip))

        for ip_int in range(start_ip_int, end_ip_int + 1):
            target = str(ipaddress.IPv4Address(ip_int))
            for port in range(self.start_port, self.end_port + 1):
                url1 = f"https://{target}:{port}"
                self.search_string_in_page(url1, "test")
                url2 = f"https://{target}:{port}"
                self.search_string_in_page(url2, "test")

    def search_string_in_page(self, url, search_string):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            if search_string.lower() in soup.get_text().lower():
                print(f"The string '{search_string}' was found in the page: {url}")
                self.find_list.append([url, search_string])
            else:
                print(f"The string '{search_string}' was not found in the page: {url}")
        except Exception as e:
            pass

start_ip = "start_ip"
end_ip = "end_ip"
start_port = 1
end_port = 65535

scanner_threads = []

for _ in range(5):
    scanner_thread = ServiceDetector(start_ip, end_ip, start_port, end_port)
    scanner_threads.append(scanner_thread)
    scanner_thread.start()

for scanner_thread in scanner_threads:
    scanner_thread.join()

for thread in scanner_threads:
    for i in range(len(thread.find_list)):
        print(f"{thread.find_list[i][0]} find {thread.find_list[i][1]}")