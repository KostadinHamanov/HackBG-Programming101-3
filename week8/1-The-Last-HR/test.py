import requests


def main():
    url = 'https://hackbulgaria.com/api/students/'
    site_response = requests.get(url)
    print (site_response)
    information = site_response.json()
    # print (information)

if __name__ == '__main__':
    main()
