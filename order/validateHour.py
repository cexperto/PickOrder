import re

class ValidateHour:
    def validateHour(self, hour):
        if len(hour)<4:
            return False
        hour_re = re.compile(r'^(?:[01]?\d|2[0-3]):[0-5]\d$')        
        try:
            if int(hour[0:2])>24 or int(hour[-2:])>59:
                return False
            else:
                return True
        except:
            pass
        if hour_re.search(str(hour)):
            return True
        return False

# hour = "1"
# validate_hour = ValidateHour()
# print(validate_hour.validateHour(hour))
