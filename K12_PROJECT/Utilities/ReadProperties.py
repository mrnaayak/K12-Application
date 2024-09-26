import configparser
config=configparser.RawConfigParser()
config.read(".\\configuarations\\config.ini")
class ReadConfing:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getUsername():
        username=config.get('common info','useremail')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password