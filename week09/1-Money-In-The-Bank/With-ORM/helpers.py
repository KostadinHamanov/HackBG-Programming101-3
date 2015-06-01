import hashlib
from settings import SALT, PASSWORD_MIN_LENGTH
from settings_email import USER_EMAIL, USER_PASS
import re
import smtplib
from email.mime.text import MIMEText


def hash_password(password):
    sha256 = hashlib.sha256()

    sha256.update((password + SALT).encode("utf-8"))

    return sha256.hexdigest()


def password_validator(username, password):
    """
    More then 8 symbols
    Must have capital letters, and numbers and a special symbol
    Username is not in the password (as a substring)
    """
    digits = re.search(r'\d+', password)
    capital_letters = re.search(r'[A-Z]+', password)
    lenght = len(password) > PASSWORD_MIN_LENGTH
    special_symbol = re.search(r'[\-\/\@\?\!\,\.\#\&\*]+', password)

    statement = digits and capital_letters and lenght and special_symbol

    if statement:
        return True
    return False


def generate_tan_codes(number):
    # tan_codes = []

    # for i in range(number):
    #     pass

    # return
    pass


def send_email(email, message):
    message = MIMEText(message)
    message["Subject"] = "Reset Password"
    message["To"] = email
    message["From"] = USER_EMAIL

    server = smtplib.SMTP('smtp.gmail.com:587')

    server.starttls()
    server.login(USER_EMAIL, USER_PASS)
    server.send_message(message)
    server.quit()
