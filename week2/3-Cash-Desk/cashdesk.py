class Bill:

    def __init__(self, amount):
        if amount <= 0:
            raise ValueError

        if not isinstance(amount, int):
            raise TypeError

        self.amount = amount

    def __str__(self):
        return 'A {}$ bill'.format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.__str__())


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __int__(self):
        return self.total()

    def total(self):
        total = 0
        for bill in self.bills:
            total += int(bill)
        return total

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:

    def __init__(self):
        self.vault = []

    def take_money(self, currency):
        self.vault.append(currency)

    def total(self):
        total_sum = 0
        for money in self.vault:
            total_sum += int(money)

        return total_sum

    def inspect(self):
        money_holder = {}
        for batch in self.vault:
            if isinstance(batch, BatchBill):
                for bill in batch:
                    if bill in money_holder.keys():
                        money_holder[bill] += 1
                    else:
                        money_holder[bill] = 1
            else:
                if batch in money_holder.keys():
                    money_holder[batch] += 1
                else:
                    money_holder[batch] = 1

        print ("We have a total of {}$ in the desk".format(self.total()))
        print (
            "We have the following count of bills")
        print (money_holder)


def main():
    peter = Bill(5000)
    john = Bill(1000)

    print (peter)
    print (peter.amount)
    print (peter == john)
    print (hash(str(peter)))

    values = [10, 20, 50, 100]
    bills = [Bill(value) for value in values]
    batch = BatchBill(bills)
    for bill in batch:
        print (bill)

    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]
    batch = BatchBill(bills)
    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print (desk.total())  # 390
    desk.inspect()

if __name__ == '__main__':
    main()
