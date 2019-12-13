import smtplib
from email.mime.text import MIMEText
from sys import stderr, argv

class Mail(object):
    def __init__(self, host, port, login, password):
        self.__server = None
        try:
            self.__server = smtplib.SMTP_SSL(host, port)
        except:
            print("Error: Can't connect to {}:{}".format(host, port), file=stderr)
            exit(2)
        try:
            self.__server.login(login, password)
        except:
            print("Error: Can't login with {} and {}".format(login, password), file=stderr)
            self.__server = None
            exit(2)
        self.login = login

    def send(self, dest, subject, msg):
        data = MIMEText(msg)
        data["Subject"] = subject
        data["From"] = self.login
        data["To"] = dest
        try:
            self.__server.sendmail(self.login, dest, data.as_string())
        except:
            print("Error: can't send mail to {}".format(dest), file=stderr)
            exit(2)

    def __del__(self):
        if self.__server is not None:
            self.__server.quit()