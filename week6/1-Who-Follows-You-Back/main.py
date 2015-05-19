from github_person import Person
from network import Network


def main():
    kostadin_api = "https://api.github.com/users/KostadinHamanov"
    kostadin = Person(kostadin_api)

    my_net = Network()
    my_net.build_network_for(kostadin, 1)

if __name__ == '__main__':
    main()
