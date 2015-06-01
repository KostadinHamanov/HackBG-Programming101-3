from histogram import Histogram
from crawler import Crawler
from chart_maker import ChartMaker


def main():
    websites_histogram = Histogram()

    webpage = "http://register.start.bg/"

    Crawler.parse_html(webpage)

    links = Crawler.get_links(webpage)
    Crawler.save_data_in_file("links.json", links)

    full_servers = Crawler.get_servers(webpage, links)
    Crawler.save_data_in_file("full_servers.json", full_servers)

    full_servers_data = Crawler.read_data_from_file("full_servers.json")
    servers = Crawler.sort_most_frequent_servers(websites_histogram,
                                                 full_servers_data)

    Crawler.save_data_in_file("servers_histogram.json", servers)

    ChartMaker.make_chart(websites_histogram)

if __name__ == '__main__':
    main()
