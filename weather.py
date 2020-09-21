# from pyowm import OWM
# from pyowm.utils import timestamps
# from datetime import datetime, timedelta, timezone
#
# owm = OWM('4968d701b7cff093f479e2f8a65a0d45')  # You MUST provide a valid API key
#
# # Search for current weather in London (Great Britain)
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place('Chita,RU')
# w = observation.weather
# print(w)                  # <Weather - reference time=2013-12-18 09:20, status=Clouds>
#
# # # Weather details
# # w.wind()                  # {'speed': 4.6, 'deg': 330}
# # w.humidity                # 87
# # w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# # print(w.temperature('celsius'))
# # # Search current weather observations in the surroundings of
# # # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# # observation_list = mgr.weather_around_coords(-22.57, -43.12)
#
#
# # what is the epoch for 3 days ago at this time?
# three_days_ago_epoch = int((datetime.now() - timedelta(days=203)).replace(tzinfo=timezone.utc).timestamp())
# print(three_days_ago_epoch)
# one_call_three_days_ago = mgr.one_call_history(lat=52.5244, lon=13.4105, dt=three_days_ago_epoch)
#
# list_of_forecasted_weathers = one_call_three_days_ago.forecast_hourly
# print(list_of_forecasted_weathers)

from datetime import date, timedelta


def from_file(name):
    el = []
    with open(f'.\\data\\{name}') as f:
        for line in f:
            el.append(float(line.replace(',', '.').strip()))
    return el


temperature = from_file('weather.txt')
t1 = from_file('T1.txt')
t2 = from_file('T2.txt')
m1 = from_file('M1.txt')
m2 = from_file('M2.txt')
q = from_file('Q.txt')

t1_y = [t1 for _, t1 in sorted(zip(temperature, t1))]
t2_y = [t2 for _, t2 in sorted(zip(temperature, t2))]
m1_y = [m1 for _, m1 in sorted(zip(temperature, m1))]
m2_y = [m2 for _, m2 in sorted(zip(temperature, m2))]
q_y = [q for _, q in sorted(zip(temperature, q))]
print(q_y)


d1 = date(2020, 1, 1)  # начальная дата

delta = timedelta(days=len(temperature)-1)         # timedelta
date = [d1 + timedelta(i) for i in range(delta.days + 1)]

print(date)

