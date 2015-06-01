from bank_controller import BankController
from bank_view import BankView
from settings import DATABASE
from settings import BLOCK_AFTER_N_FAILED_ATTEMPTS, BLOCK_FOR_N_MINUTES


def main():
    controller = BankController(
        DATABASE,
        block_after_n_logins=BLOCK_AFTER_N_FAILED_ATTEMPTS,
        block_for_n_minutes=BLOCK_FOR_N_MINUTES
    )

    view = BankView(controller)

    view.start_taking_commands()

if __name__ == '__main__':
    main()
