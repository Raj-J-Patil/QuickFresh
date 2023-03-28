import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\shivr\\PycharmProjects\\QuickFresh\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def get_url():
        base_url = config.get('common info', 'baseURL')
        return base_url

    @staticmethod
    def get_id():
        id = config.get('common info', 'id')
        return id

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
