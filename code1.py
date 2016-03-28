def show_Users(deviceName,users):
	deviceObj = Device.getDeviceObject(devicename)
	list_of_users = users.key()
	print list_of_users
	cmd = "show users"
	output = deviceObj.execute(cmd, mode="EXEC")
	output_split = output.splitlines()
	print output_split
	user_list = output_split[5:-1]
	print user_list
	for values in user_list:
		A = values.split()
		print A
		B = A[2]
		print B
		C = A[3]
		print C
		d = "{"+'"'+B+'"'+":"+'"'+C+'"'+"}"
		print D
		d = yaml.load(D)
		c = list.update(d)
		print c
