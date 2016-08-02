# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:41:40 2016

@author: RAVI TEJA
"""
print " "
print "Please enter year, month and date in numerical values"

#Manual Input of Date of Birth
xyear = int(raw_input('Given Year is - '))
xmonth = int(raw_input('Given Month is - '))
xday = int(raw_input('Given Date (Number) is - '))

#Basic Input Verification
if (xmonth > 12) or (xmonth < 1):
    print "invalid input"
elif (xyear > 9999) or (xyear < 1):
    print "Invalid Input"
elif (xday < 1) or (xday > 31):
    print "Invalid Input"
elif (xmonth == 2) and ((xyear%4)==0) and (xday > 29):
       print "Invalid Input"
elif ((xyear%100 == 0) and (xyear%400) > 0) and (xmonth == 2) and (xday > 28) :
       print "Invalid Input"
elif (xmonth == 2) and ((xyear%4) > 0) and (xday > 28):
    print "Invalid Input"
elif ((xmonth == 4) or (xmonth == 6) or (xmonth == 9) or (xmonth == 11)) and (xday > 30):
    print "Invalid Input"
  
else:  
#To determine the weekday of the birthday of the person
 #For this the assumption considered is that the first day of the calendar has started with SATURDAY
 #The Source for this assumption is - http://www.webexhibits.org/calendars/year-history.html
 # Another Source is - https://en.wikipedia.org/wiki/History_of_calendars
 
 #This Alogorith works perfectly from 14th September 1752. Because there 11 missing in september of 1752..
 #The Calendar has been changed. From September 2nd to September  to 14th September Missing 11 days.
 # Source -1: - http://www.timeanddate.com/calendar/?year=1752
 #Source 2 : - http://mentalfloss.com/article/51370/why-our-calendars-skipped-11-days-1752
 
 #So this logic has been developed considering tha fact that 14th September 1752 is considered as THURSDAY instead of Monday
 #http://www.genealogytoday.com/columns/everyday/030902.html
 if (xyear > 1752):
  def weekday(xday, xmonth, xyear):
      #If given year is a non leap Year
    if ((xyear%4) > 0) or (((xyear%100) == 0) and ((xyear%400) > 0)):
        list1 = [31,28,31,30,31,30,31,31,30,31,30,31] #Days of respective month
        countdays = 0
        for i in range (0,xmonth): #Day Count
            countdays = countdays + list1[i]
            
        excessdays = list1[xmonth-1] - xday #To remove additional days during count
        totdays = countdays - excessdays 
        yeardays = xyear * 365
        #a = 1
        leapcount = 0
        leap1count = 0
        null = 0
        for a in range (1,xyear): # To count the number of leap years
            
            if ((a%4) == 0) and ((a%100) > 0):
                leapcount = leapcount + 1
            elif (a%4 == 0) and (a%400 == 0):
                leap1count = leap1count + 1
            else:
                null +=1;
        totaldays = yeardays + totdays + leapcount + leap1count
                
        troll = totaldays%7 #To determine the day
        print " "
        if (troll == 0):
            print "This day is Saturday"
        elif (troll == 1):
            print "This day is Sunday"
        elif (troll == 2):
            print "This day is  Monday"
        elif (troll == 3):
            print "This day is  Tuesday"
        elif (troll == 4):
            print "This day is Wednesday"
        elif (troll == 5):
            print "This day is  Thursday"
        else:
            print "This day is  Friday"
    
    else:       
        #If given Year is a leap year
      if ((xyear%4) == 0):
        list1 = [31,29,31,30,31,30,31,31,30,31,30,31] #Days in a month of leap year
        countdays = 0
        for i in range (0,xmonth):
            countdays = countdays + list1[i]
            
        excessdays = list1[(xmonth) -1] - xday
        totdays = countdays - excessdays
        yeardays = (xyear) * 365
        a = 1
        leapcount = 0
        leap1count = 0
        null =0
        for a in range (1,xyear):
            
            if ((a%4) == 0) and ((a%100) > 0):
                leapcount = leapcount + 1
            elif ((a%4) == 0) and ((a%400) == 0):
                leap1count = leap1count + 1
                #print leap1count
            #else:
                #null += 1
        totaldays = yeardays + totdays + leapcount + leap1count
        
        troll = totaldays%7
        print ""
        if (troll == 0):
            print "This day is Saturday"
        elif (troll == 1):
            print "This day is Sunday"
        elif (troll == 2):
            print "This day is Monday"
        elif (troll == 3):
            print "This day is Tuesday"
        elif (troll == 4):
            print "This day is Wednesday"
        elif (troll == 5):
            print "This day is Thursday"
        else:
            print "This day is Friday"
            
  weekday(xday, xmonth, xyear)
    
 elif (xyear > 0) and (xyear <  1753):
     
  def weekday(xday, xmonth, xyear):
      #If given year is a non leap Year
    if ((xyear%4) > 0) or (((xyear%100) == 0) and ((xyear%400) > 0)):
        list1 = [31,28,31,30,31,30,31,31,30,31,30,31] #Days of respective month
        countdays = 0
        for i in range (0,xmonth): #Day Count
            countdays = countdays + list1[i]
            
        excessdays = list1[xmonth-1] - xday #To remove additional days during count
        totdays = countdays - excessdays 
        yeardays = xyear * 365
        #a = 1
        leapcount = 0
        leap1count = 0
        null = 0
        for a in range (1,xyear): # To count the number of leap years
            
            if ((a%4) == 0) and ((a%100) > 0):
                leapcount = leapcount + 1
            elif (a%4 == 0) and (a%400 == 0):
                leap1count = leap1count + 1
            else:
                null +=1;
        totaldays = yeardays + totdays + leapcount + leap1count
                
        troll = totaldays%7 #To determine the day
        print " "
        if (troll == 3):
            print "That Day is Saturday"
        elif (troll == 4):
            print "That Day is Sunday"
        elif (troll == 5):
            print "That Day is Monday"
        elif (troll == 6):
            print "That Day is Tuesday"
        elif (troll == 0):
            print "That Day is Wednesday"
        elif (troll == 9):
            print "That Day is Thursday"
        else:
            print "That Day is Friday"
        
        print " "
        print "This date/weekday may vary with Gregorian Calender due to conventional methodlogies followed at this time in past"    
        print "As no standard weekdays and dates were followed during this period"
        print "Each country had its own calendar and Conventions"
        print "For an instance missing 11 days in 1752, 1700 was made leap year, etc... "
        
    else:       
        #If given Year is a leap year
      if ((xyear%4) == 0):
        list1 = [31,29,31,30,31,30,31,31,30,31,30,31] #Days in a month of leap year
        countdays = 0
        for i in range (0,xmonth):
            countdays = countdays + list1[i]
            
        excessdays = list1[(xmonth) -1] - xday
        totdays = countdays - excessdays
        yeardays = (xyear) * 365
        a = 1
        leapcount = 0
        leap1count = 0
        null =0
        for a in range (1,xyear):
            
            if ((a%4) == 0) and ((a%100) > 0):
                leapcount = leapcount + 1
            elif ((a%4) == 0) and ((a%400) == 0):
                leap1count = leap1count + 1
                
            else:
                null += 1
        totaldays = yeardays + totdays + leapcount + leap1count
        
        troll = totaldays%7
        print " "
        if (troll == 3):
            print "This day is Saturday"
        elif (troll == 4):
            print "This day is Sunday"
        elif (troll == 5):
            print "This day is Monday"
        elif (troll == 6):
            print "This day is on Tuesday"
        elif (troll == 0):
            print "This day is Wednesday"
        elif (troll == 1):
            print "This day is Thursday"
        else:
            print "This day is Friday"
        
        print " "
        print "This date/weekday may vary with Gregorian Calender due to conventional methodlogies followed at this time in past"    
        print "As no standard weekdays and dates were followed during this period"
        print "Each country had its own calendar and Conventions"
        print "For an instance missing 11 days in 1752, 1700 was made leap year, etc... "
  weekday(xday, xmonth, xyear)
 else:
     print "Invalid Entry"

        