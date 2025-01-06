def delivery(numberOne):
	rider_pay = 0

	if numberOne >= 70:
		rider_pay = numberOne * 500 + 5000 

	elif numberOne >= 60:
		rider_pay = numberOne * 250 + 5000 

	elif numberOne >= 50:
		rider_pay = numberOne * 200 + 5000 

	else:
		rider_pay = numberOne * 160 + 5000 


	return rider_pay