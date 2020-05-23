# Redukowanie złożoności
# Abstraction

class MailServer():
    def send_mail(self):
        self.__connect()
        self.__autenticate()
        # Send mail
        self.__disconnect()

    def __connect(self):
        print("Connect")

    def __autenticate(self):
        print("Autenticate")

    def __disconnect(self):
        print("Disconnect")

m = MailServer()
m.send_mail()