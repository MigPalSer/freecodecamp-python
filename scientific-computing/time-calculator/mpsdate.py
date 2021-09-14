class Mpsdate:
  days=0
  hours=0
  minutes=0
  #We consider every date at starting at 00:00 AM in day 0
  def __init__(self, days, hours, minutes):
    self.days=int(days)
    self.hours=int(hours)
    self.minutes=int(minutes)

  def addHours(self, hrs):
    self.hours+=int(hrs)

  def addMinutes(self, mins):
    self.minutes+=int(mins)

  def adjust(self):
    self.hours+=self.minutes//60
    self.minutes%=60

    self.days+=self.hours//24
    self.hours%=24

  def toString(self, *dayof):
    string=""
    zon=""
    if(self.hours<12): zon="AM" 
    else: zon="PM"
    if(self.hours>12): self.hours-=12
    #tontuna de ver las "12 AM"
    if(self.hours==0): self.hours+=12
    string+=str(self.hours)
    string+=":"
    if(self.minutes<10):
      string+="0"
    string+=str(self.minutes)
    string+=" "+zon

    if(len(dayof)>=1):
      dayoftheweek=self.codigodiario(dayof)
      if(dayoftheweek!=-1):
        dayoftheweek+=self.days
        dayoftheweek=self.ajustdayoftheweek(dayoftheweek)
        string+=", "+self.stringdiario(dayoftheweek)

    if(self.days==1):
      string+=" (next day)"
    elif(self.days>1):
      string+=" ("+str(self.days)+" days later)"
    return string
  
  def codigodiario(*stringa):
    stringo=stringa[1]
    stringu=str(stringo[0]).lower()
    st=stringu.strip("()\',")
    if(st=="monday"):
      return 1
    elif(st=="tuesday"):
      return 2
    elif(st=="wednesday"):
      return 3
    elif(st=="thursday"):
      return 4
    elif(st=="friday"):
      return 5
    elif(st=="saturday"):
      return 6
    elif(st=="sunday"):
      return 7
    else:
      return -1

  def ajustdayoftheweek(self, code):
    c=int(code)
    while(c>7):
      c-=7
    return c

  def stringdiario(self, coda):  
    if(coda==1):
      return "Monday"
    elif(coda==2):
      return "Tuesday"
    elif(coda==3):
      return "Wednesday"
    elif(coda==4):
      return "Thursday"
    elif(coda==5):
      return "Friday"
    elif(coda==6):
      return "Saturday"
    elif(coda==7):
      return "Sunday"
    else:
      return "ERROR"
