import yaml


class Account(object):

    def __init__(self):
        with open('./config/account.yml', 'r') as yml:
            self.__account = yaml.load(yml, Loader=yaml.SafeLoader)

    def get_login_info(self):
        return {
            "username": self.__get_id(),
            "password": self.__get_password(),
            "autologin-id": "0",
            "autologin-pass": "0"
        }

    def __get_id(self):
        return self.__account["id"]

    def __get_password(self):
        return self.__account["password"]
