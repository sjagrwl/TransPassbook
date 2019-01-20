import time
date=input("Enter the date: ")

min_year = 1900
max_year = min_year + 200
date1=time.strftime("%d/%m/%Y")
days_31 = ['01', '03', '05', '07', '08', '10', '12']
days_30 = ['04', '06', '10', '11']
days_28 = ['02']

month_dict = {'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'}

def validate(day,month,leap_year_or_not):
	#print(leap_year_or_not)
	if (leap_year_or_not):
		max_day = '29'
	else:
		max_day='28'
	if (month in days_28):
		if (day > max_day):
			#print ("Invalid day: %s for month %s" %(day,month_dict[month]))
			return 0
		else:
			#print("valid")
			return 1
	elif (month in days_30):
		if (day > '30'):
			#print ("Invalid day: %s for month %s" %(day,month_dict[month]))
			return 0
		else:
			#print("valid")
			return 1
	elif (month in days_31):
		if (day <= '31'):
			#print("valid")
			return 1
		else:
			#print ("Invalid day: %s for month %s" %(day,month_dict[month]))
			return 0
	else:
		#print ("Invalid month:%s, Invalid day:%s" %(month,day))
		return 0

if (len(date)!= 10):
	#print ("Invalid Format. Please enter date in DD/MM/YYYY")
	k=0
else:
	day,month,year = date.split("/")
	day1,month1,year1=date1.split("/")
	if (len(day) != 2):
		k=0
		#print ("Length of day in not 2. Please enter day as 01 for first!") 
	elif (len(month) != 2):
		k=0
		#print ("Length of month in not 2.Please enter month as 01 for January!")
	elif (len(year) != 4):
		k=0
		#print ("Length of year in not 4. Please enter year as 2001!")
	elif(year1<year):
		#print("invalid")
		k=0
	elif(year1==year):
		if(month1>month):
			#print("invalid")
			k=0
		elif(month1==month):
			if(day1<day):
				#print("invalid")
				k=0
			
	else:
		#day=int(day)
		#month=int(month)
		#year=int(year)
		if (day < '01' or day > '31'):
			#print ("Day %s is not in range [1-31]"%str(day))
			k=0
		if (month < '01' or month > '12'):
				#print ("Month %s is not in range [1-12]" %str(month))
				k=0
			
		if (int(year) < min_year or int(year) > max_year):
					#print ("Year is not in range [%d-%d]" %(min_year,max_year))
					k=0
		else:
			if (int(year)%4 == 0):
				leap_year =True
			else:
				leap_year =False
			k = validate(day,str(month).zfill(2),leap_year)
print(k)
