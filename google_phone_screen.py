# You have a digital clock in front of you that shows the time is 12h format (e.g. 2:07PM, midnight: 0:00AM, noon: 12:00PM).
# On the back there are 4 buttons:
# Advance time by 1 minute
# Advance time by 5 minutes
# Advance time by 15 minutes
# Advance time by 1 hour
# You need to implement a method to set the clock to a given time from the current time the clock is showing, with the least
# amount of button presses
# You can assume that the clock interface is a class that support the following operations:

Clock.getCurrentTime() # returns the current time as [HH, MM, "AM"|"PM"], same format as the given time
Clock.adv1Min()        # advances the clock by 1 minute
Clock.adv5Min()        # advances the clock by 5 minutes
Clock.adv15Min()       # advances the clock by 15 minutes
Clock.adv1hr()         # advances the clock by 1 hour


# 1:00am -> 3:17am
# 1:00pm -> 2:00am   2pm -> 3pm ..... -> 11pm -> 0am -> 1am -> 2am, 13 times
 780min -> 120min, 120min + 24*60 = 1560min
 -660min + 1440min = 780min, 780 // 60 = 13
def getMinutes(time):
  #TODO: think about edge cases and bad input
  mins = 0
  if time[2] == "PM":
    mins += (time[0] + 12)*60
  elif time[2] == "AM":
    mins += time[0]*60

  mins += time[1]

  return mins

def setTimeTo(clock, newTime): #[1, 0, AM]
  curTime = Clock.getCurrentTime()
  minutesToSet = getMinutes(newTime) - getMinutes(curTime) #- 60 * 13
  if minutesToSet < 0:
    minutesToSet += 24*60

  cntHours = minutesToSet // 60 #1
  for i in range(cntHours):
    Clock.adv1hr()

  cntQuaters = minutesToSet - cntHours*60 // 15 #0
  for i in range(cntQuaters):
    Clock.adv15Min()

  cntFives = (curTime[1] - curTime[1] // 15) // 5 #0

  for i in range(cntFives):
    Clock.adv5Min()

  cntOnes = curTime[1] - cntQuaters - cntFives #0

  for i in range(cntOnes):
    Clock.adv1Min()




  
