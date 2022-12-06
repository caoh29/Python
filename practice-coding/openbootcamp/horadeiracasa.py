import time

current_time_s = time.time()
current_time = time.ctime(current_time_s)

if current_time.startswith("Sat") or current_time.startswith("Sun"):
    print("Weekend Time!")

if int(current_time[11:13]) >= 19:
    print("Time to go home!")
else:
    remaining_hours = 18 - int(current_time[11:13])
    remaining_minutes = 60 - int(current_time[14:16])
    remaining_seconds = 60 - int(current_time[17:19])
    print(f"The current time is {current_time}")
    print(f"The remaining time to go home at 7 pm is {remaining_hours}:{remaining_minutes}:{remaining_seconds}")