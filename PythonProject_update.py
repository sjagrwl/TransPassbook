import os
import sys
import time
import getpass
import re

def EmailCheck(Email):
	if re.match(r"^[A-Za-z\s][^@\s]*@[^@ | ^\.\s]+\.[a-zA-Z0-9\s]*[A-za-z]$",Email):
		if (Email.find('@')-Email.find('.')) == 1:
			return 0
		else: 
			return 1
	else:
		return 0

def dateValidation(date):
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
	return k

############################################################################################################################################
#Welcome Panel
class EntryPanel():
	def Login(self):
		os.system('clear')
		print()		
		print("-----------------------------------------------------------------------------------------------------------------------------------------------")
		print("\t\t\t\t\t\t\t  Hello, User")
		print("-----------------------------------------------------------------------------------------------------------------------------------------------")		
		
		LoginId=""
		Password=""
		
		print("\n\n\nPlease enter your Login Id and password (Both Case-sensitive):")

		LogOut=0	
		Trans=0
		Trans1=0

		while LogOut==0:		
			print("\n\n=>\tLogin ID: ",end="")
		
			while(LoginId==""):
				LoginId=input()
				if LoginId =="":
					print("\nThe Field cannot be left empty.\n") 			
					print("=>\tLogin ID: ",end="")
			
			while(Password==""):
				Password=getpass.getpass("\n=>\tPassword: ")			
				
				if Password =="":
					print("\nThe Field cannot be left empty.")
	
			try:
				fp=open("UserList.txt","r")
			except:
				print("\n The Login ID is invalid or non-existent")
				LoginId=""				
				Password=""
				Trans=1				

			else:
				buff=fp.readlines()
				for var in range(0,len(buff)):
					if LoginId != buff[var].split("**")[0] or Password != buff[var].split("**")[1]  :
						Trans=1
						Trans1=1
						fp.close()		

					else:
						fp1=open(LoginId+".txt","a")
						LogOut=1

						time.ctime()
						LoginTime=time.strftime('%l:%M:%S %p   %b %d, %Y')
						fp1.write("*\n"+LoginTime+"\n")

						fp.close()
						fp1.close()
						
						y=Passbook()
						y.WelcomePanel(var,LoginId,LoginTime)

						Trans=0
						Trans1=0
						break
			if Trans1==1:
				print("\n The Login ID or Password is invalid or non-existent")

			if Trans==1:	
				print("\nPress 1 to Sign Up, 2 to Try Again or 3 to Exit") 	
				branch={1:"self.SignUp()",3:"sys.exit()",4:"\nInvalid choice"}
				print("\n=>\tYOUR CHOICE:  ",end="")				
				while(True):
					try:
						choice=int(input())
					except:
						choice=5
					if choice==1 or choice==3:
						LogOut=1
						eval(branch.get(choice))
						break
					elif choice==2:
						LoginId=""				
						Password=""
						Trans=0						
						break
					else:
						print(branch.get(4))
						print("\n=>\tYOUR CHOICE:  ",end="")	
	
	
	def SignUp(self):
		
		os.system('clear')
		print()			   				  
		print("-----------------------------------------------------------------------------------------------------------------------------------------------")
		print ("\t\t\t\t\t|           Welcome To The SignUp Portal.              |")
		print ("\t\t\t\t\t|   Kindly Enter The Valid Details As Per Instructed.  | :)")
		print("-----------------------------------------------------------------------------------------------------------------------------------------------")						
		
		FirstName=""
		LastName=""		
		DateOfBirth=""
		Address=""
		Contact=""
		Email=""
		LoginId=""
		Password=""
	
		print ("\n\n\n  Enter the details below : ")
		print ("\n\n=>\tFirst Name: ",end="")

		while(FirstName==""):		
			FirstName=input()
			if FirstName =="":
				print("\nThe Field cannot be left empty.\n")
				print ("=>\tFirst Name: ",end="")

		print("\n=>\tLast Name: ",end="")
		
		while(LastName==""):
			LastName=input()
			if LastName =="":
				print("\nThe Field cannot be left empty.\n")
				print("=>\tLast Name: ",end="")

		print("\n=>\tDate Of Birth (DOB)[dd/mm/yy]: ",end="")

		while(DateOfBirth==""):		

			try:
				DateOfBirth=input()				

			except:
				print("\nEnter a valid Date")

			else:
				p=dateValidation(DateOfBirth)
				if(p==0):
					print("\nEnter a valid Date\n")
					print("=>\tDate Of Birth (DOB)[dd/mm/yy]: ",end="")
					DateOfBirth =""
		
			#if DateOfBirth =="":
			#	print("\nThe Field cannot be left empty.\n")
			#print("=>\tDate Of Birth (DOB)[dd/mm/yy]: ",end="")
	

		print("\n=>\tResidential Address: ",end="")

		while(Address==""):	
			Address=input()
			if Address =="":
				print("\nThe Field cannot be left empty.\n")
				print("=>\tResidential Address: ",end="")
		
		print("\n=>\tContact Number[7 or 10 digit]: ",end="")

		while(Contact==""):
			try:
				tryc1=input()
				trycontact=int(tryc1)				

			except:
				print("\nEnter a valid no.")

			else:
				Contact=tryc1
				if len(Contact)!=7 and len(Contact)!=10:
					print("\nEnter a valid no.")
					Contact=""
		
			if Contact =="":
				if tryc1=="":
					print("\nThe Field cannot be left empty.")
				print("\n=>\tContact Number[7 or 10 digit]: ",end="")
	
		print("\n=>\tEmail Address: ",end="")

		while(Email==""):
			Email=input()
			if Email =="":
				print("\nThe Field cannot be left empty.\n") 			
				print("=>\tEmail Address: ",end="")	
			q=EmailCheck(Email)
			if(q==0):
				print("\nEnter Valid Email Address\n")
				print("=>\tEmail Address: ",end="")	
				Email=""

		os.system('clear')
		print()
		print("-----------------------------------------------------------------------------------------------------------------------------------------------")
		print("\t\t\t\t\t\t\t  Hello, "+FirstName +" "+ LastName)
		print("-----------------------------------------------------------------------------------------------------------------------------------------------")		
		print("\n\n\nPlease set your Login Id and password :")
		
		MakeLog=0		

		while MakeLog==0:	
			print("\n\n=>\tLogin ID: ",end="")
			
			while(LoginId==""):
				LoginId=input()
				if LoginId =="":
					print("\nThe Field cannot be left empty.\n") 			
					print("=>\tLogin ID: ",end="")
			
		
			while(Password==""):
				Password=getpass.getpass("\n=>\tPassword: ")
				asterisk=""
				for var in range(0,len(Password)):
					asterisk+="*"
				if Password!="":
					print("\n\t\" "+asterisk+" \"")				
				
				if Password =="":
					print("\nThe Field cannot be left empty.")
				else:
					ConPass=getpass.getpass("\n=>\tConfirm Password: ")
					if(ConPass!=Password):
						print("\nPasswords Do Not Match.")					
						Password=""
			MakeLog=0
	
			try:
				fp=open("UserList.txt","r")
			except:
				MakeLog=1	
			else:
				buff=fp.readlines()
				fp.close()
				for var in range(0,len(buff)):
					if (LoginId)==buff[var].split("**")[0]:
						print("\nLogin already exists.")
						print("\nPassword has not been reset. Try Entering a Different Login ID. ")
						MakeLog=0
						LoginId=""
						Password=""
						break
					else:
						MakeLog=1
					
			if(MakeLog==1):
	
				fp=open("UserList.txt","a")
				fp1=open(LoginId+".txt","w")
				fp.write(LoginId+"**"+Password+"**")
	
				fp.write(FirstName+"**"+LastName+"**"+DateOfBirth+"**"+Address+"**"+Contact+"**"+Email+"\n")
	
				fp.close()
				fp1.close()
				print("\n\n\nYour Login ID has been created Successfully.") 	
	
				time.sleep(1)
	
				self.WelcomePanel()
				break
			
	def WelcomePanel(self):

		os.system('clear')
		print()			   				   
		time.ctime()
		print("-----------------------------------------------------------------------------------------------------------------------------------------------")
		print ("\t\t\t\t\t\t\t| Welcome Dear User |                            Entry Time: " + time.strftime('%l:%M:%S %p   %b %d, %Y'))
		print("-----------------------------------------------------------------------------------------------------------------------------------------------")
	#Options

		print("\n\n\n\n\n\n\n=>\tPress 1 if you are already using our services.\n\n=>\tPress 2 if you are a new user and want to Sign Up.\n\n=>\tPress 3 if you want to EXIT.\n\n\n\n YOUR CHOICE:  ",end="")

		branch={1:"self.Login()",2:"self.SignUp()",3:"sys.exit()",4:"\nInvalid choice\n"}
		while(True):
			try:
				choice=int(input())
			except:
				choice=5
			if(choice in range(1,4)):
				eval(branch.get(choice))
				break
			else:
				print(branch.get(4))
				print(" YOUR CHOICE:  ",end="")

############################################################################################################################################

#PassBook
class Passbook():
		def AddEntry(self,position,LoginId,LoginTime):
			fp=open("UserList.txt","r")
			fp1=open(LoginId+".txt","r")
			
			os.system('clear')
			print()
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")
			print("\t\t\t\t\t\t\tTransaction Entry Portal (TEP)")
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")		
			
			TransactionId=""
			TransactionDate=""		
			TransactionType=""
			TransactionAmount=""
		
			buff=fp1.readlines()

			print ("\n\n\n Please Enter the Transaction Details below : ")
			print ("\n\n=>\tTransaction ID: ",end="")
	
			while(TransactionId==""):		
				TransactionId=input()
				if TransactionId =="":
					print("\nThe Field cannot be left empty.\n")
					print ("=>\tTransaction ID: ",end="")
				else:
					for var in range(0,len(buff)):
							if TransactionId == buff[var].split("**")[0]:
								print("\nThe particular Transaction ID already exists.\n")
								print ("=>\tTransaction ID: ",end="")								
								TransactionId=""
								break

			print("\n=>\tTransaction Date [dd/mm/yy]: ",end="")
	
			while(TransactionDate==""):		
				TransactionDate=input()
				if TransactionDate =="":
					print("\nThe Field cannot be left empty.\n")
					print("=>\tTransaction Date [dd/mm/yy]: ",end="")
	
			print("\n=>\tTransaction Type [Online, Cash, etc.]: ",end="")
	
			while(TransactionType==""):	
				TransactionType=input()
				if TransactionType =="":
					print("\nThe Field cannot be left empty.\n")
					print("=>\tTransaction Type: ",end="")
			
			print("\n=>\tTransaction Amount: ",end="")
	
			while(TransactionAmount==""):
				try:
					tryTA1=input()
					tryTransactionAmount=float(tryTA1)				
	
				except:
					print("\nEnter a valid Transaction Amount")
	
				else:
					TransactionAmount=tryTA1
			
				if TransactionAmount =="":
					if tryTA1=="":
						print("\nThe Field cannot be left empty.")
					print("\n=>\tTransaction Amount: ",end="")

			fp1.close()
		
			fp1=open(LoginId+".txt","a")			

			fp1.write(TransactionId+"**"+TransactionDate+"**"+TransactionType+"**"+TransactionAmount+"\n")			
			print("\n\n\nYour Transaction Entry has been Recorded Successfully.") 			
							
			time.sleep(1)			

			fp.close()
			fp1.close()
			
			self.WelcomePanel(position,LoginId,LoginTime)

		def ModifyEntry(self,position,LoginId,LoginTime):
			fp=open("UserList.txt","r")
			fp1=open(LoginId+".txt","r")
	
			os.system('clear')
			print()
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")
			print("\t\t\t\t\t\t\tTransaction Modification Portal (TMP)")
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")		
			
			print ("\n\n\n=>\t Press 1 to modify a transaction by Transaction ID.\n\n=>\t Press 2 if you want to see your Existing Transaction Details.\n\n=>\t Press 3 to Go Back.\n\n=>\t Press 4 to Exit")

			branch={1:"",2:"self.ViewEntry(position,LoginId,LoginTime)",3:"self.WelcomePanel(position,LoginId,LoginTime)",4:"sys.exit()",5:"\nInvalid choice\n"}
			print("\n\n\n\n=>\tYOUR CHOICE:  ",end="")				
			while(True):
				try:
					choice=int(input())
				except:
					choice=5
				if(choice in range(1,5)):
					if choice!=1:
						eval(branch.get(choice))
						if choice==2:
							print ("\n\n Press 1 to Go Back To TMP, Press 2 if you want to Exit\n")

							branch={1:"",2:"sys.exit()",3:"\nInvalid choice\n"}
							print("\n\n=>\tYOUR CHOICE:  ",end="")				
							while(True):
								try:
									choice=int(input())
								except:
									choice=3
								if(choice in range(1,3)):
									if choice!=1:
										eval(branch.get(choice))
									break
								else:
									print(branch.get(3))
									print(" YOUR CHOICE:  ",end="")
					break
				else:
					print(branch.get(5))
					print("\n=>\tYOUR CHOICE:  ",end="")

			os.system('clear')
			print()
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")
			print("\t\t\t\t\t\t\tTransaction Modification Portal (TMP)")
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")		
	
		
			print ("\n\n\n Please Enter The Transaction Detail you want to Modify: ")

			while(True):	
				fp1.seek(0)
				TransactionId=""		
				TransIdCheck=0			
						
				print ("\n\n=>\tTransaction ID: ",end="")
		
				while(TransactionId==""):		
					TransactionId=input()
					if TransactionId =="":
						print("\nThe Field cannot be left empty.\n")
						print ("=>\tTransaction ID: ",end="")
				
				buff=fp1.readlines()
				
				for var in buff:
					if var.find("**")!=-1:
						if var.split("**")[0]==TransactionId:
							TransIdCheck=1
							break
						else:
							TransIdCheck=0
				
				if TransIdCheck==1:
					fp.close()
					fp1.close()
					
					TransactionId=""
					TransactionDate=""		
					TransactionType=""
					TransactionAmount=""
		
					print ("\n\n\n Please Enter the Modified Transaction Details below : ")
					print ("\n\n=>\tTransaction ID: ",end="")
	
					while(TransactionId==""):		
						TransactionId=input()
						if TransactionId =="":
							print("\nThe Field cannot be left empty.\n")
							print ("=>\tTransaction ID: ",end="")
	
					print("\n=>\tTransaction Date [dd/mm/yy]: ",end="")
			
					while(TransactionDate==""):		
						TransactionDate=input()
						if TransactionDate =="":
							print("\nThe Field cannot be left empty.\n")
							print("=>\tTransaction Date [dd/mm/yy]: ",end="")
			
					print("\n=>\tTransaction Type [Online, Cash, etc.]: ",end="")
		
					while(TransactionType==""):	
						TransactionType=input()
						if TransactionType =="":
							print("\nThe Field cannot be left empty.\n")
							print("=>\tTransaction Type: ",end="")
					
					print("\n=>\tTransaction Amount: ",end="")
			
					while(TransactionAmount==""):
						try:
							tryTA1=input()
							tryTransactionAmount=float(tryTA1)				
			
						except:
							print("\nEnter a valid Transaction Amount")
			
						else:
							TransactionAmount=tryTA1
					
						if TransactionAmount =="":
							if tryTA1=="":
								print("\nThe Field cannot be left empty.")
							print("\n=>\tTransaction Amount: ",end="")
		
					fp=open("UserList.txt","r")
					fp1=open(LoginId+".txt","r+")			
					
					buff = fp1.readlines()

					fp1.seek(0)
					for i in buff:
						if i != var:
							fp1.write(i)
						else:
							fp1.write(TransactionId+"**"+TransactionDate+"**"+TransactionType+"**"+TransactionAmount+"\n")

					fp1.truncate()
					print("\n\n\nYour Transaction Entry has been Modified Successfully.") 	

					time.sleep(1)

					fp.close()
					fp1.close()

					self.WelcomePanel(position,LoginId,LoginTime)
					break
				else:
					print("\n The transaction ID is invalid or non-existent")
	
					print ("\n Press 1 to Try Again, Press 2 to GO Back or Press 3 to Exit")

					branch={1:"",2:"self.ModifyEntry(position,LoginId,LoginTime)",3:"sys.exit()",4:"\nInvalid choice\n"}
					print("\n\n=>\tYOUR CHOICE:  ",end="")				
					while(True):
						try:
							choice=int(input())
						except:
							choice=4
						if(choice in range(1,4)):
							if choice!=1:						
								eval(branch.get(choice))
							break
						else:
							print(branch.get(4))
							print("\n=>\tYOUR CHOICE:  ",end="")	


			fp.close()
			fp1.close()

		def DeleteEntry(self,position,LoginId,LoginTime):
			fp=open("UserList.txt","r")
			fp1=open(LoginId+".txt","r")
	
			os.system('clear')
			print()
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")
			print("\t\t\t\t\t\t\tTransaction Deletion Portal (TDP)")
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")		
			
			print ("\n\n\n=>\t Press 1 to delete a transaction by Transaction ID.\n\n=>\t Press 2 if you want to see your Existing Transaction Details.\n\n=>\t Press 3 to Go Back.\n\n=>\t Press 4 to Exit")

			branch={1:"",2:"self.ViewEntry(position,LoginId,LoginTime)",3:"self.WelcomePanel(position,LoginId,LoginTime)",4:"sys.exit()",5:"\nInvalid choice\n"}
			print("\n\n\n\n=>\tYOUR CHOICE:  ",end="")				
			while(True):
				try:
					choice=int(input())
				except:
					choice=5
				if(choice in range(1,5)):
					if choice!=1:
						eval(branch.get(choice))
						if choice==2:
							print ("\n\n Press 1 to Go Back To TDP, Press 2 if you want to Exit\n")

							branch={1:"",2:"sys.exit()",3:"\nInvalid choice\n"}
							print("\n\n=>\tYOUR CHOICE:  ",end="")				
							while(True):
								try:
									choice=int(input())
								except:
									choice=3
								if(choice in range(1,3)):
									if choice!=1:
										eval(branch.get(choice))
									break
								else:
									print(branch.get(3))
									print(" YOUR CHOICE:  ",end="")
					break
				else:
					print(branch.get(5))
					print("\n=>\tYOUR CHOICE:  ",end="")

			os.system('clear')
			print()
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")
			print("\t\t\t\t\t\t\tTransaction Deletion Portal (TDP)")
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")		
	
		
			print ("\n\n\n Please Enter The Transaction Detail you want to Delete: ")

			while(True):	
				fp1.seek(0)
				TransactionId=""		
				TransIdCheck=0			
						
				print ("\n\n=>\tTransaction ID: ",end="")
		
				while(TransactionId==""):		
					TransactionId=input()
					if TransactionId =="":
						print("\nThe Field cannot be left empty.\n")
						print ("=>\tTransaction ID: ",end="")
				
				buff=fp1.readlines()
				
				for var in buff:
					if var.find("**")!=-1:
						if var.split("**")[0]==TransactionId:
							TransIdCheck=1
							break
						else:
							TransIdCheck=0
				if TransIdCheck==1:
					fp.close()
					fp1.close()
					
					fp=open("UserList.txt","r")
					fp1=open(LoginId+".txt","r+")			
					
					buff = fp1.readlines()

					fp1.seek(0)
					for i in buff:
						if i != var:
							fp1.write(i)

					fp1.truncate()
					print("\n\n\nYour Transaction Entry has been Deleted Successfully.") 	

					time.sleep(1)

					fp.close()
					fp1.close()

					self.WelcomePanel(position,LoginId,LoginTime)
					break

				else:
					print("\n The transaction ID is invalid or non-existent")
	
					print ("\n Press 1 to Try Again, Press 2 to GO Back or Press 3 to Exit")

					branch={1:"",2:"self.DeleteEntry(position,LoginId,LoginTime)",3:"sys.exit()",4:"\nInvalid choice\n"}
					print("\n\n=>\tYOUR CHOICE:  ",end="")				
					while(True):
						try:
							choice=int(input())
						except:
							choice=4
						if(choice in range(1,4)):
							if choice!=1:						
								eval(branch.get(choice))
							break
						else:
							print(branch.get(4))
							print("\n=>\tYOUR CHOICE:  ",end="")	



			fp.close()
			fp1.close()
			
		def ViewEntry(self,position,LoginId,LoginTime):
			fp=open("UserList.txt","r")
			fp1=open(LoginId+".txt","r")

			os.system('clear')
			print()
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")
			print("\t\t\t\t\t\tTransaction Details Display Portal (TDDP)")
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")				

			buff=fp1.readlines()
			f=0
			for var in buff:
				display=""
				display1=""				
				if var!="*\n":
					if var.find("**")!=-1:					
						var=var.split("**")
						for var1 in var:
							display+=var1+"\t\t"
					else:
						display1+="Login Time:  "+var
									
					if display1!="":
						if f==1:
							print("No Transactions\n")
							f=0
						print(display1)
						f=1
					if display!="": 
						print(display)
						f=0

			if f==1:
				print("No Transactions\n")
				f=0			
			fp.close()
			fp1.close()
	
			print ("\n Press 1 to Go Back to PMS or Press 2 to Exit")

			branch={1:"self.WelcomePanel(position,LoginId,LoginTime)",2:"sys.exit()",3:"\nInvalid choice\n"}
			print("\n\n=>\tYOUR CHOICE:  ",end="")				
			while(True):
				try:
					choice=int(input())
				except:
					choice=3
				if(choice in range(1,3)):						
						eval(branch.get(choice))

				else:
					print(branch.get(3))
					print("\n=>\tYOUR CHOICE:  ",end="")

		def LogOut(self):
			x.WelcomePanel()

		def WelcomePanel(self,position,LoginId,LoginTime):

			os.system('clear')
			fp=open("UserList.txt","r")
			buff=fp.readlines()
			fp1=open(LoginId+".txt","a")
			print()		
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")
			print (" PassBook Main Space (PMS) \t\t\t\t| Welcome, "+buff[position].split("**")[2].title()+" "+buff[position].split("**")[3].title()+" |"    + "                     Login Time: " + LoginTime)	   				   
			print("-----------------------------------------------------------------------------------------------------------------------------------------------")
		#Options
	
			print("\n\n\n\n\n\n\n=>\tPress 1 if you want to register a new Transaction Entry.\n\n=>\tPress 2 if you want to modify an existing Transaction Entry.\n\n=>\tPress 3 if you want to delete an existing Transaction Entry.\n\n=>\tPress 4 if you want to view your Complete Transaction History.\n\n=>\tPress 5 if you want to Log Out.\n\n\n\n YOUR CHOICE:  ",end="")

			branch={1:"self.AddEntry(position,LoginId,LoginTime)",2:"self.ModifyEntry(position,LoginId,LoginTime)",3:"self.DeleteEntry(position,LoginId,LoginTime)",4:"self.ViewEntry(position,LoginId,LoginTime)",5:"self.LogOut()",6:"\nInvalid choice\n"}
			while(True):
				try:
					choice=int(input())
				except:
					choice=6
				if(choice in range(1,6)):
					fp.close()
					fp1.close()
					eval(branch.get(choice))
					break
				else:
					print(branch.get(6))
					print(" YOUR CHOICE:  ",end="")
	
			
#MAIN
############################################################################################################################################	
x=EntryPanel()
x.WelcomePanel()

