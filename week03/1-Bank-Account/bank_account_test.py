from bank_account import BankAccount


import unittest


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.rado = BankAccount("Rado", 0, "$")
        self.ivo = BankAccount("Ivo", 200, "$")

    def test_init(self):
        self.assertTrue(isinstance(self.rado, BankAccount))
        self.assertTrue(isinstance(self.ivo, BankAccount))
        self.assertEqual(self.rado.name, "Rado")
        self.assertEqual(self.rado.balance, 0)
        self.assertEqual(self.rado.currency, "$")
        self.assertEqual(self.ivo.name, "Ivo")
        self.assertEqual(self.ivo.balance, 200)
        self.assertEqual(self.ivo.currency, "$")

    def test_str(self):
        needed_result = "Bank account for {} with balance of {}{}".format(
            self.rado.name, self.rado.balance, self.rado.currency)
        self.assertEqual(str(self.rado), needed_result)

        needed_result = "Bank account for {} with balance of {}{}".format(
            self.ivo.name, self.ivo.balance, self.ivo.currency)
        self.assertEqual(str(self.ivo), needed_result)

    def test_int(self):
        self.assertEqual(int(self.ivo), self.ivo.get_balance())
        self.assertEqual(int(self.rado), self.rado.get_balance())

    def test_deposite(self):
        self.rado.deposit(100)
        self.assertEqual(self.rado.balance, 100)
        with self.assertRaises(ValueError):
            self.rado.deposit(-50)

        self.ivo.deposit(0)
        self.assertEqual(self.ivo.balance, 200)
        with self.assertRaises(ValueError):
            self.ivo.deposit(-100)

    def test_transfer_to_different_currency(self):
        gosho = BankAccount("Gosho", 200, "&")

        with self.assertRaises(ValueError):
            gosho.transfer_to(self.ivo, 10)

        with self.assertRaises(ValueError):
            self.ivo.transfer_to(gosho, 110)

        self.assertEqual(self.rado.balance, 0)
        self.assertEqual(self.ivo.balance, 200)

    def test_getting_balance(self):
        self.assertEqual(self.rado.get_balance(), 0)
        self.assertEqual(self.ivo.get_balance(), 200)

    def test_transfer_to_more_money_that_we_have(self):
        self.assertFalse(self.ivo.transfer_to(self.rado, 1500))
        self.assertFalse(self.rado.transfer_to(self.ivo, 100))

        self.assertEqual(self.rado.balance, 0)
        self.assertEqual(self.ivo.balance, 200)

    def test_withdraw(self):
        # Test withdrawing amount of money we have
        self.assertTrue(self.ivo.withdraw(10))

        # Test withdrawing negative amount of money
        with self.assertRaises(ValueError):
            self.ivo.withdraw(-50)
        self.assertTrue(self.ivo.get_balance() == 190)

        # Test withdrawing more money than we have
        self.assertFalse(self.rado.withdraw(50))

        # Test withdrawing negative amount
        with self.assertRaises(ValueError):
            self.ivo.withdraw(-10)
        self.assertTrue(self.rado.get_balance() == 0)

    def test_transfer_to(self):
        pesho = BankAccount("Pesho", 20000, "$")
        result = pesho.transfer_to(self.rado, 1000)
        self.assertEqual(self.rado.balance, 1000)
        self.assertEqual(pesho.balance, 19000)
        self.assertTrue(result)

    def test_transfering_more_money_than_we_have(self):
        pesho = BankAccount("Pesho", 20000, "$")
        self.assertFalse(self.rado.transfer_to(pesho, 2000))
        self.assertEqual(self.rado.balance, 0)
        self.assertFalse(self.rado.transfer_to(pesho, 1000))
        self.assertEqual(self.rado.balance, 0)

    def test_transfering_to_different_currency(self):
        with self.assertRaises(ValueError):
            pesho = BankAccount("Pesho", 20000, "BGN")
            result = pesho.transfer_to(self.rado, 1000)
            self.assertEqual(self.rado.balance, 0)
            self.assertEqual(pesho.balance, 20000)
            self.assertFalse(result)

    def test_history_create_account(self):
        # Creating an account
        expected = "Account was created"
        self.assertEqual(self.ivo.history()[0], expected)

    def test_history_deposit(self):
        self.rado.deposit(1000)
        rado_expected = "Deposited 1000{}" .format(self.rado.currency)
        self.assertEqual(self.rado.history()[-1], rado_expected)

        self.ivo.deposit(500)
        ivo_expected = "Deposited 500{}" .format(self.ivo.currency)
        self.assertEqual(self.ivo.history()[-1], ivo_expected)

    def test_history_balance(self):
        self.ivo.get_balance()
        ivo_expected = "Balance check -> {}{}" .format(
            self.ivo.balance, self.ivo.currency)
        self.assertEqual(self.ivo.history()[-1], ivo_expected)

    def test_history_int_check(self):
        int(self.rado)
        rado_expected = "__int__ check -> {}{}" \
            .format(self.rado.balance, self.rado.currency)
        self.assertEqual(self.rado.history()[-1], rado_expected)

    def test_history_valid_withdraw(self):
        self.ivo.withdraw(10)
        ivo_expected = "10{} was withdrawed" .format(self.ivo.currency)
        self.assertEqual(self.ivo.history()[-1], ivo_expected)

    def test_history_invalid_withdraw(self):
        self.rado.withdraw(200000)
        rado_expected = "Withdraw for {}{} failed." \
            .format(200000, self.rado.currency)
        self.assertEqual(self.rado.history()[-1], rado_expected)

        with self.assertRaises(ValueError):
            self.ivo.withdraw(-50)

    def test_history_transfer_to(self):
        pesho = BankAccount("Pesho", 1000, "EUR")
        gosho = BankAccount("Gosho", 2000, "EUR")

        pesho.transfer_to(gosho, 100)
        pesho_expected = "Transfer to {} for {}{}" \
            .format(gosho.name, 100, pesho.currency)
        self.assertEqual(pesho.history()[-1], pesho_expected)

        gosho_expected = "Transfer from {} for {}{}" \
            .format(pesho.name, 100, gosho.currency)
        self.assertEqual(gosho.history()[-1], gosho_expected)

        with self.assertRaises(ValueError):
            pesho.transfer_to(self.ivo, 10)

        self.assertFalse(pesho.transfer_to(gosho, 30000))

if __name__ == '__main__':
    unittest.main()
