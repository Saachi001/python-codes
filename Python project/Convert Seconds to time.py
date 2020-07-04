#User will enter the time in second and we have to show the time in number of Days, Hours, Minute and Seconds
#input seconds will be in numbers and output will have all the parts of the time i.e day, hour, minute, seconds
#You can assume that you will not enter the negative values. No decimal values.
second = int(input("Enter the time in seconds: "))
min_sec = 60
hour_min = 60
hour_second = hour_min * min_sec
day_hour = 24
day_second = day_hour * hour_second
day_count = second // day_second
remaining_sec = second % day_second
hour_count = remaining_sec // hour_second
remaining_sec = remaining_sec % hour_second
min_count = remaining_sec // min_sec
remaining_sec = remaining_sec % min_sec
sec_count = remaining_sec 
print(day_count, "Days", hour_count, "Hours", min_count, "Minutes", sec_count, "seconds")
