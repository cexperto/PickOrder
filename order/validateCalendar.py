from order.models import Order

# class ValidateCalendar:
def validate_ranges(date):
    return Order.objects.filter(date_order=date)

date = "20/10/2022"
print(validate_ranges(date))