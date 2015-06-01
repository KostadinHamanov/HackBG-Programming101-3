import re


class Panda:

    def __init__(self, m_name, m_email, m_gender):
        self.m_name = m_name
        self.m_email = m_email
        self.m_gender = m_gender

    def get_name(self):
        return str(self.m_name)

    def get_email(self):
        return str(self.m_email)

    def get_gender(self):
        return str(self.m_gender)

    def isMale(self):
        return self.m_gender == "male"

    def isFemale(self):
        return self.m_gender == "female"

    def __eq__(self, other):
        equal_names = self.m_name == other.m_name
        equal_emails = self.m_email == other.m_email
        equal_genders = self.m_gender == other.m_gender
        return equal_names and equal_emails and equal_genders

    def __str__(self):
        return "{} - {} - {}".format(self.m_name, self.m_email, self.m_gender)

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.m_name,
                                                self.m_email, self.m_gender)

    def __hash__(self):
        return hash(self.__str__())

    def is_email_valid(self, m_email):
        if re.search('^[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z]{3,}$',
                     m_email) == None:
            return False
        return True
