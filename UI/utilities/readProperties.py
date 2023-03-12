import configparser

config = configparser.RawConfigParser()
config.read("/Users/ganeshachari/AutomationWork/UI/configuration/config.ini")


class ReadConfig:

    @staticmethod
    def getBaseUrl():
        return config.get('common info', 'baseUrl')

    @staticmethod
    def getUsername():
        return config.get('common info', 'username')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')

    @staticmethod
    def getEmail():
        return config.get('common info', 'search_email')