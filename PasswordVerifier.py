import re
class PasswordVerifier(object):
    def passwordVerification(self,userp):
        upper_case = 0
        lower_case = 0
        number = 0

        for i in userp:
            if i.isupper():
                upper_case += 1
            elif i.islower():
                lower_case += 1
            elif i.isdigit():
                number += 1

        if upper_case > 0 and lower_case > 0 and number > 0 :
            return True
        return False
