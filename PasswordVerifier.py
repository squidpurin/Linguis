import re
class PasswordVerifier(object):
    def passwordVerification(self,userp):
        if (len(userp) < 6 or len(userp) > 12):
            if not re.search("[a-z]", userp):
                if not re.search("[0-9]", userp):
                    if not re.search("[A-Z]", userp):
                        if not re.search("\s", userp):
                            return True
        return False
