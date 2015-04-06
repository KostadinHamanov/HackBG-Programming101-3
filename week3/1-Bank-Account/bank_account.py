class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.history_info = ["Account was created"]

    def __int__(self):
        current_history = "__int__ check -> {}{}". \
            format(self.balance, self.currency)
        self.history_info.append(current_history)

        return self.balance

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"
        return message.format(self.name, self.balance, self.currency)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self.balance += amount

            current_history = "Deposited {}{}". format(amount, self.currency)
            self.history_info.append(current_history)

    def get_balance(self):
        current_history = "Balance check -> {}{}". \
            format(self.balance, self.currency)
        self.history_info.append(current_history)

        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError

        if amount <= self.balance:
            self.balance -= amount

            current_history = "{}{} was withdrawed". \
                format(amount, self.currency)
            self.history_info.append(current_history)

            return True

        else:
            current_history = "Withdraw for {}{} failed.". \
                format(amount, self.currency)
            self.history_info.append(current_history)

            return False

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError

        if self.balance < amount:
            return False

        self.balance -= amount
        account.balance += amount

        # self.withdraw(amount)
        # account.deposit(amount)

        transfered_to = "Transfer to {} for {}{}". \
            format(account.name, amount, self.currency)
        self.history_info.append(transfered_to)

        transfered_from = "Transfer from {} for {}{}" .\
            format(self.name, amount, self.currency)
        account.history_info.append(transfered_from)

        return True

    def history(self):
        return self.history_info


def main():
    rado = BankAccount("Rado", 1000, "BGN")
    ivo = BankAccount("Ivo", 0, "BGN")
    rado.transfer_to(ivo, 500)
    rado.get_balance()
    ivo.get_balance()
    print (rado.history())
    print (ivo.history())

if __name__ == '__main__':
    main()
