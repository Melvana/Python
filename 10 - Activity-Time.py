#Time, conditionals, from..import, for..else
#Tells you what you're doing at any time of day
from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              10: 'Working',
              13: 'Lunch',
              17: 'Working',
              18: 'Commuting',
              19: 'Wanking',
              20: 'Eating',
              22: 'Resting'}

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'I must be dead, who knows call me or something!'
