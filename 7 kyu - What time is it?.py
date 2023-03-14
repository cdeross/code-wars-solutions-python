'''
What time is it?

Given a time in AM/PM format as a string, convert it to military (24-hour) time as a string.
Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock,
and 12:00:00 on a 24-hour clock
Sample Input: 07:05:45PM Sample Output: 19:05:45
Try not to use built in DateTime libraries
'''

def get_military_time(time):
    if time[-2:] == "AM":
        if time[:2] == "12":
            return "00" + time[2:-2]
        else:
            return time[:-2]
    else:
        if time[:2] == "12":
            return time[:-2]
        else:
            hour = str(12 + int(time[:2]))
            return hour + time[2:-2]