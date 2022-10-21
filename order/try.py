# def sum_hour_to_hour(_time):
#     hour = int(_time[0:-3])+1
#     minuts = int(_time[-2:])
#     return str(hour)+':'+str(minuts)

# _time = "00:45"
# print(sum_hour_to_hour(_time))


data = [{'id': 4, 'latitud_collected': ('15.0000000000000000'), 'longitud_collected': ('15.0000000000000000'), 'latitud_destiny': ('18.0000000000000000'), 'longitud_destiny': ('18.0000000000000000'), 'date_order': (2022, 10, 21), 'hour': '3:00', 'driver': '3'}, {'id': 5, 'latitud_collected': ('15.0000000000000000'), 'longitud_collected': ('15.0000000000000000'), 'latitud_destiny': ('18.0000000000000000'), 'longitud_destiny': ('18.0000000000000000'), 'date_order': (2022, 10, 21), 'hour': '6:00', 'driver': '3'}]
 
for i in data[0]:
    print(i)