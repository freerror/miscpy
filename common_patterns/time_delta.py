import datetime
import time

time_now = datetime.datetime.now().timestamp()
hour_ago = (datetime.datetime.now() - datetime.timedelta(hours=1)).timestamp()
print(hour_ago > time_now)
print(time_now - hour_ago)
