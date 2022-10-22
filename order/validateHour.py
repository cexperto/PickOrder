import re


class ValidateHour:
    def validateHour(self, hour):
        if len(hour) < 4:
            return False
        hour_re = re.compile(r"^(?:[01]?\d|2[0-3]):[0-5]\d$")
        try:
            if int(hour[0:-3]) < 8 or int(hour[-2:]) > 18:
                return False
        except:
            pass
        if hour_re.search(str(hour)):
            return True
        return False
