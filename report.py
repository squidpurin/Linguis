import smtplib

class Reporter:
    def __init__(self, user):
        self.user = user
        self.server = smtplib.SMTP('smtp.mail.yahoo.com',587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login('linguissep@yahoo.com','mihhemqaqpqiiiujut')
    def reportProblem(self, msg):
        #get user email, id, name from user
        ###################################
        email = "lhagvsmrner@hmtm.idz"
        name = "opilaneisa"
        msg = "\n"+email+name+msg
        print(msg)
        self.server.sendmail("linguissep@yahoo.com","c.dswibowo@yahoo.com.tw",msg)
        print("mg sent")
        self.server.quit()
        
r = Reporter("ahmadabad")
r.reportProblem("aiuma")
