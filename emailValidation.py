
def EmailCheck(Email):
	if re.match(r"^[A-Za-z\s][^@\s]*@[^@ | ^\.\s]+\.[a-zA-Z0-9\s]*[A-za-z]$",Email):
		if (Email.find('@')-Email.find('.')) == 1:
			return 0
		else: 
			return 1
	else:
		return 0

while True:
	print(EmailCheck(input()))
