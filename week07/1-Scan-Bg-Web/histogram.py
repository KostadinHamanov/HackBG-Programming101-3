class Histogram:

    def __init__(self):
        self.information = {}

    def __getitem__(self, key):
        return self.information[key]

    def add(self, server):
        if server in self.information.keys():
            self.information[server] += 1
        else:
            self.information[server] = 1

    def count(self, server):
        if server not in self.information.keys():
            return None
        return self.information[server]

    def items(self):
        return self.information.items()

    def get_dict(self):
        return self.information

    def __str__(self):
        return str(self.information)

    def __repr__(self):
        return self.__str__()


# h = Histogram()
# h.add("Apache")
# h.add("Apache")
# h.add("nginx")
# h.add("IIS")
# h.add("nginx")
# h.count("Apache")

# print (h.get_dict())

# for key, count in h.items():
#     print("{}: {}".format(key, count))
