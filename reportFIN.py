import smtplib
from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, user_):
        self.user = user_
        self.server = smtplib.SMTP('smtp.gmail.com',587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login('linguissep@gmail.com','5859lsep')

    def communicate(self, msg):
        pass

class Reporter(Notification):
    def __init__(self, user_):
        super().__init__(user_)
        
    def report(self, msg):
        try:
            email = self.user.email
            name = 'First name- ' + self.user.firstname + '\n Last name- ' + self.user.lastname + '\n Username- ' + self.user.username
            message = "E-mail- "+email+'\n'+name+'\n Message- '+msg
            #print(msg)
            self.server.sendmail("linguissep@gmail.com","linguissep@gmail.com",message)
            #print("mg sent")
            self.server.quit()
        except:
            #print("Email not sent")
            pass

    def communicate(self, msg):
        self.notify(msg)
    
class Notifier(Notification):
    def __init__(self, user_):
        super().__init__(user_)

    def communicate(self, msg):
        self.notify(msg)
        
    def notify(self, msg):
        try:
            email = self.user.email
            name = 'First name- ' + self.user.firstname + '\n Last name- ' + self.user.lastname + '\n Username- ' + self.user.username
            message = "E-mail- "+email+'\n'+name+'\n Message- '+ msg
            self.server.sendmail("linguissep@gmail.com",email,message)
            #print("mg sent")
            self.server.quit()
        except:
            #print("Email not sent")
            pass
