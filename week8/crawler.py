import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, url):
        self.url = url
        self.internal_links = []
        self.external_links = []
        self.visited = []

    def start(self):
        links = self.get_links_from_url(self.url)
        self.classify(links)
        self.visited.append(self.url)

        for link in self.internal_links:
            print (link)
            if link not in self.visited:
                self.visited.append(link)
                sub_pages = self.get_links_from_url(link)
                self.classify(sub_pages)

    def get_links_from_url(self, url):
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text)

            links = set()

            for link in soup.find_all('a'):
                links.add(link.get('href'))

        except:
            print ("INVALID URL")

        return links

    def classify(self, links):
        for link in links:

            if link is None:
                continue

            if "start.bg" in link:
                self.internal_links.append(link)
            elif "link.php?" in link:
                self.external_links.append(link)


def main():
    crawler = Crawler("http://www.start.bg/")
    crawler.start()


if __name__ == "__main__":
    main()
