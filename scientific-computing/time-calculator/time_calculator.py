
from mpsdate import Mpsdate


def add_time(start, duration, *day):

    start1=start.split()
    start2=start1[0].split(":")
    date=Mpsdate(0,start2[0],start2[1])
    if(start1[1]=="PM"):
        date.addHours(12)
    
    duration1=duration.split(":")
    date.addHours(duration1[0])
    date.addMinutes(duration1[1])

    date.adjust()
    if(len(day)==0):
        new_time=str(date.toString())
    else:
        new_time=str(date.toString(day))
    return new_time

print(add_time("11:59 PM", "24:05", "Wednesday"))

