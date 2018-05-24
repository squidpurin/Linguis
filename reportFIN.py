import smtplib

class Reporter:
    def __init__(self, user):
        self.user = user
        self.server = smtplib.SMTP('smtp.mail.yahoo.com',587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login('linguissep@yahoo.com','5859lsep')
    def report(self, msg):
        email = self.user.email
        name = self.user.firstname + ' ' + self.user.lastname
        msg = "\n"+email+'\n'+name+'\n'+msg
        print(msg)
        self.server.sendmail("linguissep@yahoo.com","linguissep@yahoo.com",msg)
        print("mg sent")
        self.server.quit()
