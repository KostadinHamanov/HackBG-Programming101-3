import requests
import json
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class Crawler:

    @staticmethod
    def parse_html(webpage):
        response = requests.get(webpage)
        parsed_html = BeautifulSoup(response.text)

        return parsed_html

    @staticmethod
    def get_links(webpage):
        links = []
        parsed = Crawler.parse_html(webpage)
        needed_link = "link.php?id="

        for link in parsed.find_all('a'):
            if needed_link in str(link.get('href')):
                links.append(webpage + str(link.get('href')))

        return links

    @staticmethod
    def domain_from_url(url):
        parsed = urlparse(url)
        return parsed[0] + "://" + parsed[1]

    @staticmethod
    def has_tld(url, tld):
        return Crawler.domain_from_url(url).endswith(tld)

    @staticmethod
    def get_servers(webpage, links):

        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}

        servers = []
        visited = set()

        for link in links:
            if link is not None and "link.php" in link:
                try:
                    response = requests.head(
                        link, timeout=3, allow_redirects=True, headers=HEADERS)

                    target_url = Crawler.domain_from_url(response.url)

                    if target_url not in visited:
                        visited.add(target_url)

                        if Crawler.has_tld(target_url, ".bg"):
                            # print(target_url)
                            print(response.headers["Server"])
                            servers.append(response.headers["Server"])
                except:
                    pass

        return servers

    @staticmethod
    def sort_most_frequent_servers(histogram, servers):
        most_frequent_servers = [
            "Apache", "nginx", "Microsoft-IIS", "lighttpd"]

        for server in servers:
            for name in most_frequent_servers:
                if name in server:
                    histogram.add(name)

        return histogram.get_dict()

    @staticmethod
    def save_data_in_file(file_name, data):
        json_data = json.dumps(data, indent=4)
        with open(file_name, 'w') as opened_file:
            opened_file.write(json_data)

    @staticmethod
    def read_data_from_file(file_name):
        with open(file_name, 'r') as opened_file:
            data = json.loads(opened_file.read())

        return data
