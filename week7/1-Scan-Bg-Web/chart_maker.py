import matplotlib.pyplot as plt


class ChartMaker:

    @staticmethod
    def make_chart(websites_histogram):
        keys = list(websites_histogram.get_dict().keys())
        values = list(websites_histogram.get_dict().values())

        X = list(range(len(keys)))
        plt.bar(X, values, align="center")
        plt.xticks(X, keys)
        plt.title(".bg servers")
        plt.xlabel("Server")
        plt.ylabel("Count")
        plt.savefig("histogram.png")
