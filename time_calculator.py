def add_time(start, duration, dayOfWeek = None):

	new_time = ""

	#Conversion of Start 12 hour format to 24 hour format
	startFormat = start.split(" ")
	startTime = startFormat[0].split(":")
	startAmPm = startFormat[1]
	startHour = int(startTime[0])
	startMinute = int(startTime[1])

	if startAmPm == "PM" :
		startHour += 12

	#Conversion of Start hours into minutes
	startMinute += (60 * startHour)

	#Conversion of duration hours into minutes
	durationTime = duration.split(":")
	durationHour = int(durationTime[0])
	durationMinute = int(durationTime[1])

	#Conversion of Duration hours into minutes
	durationMinute += (60 * durationHour)

	#Total minutes
	minutes = startMinute + durationMinute

	#Minute calculation
	finalMinutes = minutes % 60
	hours = int(minutes // 60)

	new_time = "0" + str(finalMinutes) if len(str(finalMinutes)) == 1 else str(finalMinutes)

	#Days calculation
	hour = hours % 24
	days = int(hours // 24)

	#Hour and AM/PM calculation
	finalHours = hour % 12
	finalAmPm = 'AM'  if int(hour // 12) == 0 else 'PM'
	if finalHours == 0:
			finalHours = 12

	new_time = str(finalHours) + ':' + new_time + ' ' + finalAmPm

	#Calculation of day of day Of Week
	if not dayOfWeek == None:
		daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		pos = 0
		while True:
			if dayOfWeek.lower() == daysOfWeek[pos].lower():
				break
			pos += 1
		newDayOfWeek = daysOfWeek[((pos + (days % 7)) % 7)]
		new_time += ", " + newDayOfWeek

	#Final output
	if days == 1:
		new_time += " (next day)"
	elif days > 1:
		days = str(days)
		new_time += " (" + days + " days later)"

	return new_time
