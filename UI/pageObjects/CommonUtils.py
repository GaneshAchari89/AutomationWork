from UI.utilities.customLogger import LogGenerator
from UI.utilities.readProperties import ReadConfig


class CommonUtils:
    baseUrl = ReadConfig.getBaseUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGenerator.generateLogger()
    search_email = ReadConfig.getEmail()