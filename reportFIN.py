import smtplib

class Reporter:
    def __init__(self, user_):
        self.user = user_
        self.server = smtplib.SMTP('smtp.mail.yahoo.com',587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login('linguissep@yahoo.com','5859lsep')
    def report(self, msg):
        try:
            email = self.user.email
            name = self.user.firstname + ' ' + self.user.lastname
            msg = "\n"+email+'\n'+name+'\n'+msg
            print(msg)
            self.server.sendmail("linguissep@yahoo.com","linguissep@yahoo.com",msg)
            print("mg sent")
            self.server.quit()
        except:
            print("Email not sent")

class Notifier:
    def __init__(self, user_):
        self.user = user_
        self.server = smtplib.SMTP('smtp.mail.yahoo.com',587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login('linguissep@yahoo.com','5859lsep')
    def notify(self, msg):
        try:
            email = self.user.email
            name = self.user.firstname + ' ' + self.user.lastname
            msg = "\n"+email+'\n'+name+'\n'+msg
            print(msg)
            self.server.sendmail("linguissep@yahoo.com",email,msg)
            print("mg sent")
            self.server.quit()
        except:
            print("Email not sent")
