from datetime import date

today_date = date.today() #returns today's date as a date object
new_date = date(2023,7,26) #instantiates a date object for 26 July 2023
difference = new_date - today_date #calculate the difference between two date objects

print(difference.days) #display the difference in days
